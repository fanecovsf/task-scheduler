from django.shortcuts import render, HttpResponse

from rest_framework.views import APIView, Response, status

from main.services import TaskServices
from main.serializer import TaskSerializer
from main.models import Task
from main.errors import Errors


class MainViews:


    def panel(request):
        tasks = TaskServices.query_all()
        return render(request, 'panel.html', context={
            'tasks':tasks
        })
    
    def task_register(request):
        return render(request, 'task-register.html')


class ApiViews:


    class TaskAPI(APIView):


        def get(self, request):
            tasks = TaskServices.query_all()
            serializer = TaskSerializer(tasks, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)
        
        def post(self, request):
            serializer = TaskSerializer(data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Errors.bad_request('data format is not valid')
            
        def delete(self, request):
            return Errors.not_allowed()
        
        def put(self, request):
            return Errors.not_allowed()
            

    class TaskDetailAPI(APIView):
        

        def get(self, request, id):
            try:
                task = TaskServices.get(id)
            except:
                return Errors.not_found()

            if task:
                serializer = TaskSerializer(task)
                return Response(serializer.data, status=status.HTTP_200_OK)

        def delete(self, request, id):
            try:
                task = TaskServices.get(id)
            except:
                return Errors.not_found()
            
            if task:
                task.delete()
                return Errors.delete()
            
        def put(self, request, id):
            try:
                task = TaskServices.get(id)
            except:
                return Errors.not_found()
            
            if task:
                serializer = TaskSerializer(task, data=request.data)

                if serializer.is_valid():
                    serializer.save()
                    return Response(data=serializer.data, status=status.HTTP_202_ACCEPTED)
                else:
                    return Errors.bad_request('data format is not valid')
                
        def post(self, request):
            return Errors.not_allowed()


    
