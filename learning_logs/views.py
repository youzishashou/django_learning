from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Topic
from .forms import TopicForm,EntryForm
# Create your views here.

def index(request):
    """学习笔记的主页"""
    return render(request, 'learning_logs/index.html')

def topics(request):
    # 显示所有主题
    topics = Topic.objects.order_by('date_added')
    context = {'topics':topics}
    return render(request,'learning_logs/topics.html',context)

def topic(request, topic_id):
    # 显示单个主题条目
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

def add_new_topic(request):
    #添加新主题
    if request.method != 'POST':
        #创建一个新表单
        form = TopicForm()
    else:
        #提交表单
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topics'))

    context = {'form':form}
    return render(request,'learning_logs/add_new_topic.html',context)

def add_new_entry(request,topic_id):
    # 添加新条目
    topic = Topic.objects.get(id = topic_id)
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(request.POST)
        if form.is_valid():
            new_entry = form.save(commit = False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('learning_logs:topic',args=[topic_id]))
    context = {'form': form,'topic':topic}
    return render(request, 'learning_logs/add_new_entry.html', context)