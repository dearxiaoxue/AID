from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from login.models import *
from time import *
import json

set_time_morning = '09:00:00'
set_time_night = '21:00:00'


# Create your views here.
# 主页
def index(request):
    # 判断 员工的权限 返回不同网页
    user_name = request.session.get('uname')
    user = Users.objects.get(username=user_name)
    employee = user.employee_set.all()[0]
    print(user_name)
    print(user.intro)
    if user.intro == 'admin':
        return render(request, "cwa/cwa-users-adm.html")
    else:
        return render(request, 'cwa/cwa-users.html',locals())

# 获取当前session的信息
def get_session(request):
    username = request.session.get('uname')
    # print(username)
    user = Users.objects.get(username=username)
    employee = user.employee_set.all()
    # print(employee)
    user = {
        'id':employee[0].id,
        'name':employee[0].em_name,
    }
    return HttpResponse(json.dumps(user))

# 签到
def log_in(request):
    if request.method == 'GET':
        uid = request.GET.get('uid')
        time = strftime('%Y-%m-%d')
        # print(uid,time)
        user = Attendance_status.objects.filter(time=time, uid=uid)
        # print(user)
        if len(user)==0:
            return HttpResponse(json.dumps(0))
        else:
            return HttpResponse(json.dumps(1))
    else:
        user = Attendance_status()
        user.uid = request.POST.get('uid')
        # print(user.uid)
        user.name = request.POST.get('name')
        # print(user.name)
        user.time = strftime('%Y-%m-%d')
        log_in = strftime('%H:%M:%S')
        # print(log_in)
        user.log_in = log_in
        if log_in > set_time_morning:
            user.isActive = '迟到'
            # print(user.isActive)
        try:
            user.save()
            str = json.dumps('签到成功')
            # print(str)
            return HttpResponse(str)
        except:
            return json.dumps('签到失败')

# 签退
def log_back(request):
    if request.method == 'GET':
        uid = request.GET.get('uid')
        # print(uid)
        time = strftime('%Y-%m-%d')
        # print(time)
        user = Attendance_status.objects.filter(uid=uid, time=time)
        # print(user)
        if len(user) == 0:
            return HttpResponse(json.dumps(2))
        else:
            if user[0].log_back == '未签退':
                return HttpResponse(json.dumps(0))
            else:
                return HttpResponse(json.dumps(1))

    else:
        uid = request.POST.get('uid')
        # print(uid)
        time = strftime('%Y-%m-%d')
        # print(time)
        user = Attendance_status.objects.get(uid=uid, time=time)
        # print(user)
        act = user.isActive
        log_back = strftime('%H:%M:%S')
        user.log_back = log_back
        # print(log_back)
        if log_back < set_time_night:
            if act == '迟到':
                user.isActive = act + ',' + '早退'
                try:
                    user.save()
                    return HttpResponse(json.dumps('签退成功'))
                except:
                    return HttpResponse(json.dumps('签退失败'))
            else:
                user.isActive = '早退'
                try:
                    user.save()
                    return HttpResponse(json.dumps('签退成功'))
                except:
                    return HttpResponse(json.dumps('签退失败'))

# 查找
def find_one(request):
    uid = request.POST.get('uid')
    date = request.POST.get('date')
    day = request.POST.get('day')
    # print(uid, date, day)
    if day != '':
        time = date + '-' + day
        # print(time)
        users = Attendance_status.objects.filter(uid=uid, time=time).order_by('-time')
        s = ''
        for user in users:
            s += "%s_%s_%s_%s_%s_%s|" % (
                user.uid, user.name, user.time, user.log_in, user.log_back, user.isActive)
        str = json.dumps(s[0:-1])
        return HttpResponse(str)
    else:
        users = Attendance_status.objects.filter(uid=uid, time__startswith=date).order_by('-time')
        # print(users)
        s = ''
        for user in users:
            s += "%s_%s_%s_%s_%s_%s|" % (user.uid, user.name, user.time, user.log_in, user.log_back, user.isActive)
        str = json.dumps(s[0:-1])
        # print(str)
        return HttpResponse(str)

# 查找当天考勤异常
def find_all(request):
    time = strftime('%Y-%m-%d')
    users = Attendance_status.objects.filter(time=time).exclude(isActive='正常').order_by('-time')
    # print(users)
    s = ''
    for user in users:
        s += "%s_%s_%s_%s_%s_%s|" % (
            user.uid, user.name, user.time, user.log_in, user.log_back, user.isActive)
    str = json.dumps(s[0:-1])
    return HttpResponse(str)

def alter(request):
    msg = request.GET.get('user')
    users = msg[1:-1].split(',')
    # print(users)
    user={
        'uid':users[0],
        'name': users[1],
        'time': users[2],
        'log_in': users[3],
        'log_back': users[4],
        'isActive': users[5]+','+users[6],
    }
    return render(request, "cwa/alter.html", locals())

# 修改信息
def alter_server(request):
    # 接收数据
    uid = request.POST.get('uid')
    time = request.POST.get('time')
    users = Attendance_status.objects.get(uid=uid, time=time)
    str = request.POST.get('select')
    msg = request.POST.get('msg')
    # print(users)
    # print(str,msg)
    # 修改信息
    users.isActive = str

    # 修改之前的信息 存入 Extras 表中
    data = users.isActive
    extras = Extras()
    extras.Modify_previous_information = data
    extras.message = msg
    extras.user_status = users
    try:
        users.save()
        extras.save()
        return HttpResponse(json.dumps('修改成功'))
    except:
        return HttpResponse(json.dumps('修改失败'))


# 查找用户所有异常考勤
def find_user_all(request):
    username = request.session.get('uname')
    users = Users.objects.get(username=username)
    employee = users.employee_set.all()
    # print(employee[0])
    user = Users.objects.get(id=employee[0].id)
    user_active = Attendance_status.objects.filter(uid=user.id).exclude(isActive='正常').order_by('-time')
    s = ''
    for user in user_active:
        s += "%s_%s_%s_%s_%s_%s|" % (user.uid, user.name, user.time, user.log_in, user.log_back, user.isActive)
    str = json.dumps(s[0:-1])
    # print(str)
    return HttpResponse(str)













