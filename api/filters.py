import django_filters
from background.models import User,ListThings

# 目前这里没用到
# 用到的是重构后的方法
class UserFilter(django_filters.rest_framework.FilterSet):
    """
    用户的过滤类
    """
    user_name = django_filters.CharFilter(field_name="user_name",lookup_expr="exact")
    user_passwd = django_filters.CharFilter(lookup_expr="exact")

    class Meta:
        # 指定模型类
        model = User
        # 需要判断的条件
        # 查询条件中可以出现的字段
        fields = ["user_name","user_passwd"]


class ThingsFilter(django_filters.rest_framework.FilterSet):
    """
    事件的过滤类
    """
    class Meta:
        # 指定模型类
        model = ListThings
        # 显示这个字段
        fields = ['things_id', 'date', 'process', 'emotion', 'energy', 'key']
