from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    """
    index 视图
    :param request: 包含了请求星系的请求对象
    :return: 响应对象
    """
    return HttpResponse('hello world!')