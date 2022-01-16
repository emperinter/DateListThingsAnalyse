from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url(r'^index/$', views.IndexView.as_view(), name='backgorund'),
    path('login/', views.post),
]
