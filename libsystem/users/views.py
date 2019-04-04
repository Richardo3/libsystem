from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from django.views.generic import View


def index(request):
    """
    index 视图
    :param request: 包含了请求星系的请求对象
    :return: 响应对象
    """
    return redirect('/static/index.html')


def demo(request):
    print('view 视图被调用')
    return HttpResponse('ok')