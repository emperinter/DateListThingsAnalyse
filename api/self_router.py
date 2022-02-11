from rest_framework import routers
from . import views

# 用于设置数据获取地址
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'things', views.ThingsViewSet)
router.register(r'user/query', views.UserListView,basename='get-user')
router.register(r'thing/query', views.ThingsListView,basename='get-things')