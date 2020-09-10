"""定义learning_log的URL模式"""
from django.urls import path, re_path
from . import views

app_name = 'learning_log'

urlpatterns = [
    # 主页
    path('', views.index, name='index'),
    path('topics/', views.topics, name='topics'),
    re_path(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    path('new_topic/', views.new_topic, name='new_topic'),
    re_path(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
]