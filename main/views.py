from django.shortcuts import render, HttpResponse

from rest_framework.views import APIView, Response, status

from main.services import TaskServices
from main.serializer import TaskSerializer
from main.models import Task


class MainViews:


    def panel(request):
        return HttpResponse('Online')


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
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                        


    
