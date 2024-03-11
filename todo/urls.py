from django.urls import path
from todo.views import TaskListView, TagListView, TagCreateView

urlpatterns = [
    path("", TaskListView.as_view(), name="task_list"),
    path("tags/", TagListView.as_view(), name="tag_list"),
    path("tags/create", TagCreateView.as_view(), name="tag_create")
]

app_name = "todo"
