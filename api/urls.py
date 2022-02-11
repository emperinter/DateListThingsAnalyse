from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers
from . import views
from rest_framework.documentation import include_docs_urls

# Routers provide an easy way of automatically determining the URL conf.
# 用于设置数据获取地址
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'things', views.ThingsViewSet)
router.register(r'get-user', views.UserListView,basename='get-user')
router.register(r'get-things', views.ThingsListView,basename='get-things')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^docs/', include_docs_urls(title='DateListThingsAPI DOCS')),   # 参数为title为接口文档网站的标题
]