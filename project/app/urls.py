from django.urls import path
from .views import *

urlpatterns = [
    path('',Home,name='index'),
    path('register/',Registration,name='register'),
    path('show/',ShowData,name='show'),
    path('edit/<pk>',EditData,name='edit'),
    path('update/<pk>',UpdateData,name='update'),
]