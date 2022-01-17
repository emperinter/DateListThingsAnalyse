#coding=utf-8
import json

from django.http import HttpResponse
from django.shortcuts import render, reverse, redirect
from rest_framework.views import APIView
from pyecharts.components import Table
from pyecharts.options import ComponentTitleOpts
from . import models

class IndexView(APIView):
    def get(self, request, *args, **kwargs):
        return HttpResponse(content=open("./background/templates/index.html", encoding='utf-8').read())

class AdminView(APIView):
    def get(self, request, *args, **kwargs):
        return HttpResponse(content=open("./background/templates/admin.html", encoding='utf-8').read())


# def TableBase() -> Table:
#     headers = ["City name", "Area", "Population", "Annual Rainfall"]
#     rows = [
#         ["Brisbane", 5905, 1857594, 1146.4],
#         ["Adelaide", 1295, 1158259, 600.5],
#         ["Darwin", 112, 120900, 1714.7],
#         ["Hobart", 1357, 205556, 619.5],
#         ["Sydney", 2058, 4336374, 1214.8],
#         ["Melbourne", 1566, 3806092, 646.9],
#         ["Perth", 5386, 1554769, 869.4],
#     ]
#
#     t = (
#         Table()
#             .add(headers, rows)
#             .set_global_opts(
#             title_opts=ComponentTitleOpts(title="Table-基本示例", subtitle="我是副标题支持换行哦")
#             )
#         )
#     print(json.loads(str(t)))
#     return json.loads(str(t))


# class TableView(APIView):
#     def get(self, request, *args, **kwargs):
#         return JsonResponse(json.loads(TableBase()))

# def user_list(request):
#     return render(request, './admin.html', {'users': users})


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

def admin(request,username,passwd,table):
    print("跳转到admin")
    users = models.User.objects.all()  #将User表中的所有对象赋值给users这个变量，它是一个列表
    print(users)
    return render(request,"./admin.html", {'users':users, 'username': username, "passwd":passwd})

# 接口函数
def post(request):
    if request.method == 'POST':  # 当提交表单时
        dic = {}
        # 判断是否传参
        if request.POST:
            user = request.POST.get('email', 0)
            passwd = request.POST.get('passwd', 0)
            date = request.POST.get('date', 0)
            process = request.POST.get('Process', 0)
            emption = request.POST.get('Emotion', 0)
            energy = request.POST.get('Energy', 0)
            key = request.POST.get('KeyWords', 0)
            print(str(date)+"\t"+ str(process) +"\t"+str(emption)+"\t"+str(energy)+"\t"+str(key))

            # 判断参数中是否含有a和b
            if  user and passwd:
                if(search_user(user,passwd)):
                    print("该用户已存在" + str(user))
                    dic['number'] = "该用户已存在"
                    admin(request,user,passwd,"<li>TESt<li>")
                else:
                    print("该用户不存在,准备创建!")
                    dic['number'] = "该用户不存在,准备创建!"
                    creat_user(user,passwd)
                users = models.User.objects.all()  # 将User表中的所有对象赋值给users这个变量，它是一个列表
                return render(request, "./admin.html", {'user': user, "passwd": passwd,'users':users})
            else:
                # print("输入错误")
                return render(request, "./admin.html", {'user': "", "passwd": ""})
        else:
            # print("输入为空")
            return render(request, "./admin.html", {'user': "", "passwd": ""})
    else:
        # return HttpResponse('方法错误')
        return render(request, "./admin.html", {'user': "", "passwd": ""})


# Create your views here.
def response_as_json(data):
    json_str = json.dumps(data)
    response = HttpResponse(
        json_str,
        content_type="application/json",
    )
    response["Access-Control-Allow-Origin"] = "*"
    return response


def json_response(data, code=200):
    data = {
        "code": code,
        "msg": "success",
        "data": data,
    }
    return response_as_json(data)


def json_error(error_string="error", code=500, **kwargs):
    data = {
        "code": code,
        "msg": error_string,
        "data": {}
    }
    data.update(kwargs)
    return response_as_json(data)


JsonResponse = json_response
JsonError = json_error