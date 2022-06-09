from django.db import models
from django.contrib.auth.models import User
from Account.models import Department,College



class Subject(models.Model):
    dept = models.ForeignKey(Department,on_delete=models.CASCADE,related_name='subject')
    teacher = models.ForeignKey(User,on_delete=models.CASCADE,related_name='teacher',blank=True,null=True)
    subject_name = models.CharField(max_length=150)
    school_hour = models.TimeField(blank=True,null=True)
    subject_degree = models.FloatField()

    def __str__(self):
        return self.subject_name


class SubSubject(models.Model):
    subject = models.OneToOneField(Subject,on_delete=models.CASCADE,related_name='SubSubject')
    teacher = models.ForeignKey(User,on_delete=models.CASCADE,related_name='Teacher',blank=True,null=True)
    sub_subject_name = models.CharField(max_length=150)
    school_hour = models.TimeField(blank=True, null=True)
    subject_degree = models.FloatField()

    def __str__(self):
        return self.sub_subject_name

class Lecture(models.Model):
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE,related_name='subject_lecture',blank=True,null=True)
    sub_subject = models.ForeignKey(SubSubject,on_delete=models.CASCADE,related_name='sub_subject_lecture',blank=True,null=True)
    title = models.CharField(max_length=200)
    lecture = models.FileField(upload_to='lecture_file/')

    def __str__(self):
        return self.title