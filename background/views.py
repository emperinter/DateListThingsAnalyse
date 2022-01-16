#coding=utf-8
import json

from django.http import HttpResponse
from rest_framework.views import APIView



class IndexView(APIView):
    def get(self, request, *args, **kwargs):
        return HttpResponse(content=open("./background/templates/index.html", encoding='utf-8').read())

# 定义功能
def add_args(a, b):
    return a+b


# 定义功能
def add_args(a, b):
    return a + b


# 接口函数
def post(request):
    if request.method == 'POST':  # 当提交表单时
        dic = {}
        # 判断是否传参
        if request.POST:
            a = request.POST.get('email', 0)
            b = request.POST.get('passwd', 0)
            # 判断参数中是否含有a和b
            if a and b:
                res = add_args(a, b)
                dic['number'] = res
                dic = json.dumps(dic)
                return HttpResponse(dic)
            else:
                return HttpResponse('输入错误')
        else:
            return HttpResponse('输入为空')

    else:
        return HttpResponse('方法错误')


