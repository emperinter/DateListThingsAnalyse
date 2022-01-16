# coding=utf-8
import json

from django.http import HttpResponse
from rest_framework.views import APIView

import pyecharts.options as opts
from pyecharts.charts import WordCloud, Line


from . import models

date_list = ["2022/01/06","2022/01/07","2022/01/08"] #时间
process = [3,4,4]
emotion = [4,4,8]
energy = [5,3,4]

key_dict = {"You Should Add Some KeyWords !":"1"} # 用于统计数据
key = [] # 关键字，用于制作词云图

def get_things_date():
    things_date = models.Things_Date.all()
    for m in things_date:
        date_list.append(m)

def get_state():
    # state_p = models.Processing.objects.values("process").first()
    # state_e  = models.Processing.objects.filter("emotion").first()
    # state_en = models.Processing.objects.filter("energy").first()
    # state_key = models.Processing.objects.filter("key").first()
    # for s in state_p:
    #     process.append(s)
    # for s_e in state_e:
    #     emotion.append(s_e)
    # for s_en in state_en:
    #     energy.append(s_en)
    # for k in state_key:
    #     key.append(k)
    global key
    key.clear()
    for get_dict_key in key_dict:
        print(get_dict_key,key_dict[get_dict_key])
        key.append((get_dict_key,key_dict[get_dict_key]))




def line_base() -> Line:
    get_state()
    l = (
        Line()
            .add_xaxis(date_list)
            .add_yaxis("process",process,color='red')
            .add_yaxis("emotion", emotion,color='blue')
            .add_yaxis("energy",energy,color='green')
            # .set_global_opts(title_opts=opts.TitleOpts(title="DateListThingsAnalyse"))
    ).dump_options_with_quotes()
    return l

def word_base() -> WordCloud:
    get_state()
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


class LineView(APIView):
    def get(self, request, *args, **kwargs):
        return JsonResponse(json.loads(line_base()))

class WordView(APIView):
    def get(self, request, *args, **kwargs):
        return JsonResponse(json.loads(word_base()))

class IndexView(APIView):
    def get(self, request, *args, **kwargs):
        return HttpResponse(content=open("./front/templates/index.html", encoding='utf-8').read())
