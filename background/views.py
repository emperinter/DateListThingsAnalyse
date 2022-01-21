import json
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from django.conf import settings
from . import models
import  os

class IndexView(APIView):
    def get(self, request, *args, **kwargs):
        return HttpResponse(content=open("./background/templates/index.html", encoding='utf-8').read())

class AdminView(APIView):
    def get(self, request, *args, **kwargs):
        username = request.POST.get('username', 0)
        passwd = request.POST.get('passwd', 0)
        if passwd and username:
            return HttpResponse(content=open("./background/templates/admin.html", encoding='utf-8').read())
        else:
            return HttpResponse(content=open("./background/templates/index.html", encoding='utf-8').read())


def creat_user(username,passwd):
    user = models.User(user_name = username,user_passwd = passwd)
    try:
        user.save()
        return(search_user(username,passwd))
    except:
        print("SomeThing Woring !")


def search_user(username,passwd):
    user = models.User.objects.filter(user_name = username,user_passwd = passwd)
    if(user):
        print("用户" + str(user) +"\tuserid:" + str(user[0].user_id))
        return int(user[0].user_id)
    else:
        print("该用户不存在,准备创建")
        return False

def admin(request,userid,username,passwd):
    print("跳转到admin")
    users = models.User.objects.filter(user_id = userid,user_name = username,user_passwd=passwd)  #将User表中的所有对象赋值给users这个变量，它是一个列表
    print("用户"+str(users))
    things = models.ListThings.objects.filter(userid = userid)
    print(things)
    return render(request,"./admin.html", {'things':things,'users':users,'userid':userid, 'username': username, "passwd":passwd})



# 接口函数
def post(request):
    if request.method == 'POST':  # 当提交表单时
        # 判断是否传参
        if request.POST:
            userid = request.POST.get('userid', 0)
            username = request.POST.get('username', 0)
            passwd = request.POST.get('passwd', 0)
            date = request.POST.get('date', 0)
            process = request.POST.get('Process', 0)
            emotion = request.POST.get('Emotion', 0)
            energy = request.POST.get('Energy', 0)
            key = request.POST.get('KeyWords', 0)
            print("userid"+str(userid)+"\tusername"+str(username)+"\t"+str(date)+"\t"+ str(process) +"\t"+str(emotion)+"\t"+str(energy)+"\t"+str(key))

            if(date):
                # 使用request.FILES['myfile']获得文件流对象file
                file = request.FILES['myfile']
                if(file):
                    print("file:\t"+str(file))
                    # 文件储存路径，应用settings中的配置，file.name获取文件名
                    filename = os.path.join(settings.MEDIA_ROOT, file.name)
                    print("filename:\t"+str(filename))
                    # 写文件
                    with open(filename, 'wb+') as f:
                        # file.file 获取文件字节流数据
                        # data = file.file.read()
                        # f.write(data)

                        #file.chunks()，而不是直接使用read()方法
                        #能确保大文件不会占用系统过多的内存。
                        for chunk in file.chunks():
                            f.write(chunk)
                        print("文件存储成功！")

            # 判断参数中是否含有a和b
            if username and passwd:
                if(search_user(username,passwd)):
                    print("该用户已存在" + str(username))
                    userid = search_user(username,passwd)

                    if(process):
                        date_things = models.ListThings.objects.filter(userid = userid,date = date)
                        # 一天只能有一个状态，如果已有则是修改数据
                        if(date_things):
                            date_things.update(userid=userid,date=date,process=process,emotion=emotion,energy=energy,key=key)
                        else:
                            things = models.ListThings(userid=userid,date=date,process=process,emotion=emotion,energy=energy,key=key)
                            things.save()
                    admin(request,userid,username,passwd)
                else:
                    print("该用户不存在,准备创建!")
                    userid = creat_user(username,passwd)
                users = models.User.objects.filter(user_id=userid, user_name=username,user_passwd=passwd)  # 将User表中的所有对象赋值给users这个变量，它是一个列表
                things = models.ListThings.objects.filter(userid = userid).order_by('date')
                return render(request, "./admin.html",{'things': things, 'users': users, 'userid': userid, 'username': username,"passwd": passwd})
            else:
                print("输入错误")
                # return render(request, "./admin.html", {'user': "", "passwd": ""})
                return HttpResponse('输入错误')
        else:
            # return render(request, "./admin.html", {'user': "", "passwd": ""})
            return HttpResponse('输入为空')
    else:
        return HttpResponse('方法错误')
        # return render(request, "./admin.html", {'user': "", "passwd": ""})



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