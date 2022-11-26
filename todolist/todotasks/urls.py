from django.urls import path
from . import views as v

urlpatterns = [
        path('', v.TaskListView.as_view(), name="task-list"),
        path("<int:pk>/", v.TaskDetailView.as_view(), name = "task-detail")
        ]
