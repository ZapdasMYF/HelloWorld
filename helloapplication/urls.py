from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('data', views.data, name='data'),
    path('post', views.post, name='post'),
]

