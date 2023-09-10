from django.urls import path
from main.views import MainViews, ApiViews

urlpatterns = [
    path('', MainViews.panel, name='panel'),
    path('api/task', ApiViews.TaskAPI.as_view(), name='task_api'),
    path('api/task/<id>', ApiViews.TaskDetailAPI.as_view(), name='task_detail_api')
]
