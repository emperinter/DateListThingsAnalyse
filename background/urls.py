from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url(r'^index/$', views.IndexView.as_view(), name='index'),
    path('admin/', views.admin),
    path('auth/', views.auth),
    path('upload_file/', views.upload_file),
    path('404/', views.NotFound),
    path('del_data/', views.del_data),
    path('del_account/', views.del_account),
    path('get_files/', views.get_files),
]
