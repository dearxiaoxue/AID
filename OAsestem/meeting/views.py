import math

from django.core.paginator import Paginator
from pandas import json
from django.shortcuts import render
from .forms import *
from .models import *
from django.http import HttpResponse
from . import models
from employees import models
import time


# Create your views here.

# 参会人员信息确认
def isname(list_meattendee):
    list_meattendeeFailure=[]
    list_meattendeenew = list_meattendee.split(";")
    for meattendee in list_meattendeenew:
        obj = models.Employee.objects.filter(em_name=meattendee)
        if obj:
            continue
        else:
            list_meattendeeFailure.append(meattendee)
    return list_meattendeeFailure

# 首页
def index(request):
    user_name = request.session['uname']
    return render(request, 'meeting/oa_main.html', locals())
    # return render(request, 'meeting/sys_main.html', locals())


# 新建会议
def newmeet(request):
    if request.method == 'GET':
        form = NewMeetForm()
        user_name = request.session['uname']
        return render(request, 'meeting/oa_newmeet.html', locals())
    else:
        form = NewMeetForm(request.POST)
        # print(form)
        # 校验
        if form.is_valid():
            timeArray = time.localtime(time.time())  # 时间元组
            mesystemTime01 = time.strftime("%Y%m%d%H%M%S", timeArray)
            mesystemTime02 = time.strftime("%Y/%m/%d-%H:%M:%S", timeArray)
            meid = str(mesystemTime01)  # 会议编号-->td+系统时间戳
            mesytime = str(mesystemTime02)  # 会议创建时间-->系统生成

            meinitiator = request.session['uname']  # 发起人

            data = form.cleaned_data
            data['meid'] = meid  # 增加会议编号
            data['mesytime'] = mesytime  # 增加会议发起时间
            data['meinitiator'] = meinitiator  # 增加会议发起人

            data['meattendee'] += ";" + meinitiator  # 参会人员增加发起人

            list_meattendeeFailure=isname(data['meattendee'])
            if list_meattendeeFailure:
                str_meattendee= ','.join(list_meattendeeFailure)+',这几人不是公司员工'
                a='发送失败'+str_meattendee
                print(a)
                return render(request, 'meeting/oa_newmeet.html', locals())
            else:
                # 返回字典格式的数据
                meet = Meeting(**data)
                try:
                    meet.save()
                    a = '会议提交成功'
                    # return HttpResponse('发送成功')
                    return render(request, 'meeting/oa_newmeet.html', locals())
                except Exception as e:
                    print('-----出错啦-------')
                    print(e)
                    a = '会议提交失败'
                    return render(request, 'meeting/oa_newmeet.html', locals())


# 查询会议
def selectmeet(request):
    if request.method == 'GET':
        user_name = request.session['uname']
        infomeets = Meeting.objects.filter(meinitiator__contains=user_name)
        count = infomeets.count()
        return render(request, 'meeting/oa_selectmeet.html', locals())
    else:
        user_name = request.session['uname']
        if request.POST['meid']:
            meid = request.POST['meid']
            infomeets = Meeting.objects.filter(meid=meid)
            count = infomeets.count()
            if infomeets:
                return render(request, 'meeting/oa_selectmeet.html', locals())
            else:
                return render(request, 'meeting/oa_selectmeetfail.html')
        elif request.POST['metopic']:
            metopic = request.POST['metopic']
            infomeets = Meeting.objects.filter(metopic__contains=metopic)
            count = infomeets.count()
            if infomeets:
                return render(request, 'meeting/oa_selectmeet.html', locals())
            else:
                return render(request, 'meeting/oa_selectmeetfail.html')
        elif request.POST['meinitiator']:
            meinitiator = request.POST['meinitiator']
            infomeets = Meeting.objects.filter(meinitiator__contains=meinitiator)
            count = infomeets.count()
            if infomeets:
                return render(request, 'meeting/oa_selectmeet.html', locals())
            else:
                return render(request, 'meeting/oa_selectmeetfail.html')
        elif request.POST['meattendee']:
            meattendee = request.POST['meattendee']
            infomeets = Meeting.objects.filter(meattendee__contains=meattendee)
            count = infomeets.count()
            if infomeets:
                return render(request, 'meeting/oa_selectmeet.html', locals())
            else:
                return render(request, 'meeting/oa_selectmeetfail.html')
        else:
            return render(request, 'meeting/oa_selectmeetfail.html')


# 会议提醒
def remindmeet(request,page):
    user_name = request.session['uname']
    infomeets = Meeting.objects.filter(meattendee__contains=user_name, statu='未开')
    if infomeets:
        count = infomeets.count()
        # 生成meet_list对象，定义每页显示3条记录
        paginator = Paginator(infomeets, 3)
        # 把当前的页码数转换为整数类型
        currentPage = int(page)
        # 上一页
        currentPagemin = currentPage - 1
        # 下一页
        currentPagemax = currentPage + 1
        print(currentPagemin, currentPagemax)
        if currentPagemin == 0:
            currentPagemin = 1
            meeting_list = paginator.page(currentPagemin)
        elif currentPagemax > (count // 3):
            if count%3==0:
                currentPagemax = count // 3
            else:
                currentPagemax = count // 3+1
            meeting_list = paginator.page(currentPagemax)
        else:
            meeting_list = paginator.page(page)  # 获取当前页码的记录
        return render(request, "meeting/oa_remindmeet.html", locals())
    else:
        return HttpResponse('暂无未开会议')


# 查询发起会议记录
def uploadmeet(request,page):
    user_name = request.session['uname']
    infomeets = Meeting.objects.filter(meinitiator=user_name)
    if infomeets:
        count = infomeets.count()
        # 生成meet_list对象，定义每页显示3条记录
        paginator = Paginator(infomeets, 3)
        # 把当前的页码数转换为整数类型
        currentPage = int(page)
        # 上一页
        currentPagemin = currentPage - 1
        # 下一页
        currentPagemax = currentPage + 1
        print(currentPagemin, currentPagemax)
        if currentPagemin == 0:
            currentPagemin = 1
            meeting_list = paginator.page(currentPagemin)
        elif currentPagemax > (count // 3):
            if count%3==0:
                currentPagemax = count // 3
            else:
                currentPagemax = count // 3+1
            meeting_list = paginator.page(currentPagemax)
        else:
            meeting_list = paginator.page(page)  # 获取当前页码的记录
        return render(request, "meeting/oa_uploadmeet.html", locals())
    else:
        return HttpResponse('暂无会议记录需要上传')


# 上传会议记录
def uploadmeet01(request, meid):
    if request.method == 'GET':
        user_name = request.session['uname']
        infomeets = Meeting.objects.get(meid=meid)
        if infomeets.statu == '已开':
            return HttpResponse('会议记录已上传')
        elif infomeets.statu=='未开':
            return render(request, 'meeting/oa_uploadmeet01.html', locals())
    else:
        infomeets = Meeting.objects.get(meid=meid)
        infomeets.metopic = request.POST['metopic']
        infomeets.meinitiator = request.POST['meinitiator']
        infomeets.content = request.POST['content']
        mepresent01 = request.POST['mepresent']
        menopresent01 = request.POST['menopresent']
        infomeets.statu = '已开'

        list_personFailure = isname(mepresent01+';'+menopresent01)
        if list_personFailure:
            str_meattendee = ','.join(list_personFailure) + '这几人不是公司员工'
            return HttpResponse('发送失败' +','+ str_meattendee)
        else:
            try:
                infomeets.save()
                return HttpResponse('上传成功')
            except Exception as e:
                print(e)
                return HttpResponse('上传失败')



# 修改会议记录
def updateinfo(request, meid):
    if request.method == 'GET':
        user_name = request.session['uname']
        infomeets = Meeting.objects.get(meid=meid)
        if infomeets.statu=='已开':
            return render(request, 'meeting/oa_updateinfo.html', locals())
        elif infomeets.statu=='未开':
            return HttpResponse('会议还未开始，不可修改')
    else:
        infomeets = Meeting.objects.get(meid=meid)
        infomeets.metopic = request.POST['mepresent']
        infomeets.meinitiator = request.POST['menopresent']
        infomeets.content = request.POST['content']
        print(infomeets)
        try:
            infomeets.save()
            return HttpResponse('修改成功')
        except Exception as e:
            print(e)
            return HttpResponse('修改失败')


# 删除会议记录
def delinfo(request, meid):
    if request.method == 'GET':
        infomeets = Meeting.objects.get(meid=meid)
        try:
            infomeets.delete()
            bb='删除成功'
            return HttpResponse('删除成功')
            # return render(request, 'meeting/oa_selectmeet.html', bb=bb)
        except Exception as e:
            print(e)
            bb = '删除失败'
            return HttpResponse('删除失败')
            # return render(request, 'meeting/oa_selectmeet.html', bb=bb)
