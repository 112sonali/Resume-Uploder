from rest_framework.response import Response
from .models import *
from .serializer import profileserializer
from rest_framework.views import APIView
from rest_framework import status

# Create your views here.
class ProfileView(APIView):
    def post(self, request, format=None):
        serializer = profileserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Resume Uploaded Successfully',
                             'status': 'success', 'candidate': serializer.data},
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors)

    def get(self, request, format=None):
        candidates = Profile.objects.all()
        serializer = profileserializer(candidates, many=True)
        return Response({'status': 'success', 'candidates': serializer.data}, status=status.HTTP_200_OK)

    def delete(self, request, format=None):
        candidates = Profile.objects.all()
        # serializer = ProfileSerializer.objects.all()
        return Response({'status': 'success'})

    def put(self, request, pk, format=None):
        try:
            profile = Profile.objects.get(pk=pk)
        except Profile.DoesNotExist:
            return Response({'msg': 'Profile not found', 'status': 'error'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Profile Updated Successfully',
                             'status': 'success', 'candidate': serializer.data},
                            status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class ProfileDetailView(APIView):
    def get_object(self, pk):
        try:
            return Profile.objects.get(pk=pk)
        except Profile.DoesNotExist:
            return None

    def get(self, request, pk, format=None):
        profile = self.get_object(pk)
        if profile is None:
            return Response({'msg': 'Profile not found', 'status': 'error'}, status=status.HTTP_404_NOT_FOUND)
        serializer = profileserializer(profile)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        profile = self.get_object(pk)
        if profile is None:
            return Response({'msg': 'Profile not found', 'status': 'error'}, status=status.HTTP_404_NOT_FOUND)
        serializer = profileserializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Profile Updated Successfully',
                             'status': 'success', 'candidate': serializer.data},
                            status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)






