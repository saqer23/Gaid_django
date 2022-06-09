from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.db.models import Q
from .models import Subject,SubSubject,Lecture
from .serializer import SubjectSerializer,SubSubjectSerializer,LectureSerializer,PostLectureSerializer

@api_view(['GET'])
def get_lecture_subject(request):
    user = request.user
    if user.is_authenticated:
        subject = Subject.objects.filter(dept=user.profile.dept)
        serializer = SubjectSerializer(subject,many=True)
        return Response(serializer.data)
    return Response({
        'error':'not authenticated',
    },status=400)


@api_view(['POST'])
def post_lecture(request):
    user = request.user
    if user.is_authenticated:
        serializer = PostLectureSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)