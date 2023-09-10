from rest_framework.response import Response
from rest_framework import status


class Errors:


    @staticmethod
    def not_found():
        data = {
            'error':'item not found'
        }

        return Response(data=data, status=status.HTTP_404_NOT_FOUND)
    
    @staticmethod
    def bad_request(message:str):
        data = {
            'error':message
        }

        return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
    
    @staticmethod
    def delete():
        data = {
            'delete':'item deleted succesfull'
        }

        return Response(data=data, status=status.HTTP_204_NO_CONTENT)
