
# 定义learning_logs的urls

from django.urls import path

from . import views

urlpatterns = [
    # 主页
    path('',views.index,name='index'),
]
