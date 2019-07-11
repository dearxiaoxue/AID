from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader

def login(request):
    return redirect('/login/')
