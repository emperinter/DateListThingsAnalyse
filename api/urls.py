from django.conf.urls import url
from django.urls import path, include
from rest_framework.documentation import include_docs_urls

from . import self_router

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(self_router.router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^docs/', include_docs_urls(title='DateListThingsAPI DOCS')),   # 参数为title为接口文档网站的标题
]