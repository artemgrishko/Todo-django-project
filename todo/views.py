from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from todo.models import Task, Tag


def task_list(request):
    tasks = Task.objects.all()
    for task in tasks:
        task.tag_list = ", ".join(tag.name for tag in task.tags.all())
    return render(request, 'todo/task_list.html', {'task_list': tasks})


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("todo:task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("todo:task-list")


class TagListView(generic.ListView):
    model = Tag


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("todo:tag-list")
