
# 定义learning_logs的urls

from django.urls import path

from . import views

urlpatterns = [
    # 主页
    path('',views.index,name='index'),

    # 显示所有主题
    path('topics/',views.topics,name='topics'),

    # 各个主题
    path('topics/(?P<topic_id>\d+)/', views.topic, name='topic'),
]
