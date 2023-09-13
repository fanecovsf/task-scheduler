from django.urls import path
from main.views import MainViews, ApiViews

urlpatterns = [
    path('panel/', MainViews.panel, name='panel'),
    path('panel/task-register/', MainViews.task_register, name='task-register'),

    path('api/task', ApiViews.TaskAPI.as_view(), name='task_api'),
    path('api/task/<id>', ApiViews.TaskDetailAPI.as_view(), name='task_detail_api'),
    path('api/task/execute/<id>', ApiViews.TaskExecutionAPI.as_view(), name='task_execution_api')
]
