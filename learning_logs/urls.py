
# 定义learning_logs的urls

from django.urls import path

from . import views

urlpatterns = [

    # 主页
    path('',views.index,name='index'),

    # 显示所有主题
    path('topics/',views.topics,name='topics'),

    #添加新条目
    path('add_new_entry/(?P<topic_id>\d+)/', views.add_new_entry, name='add_new_entry'),

    #编辑条目
    path('edit_entry/(?P<entry_id>\d+)/', views.edit_entry, name='edit_entry'),
    # 各个主题
    path('topics/(?P<topic_id>\d+)/', views.topic, name='topic'),

    #添加新主题
    path('add_new_topic',views.add_new_topic,name = 'add_new_topic'),

]
