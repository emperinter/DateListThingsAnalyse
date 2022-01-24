# coding=utf-8
import time
import json

from django.http import HttpResponse
from rest_framework.views import APIView
from django.shortcuts import render

import pyecharts.options as opts
from pyecharts.charts import WordCloud, Line
import _thread

from . import models

date_list = ["2022/01/06","2022/01/07","2022/01/08"] #默认时间设计
process = [3,4,4]
emotion = [4,4,8]
energy = [5,3,4]

key_dict = {} # 用于统计数据
key = [] # 关键字，用于制作词云图

userid = ""

# choose
# 1 -> Line Charts Data
# 2 -> Word Charts Data
def get_data(choose):
    global userid

    getkey = []
    global process
    global emotion
    global energy
    global date_list
    global key

    print("\n################"+str( time.ctime(time.time()))+"################\n")
    things = models.ListThings.objects.filter(userid=userid).order_by('date')
    #有数据的的情况下获取数据，没有则是默认数据
    if(things):
        if(choose == 1):
            print("\n折线统计图！")
            process.clear()
            emotion.clear()
            date_list.clear()
            energy.clear()
            for t in things:
                date_list.append(t.date)
                process.append(t.process)
                emotion.append(t.emotion)
                energy.append(t.energy)
                print("\ndate: "+str(t.date)+"\tprocess: "+str(t.process)+"\temotion: "+str(t.process)+"\tenergy: "+str(t.energy))
        elif(choose == 2):
            print("词云图！")
            getkey.clear()
            key.clear()
            key_dict.clear()
            for t in things:
                getkey.append(t.key)
            print(getkey)
            for m in getkey:
                if m in key_dict:
                    key_dict[m] += 1
                else:
                    key_dict[m] = 1

            for get_dict_key in key_dict:
                key.append((get_dict_key,key_dict[get_dict_key]))



def line_base() -> Line:
    _thread.start_new_thread(get_data,(1,))
    l = (
        Line()
            .add_xaxis(date_list)
            .add_yaxis("process",process,color='red')
            .add_yaxis("emotion", emotion,color='blue')
            .add_yaxis("energy",energy,color='green')
    ).dump_options_with_quotes()
    return l

def word_base() -> WordCloud:
    _thread.start_new_thread(get_data,(2,))
    w = (
        WordCloud()
            .add(series_name="热点分析", data_pair=key, word_size_range=[18, 88])
            .set_global_opts(
            title_opts=opts.TitleOpts(
                title_textstyle_opts=opts.TextStyleOpts(font_size=64)
            ),
            tooltip_opts=opts.TooltipOpts(is_show=True),
        )
            .dump_options_with_quotes()
    )
    return w


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


class LineView(APIView):
    def get(self, request, *args, **kwargs):
        return JsonResponse(json.loads(line_base()))

class WordView(APIView):
    def get(self, request, *args, **kwargs):
        return JsonResponse(json.loads(word_base()))

class IndexView(APIView):
    def get(self, request, *args, **kwargs):
        return HttpResponse(content=open("./front/templates/index.html", encoding='utf-8').read())

def NotFound(request,information):
    return render(request,"./404.html", {'information':information})

# 接口函数
def post(request):
    if request.method == 'POST':  # 当提交表单时
        # 判断是否传参
        if request.POST:
            global userid
            userid = request.POST.get('userid', 0)
            username = request.POST.get('username', 0)
            passwd = request.POST.get('passwd', 0)
            # 判断参数中是否含有username和passwd
            if username and passwd:
                print(str(userid) + str(username) + str(passwd))
                return render(request, "./index.html", {'userid': userid, 'username': username, "passwd": passwd})
            else:
                return render(request, "./index.html", {'userid': userid, 'username': username, "passwd": passwd})
        else:
            return render(request, "./404.html", {'information': "输入为空!"})
    else:
        return render(request, "./404.html", {'information': "方法错误!"})
