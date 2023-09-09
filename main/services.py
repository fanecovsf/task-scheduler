from main.models import Task


class TaskServices:


    @staticmethod
    def query_all():
        return Task.objects.all()
    
    @staticmethod
    def get(id):
        return Task.objects.get(id=id)
