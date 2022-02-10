import json
from django.http import HttpResponse,StreamingHttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from django.conf import settings
from . import models
import  os
import pandas as pd

class IndexView(APIView):
    def get(self, request, *args, **kwargs):
        return HttpResponse(content=open("./background/templates/index.html", encoding='utf-8').read())

def creat_user(username,passwd):
    user = models.User(user_name = username,user_passwd = passwd)
    try:
        user.save()
        return(search_user(username,passwd))
    except Exception as e:
        print("SomeThing Woring !")
        print("ERROR:\t" , e)


def search_user(username,passwd):
    user = models.User.objects.filter(user_name = username,user_passwd = passwd)
    if(user):
        print("用户" + str(user) +"\tuserid:" + str(user[0].user_id))
        return int(user[0].user_id)
    else:
        print("该用户不存在,准备创建")
        return False

def NotFound(request,information):
    return render(request,"./404.html", {'information':information})

def inserDb(userid,date,process,emotion,energy,key):
    print(str(userid) + "\tinsertDb_Date|" + date + "|" + "\t" + str(process) + "\t" + str(emotion) + "\t" + str(energy) + "\t" + str(key))
    get_userid = models.User.objects.get(user_id=userid)
    date_things = models.ListThings.objects.filter(userid=get_userid, date=date)
    # 一天只能有一个状态，如果已有则是修改数据
    if (date_things):
        print("update")
        date_things.update(userid=get_userid, date=date, process=process, emotion=emotion, energy=energy, key=key)
    else:
        print("insert|"+str(date))
        things = models.ListThings(userid=get_userid, date=date, process=process, emotion=emotion, energy=energy, key=key)
        things.save()

def upload_file(file):
    print("file:\t" + str(file))
    # 文件储存路径，应用settings中的配置，file.name获取文件名
    filename = os.path.join(settings.MEDIA_ROOT, file.name)
    print("filename:\t" + str(filename))
    # 写文件
    with open(filename, 'wb+') as f:
        # file.file 获取文件字节流数据
        # data = file.file.read()
        # f.write(data)
        # file.chunks()，而不是直接使用read()方法
        # 能确保大文件不会占用系统过多的内存。
        for chunk in file.chunks():
            f.write(chunk)
        print("文件存储成功！")

def del_data(request):
    if request.method == 'POST':  # 当提交表单时
        # 判断是否传参
        if request.POST:
            userid = request.POST.get('userid', 0)
            username = request.POST.get('username', 0)
            passwd = request.POST.get('passwd', 0)
            users = models.User.objects.filter(user_id=userid, user_name=username,user_passwd=passwd)  # 将User表中的所有对象赋值给users这个变量，它是一个列表
            things = models.ListThings.objects.filter(userid=userid)
            things.delete()
            return render(request, "./admin.html",
                          {'things': things, 'users': users, 'userid': userid, 'username': username, "passwd": passwd})


def del_account(request):
    if request.method == 'POST':  # 当提交表单时
        # 判断是否传参
        if request.POST:
            userid = request.POST.get('userid', 0)
            users = models.User.objects.filter(user_id=userid)
            print("删除用户：\t" + str(userid) + str(users))
            users.delete()
        return HttpResponse(content=open("./background/templates/index.html", encoding='utf-8').read())


def file_to_database(file,userid):
    print("###########################处理文件入库##################################")
    filename = os.path.join(settings.MEDIA_ROOT, file.name)
    df=pd.read_excel(filename,engine='openpyxl',parse_dates=True)#这个会直接默认读取到这个Excel的第一个表单
    for row in df.index.values :
        doc = dict()
        doc['date'] = df.iloc[row, 0]
        doc['finished'] = df.iloc[row, 1]
        doc['emotion'] = df.iloc[row, 2]
        doc['energy'] = df.iloc[row, 3]
        doc['key'] = df.iloc[row, 4]
        print(type(str(doc['date'].date())))
        print(str(userid)+"|"+str(doc['date'].date()) + "\t" + str(doc['finished']) +  "\t" +   str(doc['emotion']) +  "\t" +  str(doc['energy']) + "\t" +  str(doc['key']) )
        if(str(doc['date'].date())  != 'NaT'):
            try:
                inserDb(userid,str(doc['date'].date()),int(doc['finished']),int(doc['emotion']),int(doc['energy']),doc['key'])
            except:
                print("someThing Woring !")
        print("----------------------------------------------------------------------")
    print("###########################处理文件入库完成##################################")


def file_iterator(file_name, chunk_size=512):
    with open(file_name) as f:
        while True:
            c = f.read(chunk_size)
            if c:
                yield c
            else:
                break
# 获取文件
def get_files(request):
    if request.method == 'POST':  # 当提交表单时
        # 判断是否传参
        if request.POST:
            the_file_name = "./static/files/get_file.csv"
            data = []
            userid = request.POST.get('userid', 0)
            things = models.ListThings.objects.filter(userid=userid)
            print(things)
            for m in things:
                data.append({"date":str(m.date),"process":str(m.process),"emotion":str(m.emotion),"energy":str(m.energy),"key":str(m.key)})
                df = pd.DataFrame(data,columns=["date","process","emotion","energy","key"])
                df.to_csv(the_file_name,index=False)
            response = StreamingHttpResponse(file_iterator(the_file_name))
            response['Content-Type'] = 'application/octet-stream'
            response['Content-Disposition'] = 'attachment;filename="output.csv"'
            return response

# 登录判断
def auth(request):
    if request.method == 'POST':  # 当提交表单时
        # 判断是否传参
        if request.POST:
            userid = request.POST.get('userid', 0)
            username = request.POST.get('username', 0)
            passwd = request.POST.get('passwd', 0)
            users = models.User.objects.filter(user_id=userid, user_name=username,user_passwd=passwd)  # 将User表中的所有对象赋值给users这个变量，它是一个列表
            things = models.ListThings.objects.filter(userid=userid).order_by('date')

            # 判断参数中是否含有a和b
            if username and passwd:
                userid = search_user(username, passwd)
                if(userid):
                    print("该用户已存在!!!" + str(username))
                    users = models.User.objects.filter(user_id=userid, user_name=username,
                                                       user_passwd=passwd)  # 将User表中的所有对象赋值给users这个变量，它是一个列表
                    things = models.ListThings.objects.filter(userid=userid).order_by('date')
                    print(things)
                    return render(request, "./admin.html",
                                  {'things': things, 'users': users, 'userid': userid, 'username': username,
                                   "passwd": passwd})
                else:
                    print("该用户不存在,准备创建!")
                    userid = creat_user(username,passwd)
                    return render(request, "./admin.html",{'things': things, 'users': users, 'userid': userid, 'username': username,"passwd": passwd})
            elif username and passwd:
                return render(request, "./admin.html",{'things': things, 'users': users, 'userid': userid, 'username': username,"passwd": passwd})
            else:
                print("输入错误")

                return render(request, "./404.html", {'information': "输入错误!"})
        else:
            return render(request, "./404.html", {'information': "输入为空!"})
    else:
        return render(request, "./404.html", {'information': "方法错误!"})

# 接口函数
def admin(request):
    print("\n\n\nadmin")
    if request.method == 'POST':  # 当提交表单时
        # 判断是否传参
        if request.POST:
            userid = request.POST.get('userid', 0)
            username = request.POST.get('username', 0)
            passwd = request.POST.get('passwd', 0)
            date = request.POST.get('date',0)
            process = request.POST.get('Process', 0)
            emotion = request.POST.get('Emotion', 0)
            energy = request.POST.get('Energy', 0)
            key = request.POST.get('KeyWords', 0)
            print("userid"+str(userid)+"\tusername"+str(username)+"\tdate:"+str(date)+"\t"+ str(process) +"\t"+str(emotion)+"\t"+str(energy)+"\t"+str(key))
            users = models.User.objects.filter(user_id=userid, user_name=username,
                                               user_passwd=passwd)  # 将User表中的所有对象赋值给users这个变量，它是一个列表

            print("处理文件！")
            try:
                file = request.FILES['myfile']
                print("file" + str(file))
                upload_file(file)
                file_to_database(file,userid)
                file_tag = 1
            except:
                file_tag = 0
                print("文件处理异常！")


            print(file_tag)

            if file_tag == 0:
                inserDb(userid,date,process,emotion,energy,key)
                things = models.ListThings.objects.filter(userid=userid).order_by('date')
                print(things)
                return render(request, "./admin.html",{'things': things, 'users': users, 'userid': userid, 'username': username,"passwd": passwd})
            elif file_tag == 1:
                things = models.ListThings.objects.filter(userid=userid).order_by('date')
                return render(request, "./admin.html",{'things': things, 'users': users, 'userid': userid, 'username': username,"passwd": passwd})
            else:
                return render(request, "./404.html", {'information': "输入错误!"})
        else:
            return render(request, "./404.html", {'information': "输入为空!"})
    else:
        return render(request, "./404.html", {'information': "方法错误!"})


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