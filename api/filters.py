import django_filters
from background.models import User,ListThings

class UserFilter(django_filters.rest_framework.FilterSet):
    """
    用户的过滤类
    """

    # 大于这个值 name指定字段 lookup_expr过滤条件
    # NumberFilter 数字类型
    # price_min = django_filters.NumberFilter(name="shop_price", lookup_expr="gte")
    # # 小于这个值
    # price_max = django_filters.NumberFilter(name="shop_price", lookup_expr="lte")

    # name模糊查询, 不指定过滤条件, 必须全部匹配
    # CharFilter字符串类型
    # name = django_filters.CharFilter(name="name", lookup_expr="icontains")

    class Meta:
        # 指定模型类
        model = User
        # 显示这个字段
        fields = ["user_name"]


class ThingsFilter(django_filters.rest_framework.FilterSet):
    """
    用户的过滤类
    """

    # 大于这个值 name指定字段 lookup_expr过滤条件
    # NumberFilter 数字类型
    # price_min = django_filters.NumberFilter(name="shop_price", lookup_expr="gte")
    # # 小于这个值
    # price_max = django_filters.NumberFilter(name="shop_price", lookup_expr="lte")

    # name模糊查询, 不指定过滤条件, 必须全部匹配
    # CharFilter字符串类型
    # name = django_filters.CharFilter(name="name", lookup_expr="icontains")

    class Meta:
        # 指定模型类
        model = ListThings
        # 显示这个字段
        fields = ['userid', 'date', 'process', 'emotion', 'energy', 'key']
