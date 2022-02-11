from django.http import HttpResponse
from django_filters.rest_framework import DjangoFilterBackend

from background.models import ListThings,User
from rest_framework import serializers, viewsets, filters, mixins

from .filters import ThingsFilter
# Create your views here.

# Serializers define the API representation.
class ThingsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ListThings
        fields = ['things_id','date', 'process', 'emotion', 'energy', 'key']

# ViewSets define the view behavior.
class ThingsViewSet(viewsets.ModelViewSet):
    queryset = ListThings.objects.all()
    serializer_class = ThingsSerializer

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        # 显示的字段
        # 返回的JSON字段
        fields = ['user_id']

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserListView(mixins.ListModelMixin, viewsets.GenericViewSet):
    # 指定序列化类
    serializer_class = UserSerializer

    # 重写get_queryset
    def get_queryset(self):
        user_name = self.request.query_params.get("user_name",None)
        user_passwd = self.request.query_params.get("user_passwd",None)

        if (user_name is not None) and (user_passwd is not None):
            query_set = User.objects.filter(user_name=user_name,user_passwd=user_passwd)
            return query_set


class ThingsListView(mixins.ListModelMixin, viewsets.GenericViewSet):
    # 指定queryset
    queryset = ListThings.objects.all()

    # 指定序列化类
    serializer_class = ThingsSerializer

    # 添加过滤器 这里可以吧django-filter过滤器添加进来 和 rest_framework的filters添加进来一起用, 也可以单个用, 看你的需求
    filter_backends = [DjangoFilterBackend]

    # 只需要简单的基于等同的过滤，则可以filter_fields在视图或视图集上设置属性，列出要过滤的字段集。
    # 等同就是根据你过滤的字段的数据必须跟数据库里那个字段的数据相同
    # filter_fields = ['userid']

    # 指定过滤器类
    filter_class = ThingsFilter

    # 模糊搜索的字段
    # search_fields = ['userid']