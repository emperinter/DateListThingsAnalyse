from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url(r'^index/$', views.IndexView.as_view(), name='index'),
    path('login/', views.post),
    url(r'^admin/', views.AdminView.as_view(), name='admin'),
]
