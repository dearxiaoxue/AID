from django.shortcuts import render
from . import models
from login.models import Users
# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader


def employee(request):
    employee_list = models.Employee.objects.all()
    user_name = request.session['uname']
    return render(request, 'employee.html', locals())


def add_employee(request):
    if request.method == 'GET':
        return render(request, 'add_employee.html')
    elif request.method == 'POST':
        try:
            em_name = request.POST.get('em_name')
            em_age = request.POST.get('em_age')
            em_born = request.POST.get('em_born')
            gender = request.POST.get('gender')
            level = request.POST.get('level')
            departmen = request.POST.get('department')
            school = request.POST.get('school')
            email_id = request.POST.get('email_id')
            email_pword = request.POST.get('email_pword')
            username = request.POST.get('username')
            username = Users.objects.get(username=username)
        except Exception as s:
            print(s)
            return HttpResponse('信息不完整')
        try:
            models.Employee.objects.create(
                em_name=em_name,
                em_age=em_age,
                em_born=em_born,
                gender=gender,
                level=level,
                department=departmen,
                school=school,
                email_id=email_id,
                email_pword=email_pword,
                username=username,
            )
            employee_list = models.Employee.objects.all()
            user_name = request.session['uname']
            return render(request, 'employee.html', locals())
        except Exception as e:
            print(e)
            return '创建失败'


def delete_employee(request, id):
    employee = models.Employee.objects.get(id=id)
    employee.delete()
    employee_list = models.Employee.objects.all()
    user_name = request.session['uname']
    return render(request, 'employee.html', locals())


def update(request, id=0):
    if request.method == 'GET':
        employee_list = models.Employee.objects.filter(id=id).first()
        return render(request, 'update_employee.html', locals())
    elif request.method == 'POST':
        id = request.POST.get('id')
        em_name = request.POST.get('em_name')
        em_age = request.POST.get('em_age')
        em_born = request.POST.get('em_born')
        gender = request.POST.get('gender')
        level = request.POST.get('level')
        department = request.POST.get('department')
        school = request.POST.get('school')
        email_id = request.POST.get('email_id')
        email_pword = request.POST.get('email_pword')
        employee_obj = models.Employee.objects.filter(id=id).first()
        employee_obj.em_name= em_name
        employee_obj.age = em_age
        employee_obj.em_born = em_born
        employee_obj.gender = gender
        employee_obj.level = level
        employee_obj.department = department
        employee_obj.school = school
        employee_obj.email_id = email_id
        employee_obj.email_pword = email_pword
        employee_obj.save()
        employee_list = models.Employee.objects.all()
        user_name = request.session['uname']
        return render(request, 'employee.html', locals())


def search(request):
    search = request.POST.get('search')
    employee_list = models.Employee.objects.all()
    print(search,type(search))
    for x in employee_list:
        print(x.id,type(x.id))
        if x.em_name == search:
            employee_list = models.Employee.objects.filter(em_name=search).all()
        elif x.department == search:
            employee_list = models.Employee.objects.filter(department=search).all()
        elif x.username == search:
            employee_list = models.Employee.objects.filter(username=search).all()
        elif str(x.id) == search:
            search=int(search)
            employee_list = models.Employee.objects.filter(id=search).all()
        # return render(request, 'employee.html', locals())
    user_name = request.session['uname']
    return render(request, 'employee.html', locals())

