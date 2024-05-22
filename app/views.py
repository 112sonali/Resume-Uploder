from django.shortcuts import render
from.models import *
from.serializer import profileserializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class profile_view(APIView):
    def post(self,request):
        serializer = profileserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':"Resume upload successfully",'status':"success",'candidate':serializer.data},
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors)