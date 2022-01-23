from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [
    # url(r'^index/$', views.IndexView.as_view(), name='front'),
    url(r'^index/$', views.post, name='front'),
    url(r'^word/$', views.WordView.as_view(), name='front'),
    url(r'^line/$', views.LineView.as_view(), name='front'),
    path('404/', views.NotFound),
]