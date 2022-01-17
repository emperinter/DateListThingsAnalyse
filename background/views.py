#coding=utf-8
import json

from django.http import HttpResponse
from django.shortcuts import render, reverse, redirect
from rest_framework.views import APIView
from . import models

class IndexView(APIView):
    def get(self, request, *args, **kwargs):
        return HttpResponse(content=open("./background/templates/index.html", encoding='utf-8').read())


class AdminView(APIView):
    def get(self, request, *args, **kwargs):
        return HttpResponse(content=open("./background/templates/admin.html", encoding='utf-8').read())


def creat_user(username,passwd):
    user = models.User(user_name = username,user_passwd = passwd)
    try:
        user.save()
    except:
        # return render("./admin.html", {'user': "", "passwd": ""})
        print("SomeThing Woring !")


def search_user(username,passwd):
    user = models.User.objects.filter(user_name = username,user_passwd = passwd)
    print("用户" + str(user))
    if(user):
        return True
    else:
        print("该用户不存在,准备创建")
        return False

def admin(request,username,passwd):
    print("跳转到admin")
    return render(request,"./admin.html", {'user': username,"passwd":passwd})

# 接口函数
def post(request):
    if request.method == 'POST':  # 当提交表单时
        dic = {}
        # 判断是否传参
        if request.POST:
            user = request.POST.get('email', 0)
            passwd = request.POST.get('passwd', 0)
            # 判断参数中是否含有a和b
            if  user and passwd:
                if(search_user(user,passwd)):
                    print("该用户已存在" + str(user))
                    dic['number'] = "该用户已存在"
                    admin(request,user,passwd)
                else:
                    print("该用户不存在,准备创建!")
                    dic['number'] = "该用户不存在,准备创建!"
                    creat_user(user,passwd)
                return render(request, "./admin.html", {'user': user, "passwd": passwd})
            else:
                # print("输入错误")
                return render(request, "./admin.html", {'user': "", "passwd": ""})
        else:
            # print("输入为空")
            return render(request, "./admin.html", {'user': "", "passwd": ""})
    else:
        # return HttpResponse('方法错误')
        return render(request, "./admin.html", {'user': "", "passwd": ""})


