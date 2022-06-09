from rest_framework import serializers
from .models import Lecture,SubSubject,Subject
from Account.serializer import CollegeSerializer,DepartmentSerializer,UserSerializer




class SubSubjectSerializer(serializers.ModelSerializer):
    teacher = UserSerializer()
    class Meta:
        model = Subject
        fields = ('id','subject','teacher','sub_subject_name','school_hour','subject_degree',)


class LectureSerializer(serializers.ModelSerializer):
    sub_subject = SubSubjectSerializer()
    class Meta:
        model = Lecture
        fields = ('id','sub_subject','title','lecture',)


class SubjectSerializer(serializers.ModelSerializer):
    dept = DepartmentSerializer()
    teacher = UserSerializer()
    subject_lecture = LectureSerializer(many=True)
    class Meta:
        model = Subject
        fields = ('id','dept','teacher','subject_name','school_hour','subject_degree','subject_lecture',)

class PostLectureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecture
        fields = ('id', 'subject', 'sub_subject', 'title', 'lecture',)

