from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    print('第一个函数')
    return HttpResponse('第一个函数')


def login(request):
    print('第二个函数')
    return HttpResponse('第二个函数')