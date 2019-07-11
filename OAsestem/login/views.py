from django.shortcuts import render
from . import models
from employees.models import Employee
# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Users

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        name = request.POST.get('userName')
        password = request.POST.get('password')
        users = Users.objects.all()
        for i in users:
            if i.username == name:
                if str(i.password) == password:
                    print(i.username)
                    username = Users.objects.get(username=name)
                    user_name= name
                    request.session['uname']=name
                    print(request.session['uname'])
                    return render(request, 'system.html', locals())
        else:
            a = '账户名密码错误'
            return render(request, 'login.html', locals())


def staff(request):
    user = Users.objects.all()
    user_name=request.session['uname']
    return render(request, 'staff.html', locals())


def staff_add(request):
    if request.method == 'GET':
        return render(request, 'add_user.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        intro = request.POST.get('intro')
        Users.objects.create(username=username, password=password, intro=intro)
        user = Users.objects.all()
        user_name = request.session['uname']
        return render(request, 'staff.html', locals())


def search(request):
    search = request.POST.get('search')
    user = Users.objects.all()
    for x in user:
        if x.username == search:
            user = Users.objects.filter(username=search).all()
        elif x.id == search:
            user = Users.objects.filter(id=search).all()
        elif x.intro == search:
            user = Users.objects.filter(intro=search).all()
    user_name = request.session['uname']
    return render(request, 'staff.html', locals())


def staff_delete(request, id=0):
    user = models.Users.objects.get(id=id)
    user.delete()
    user = models.Users.objects.all()
    user_name = request.session['uname']
    return render(request, 'staff.html', locals())


def update(request, id=1):
    if request.method == 'GET':
        user_list = models.Users.objects.filter(id=id).first()
        return render(request, 'update_user.html', locals())
    elif request.method == 'POST':
        uid = request.POST.get('id')
        username = request.POST.get('uname')
        password = request.POST.get('password')
        intro = request.POST.get('intro')
        user_obj = Users.objects.filter(id=uid).first()
        user_obj.username = username
        user_obj.password = password
        user_obj.intro = intro
        user_obj.save()
        user = Users.objects.all()
        user_name = request.session['uname']
        return render(request, 'staff.html', locals())
