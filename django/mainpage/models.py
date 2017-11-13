from django.db import models
import os,sys

class Subject(models.Model):
    name = models.CharField(max_length=100, default="과목명")
    teacher = models.CharField(max_length=10, default="담당선생님")
    email = models.EmailField(max_length=50, default="이메일")
    phone = models.CharField(max_length=13, default="연락처")
    description = models.TextField( default="수행평가등을 메모하세요")
    symbol = models.ImageField

    def admit(self):
        self.published_date = timezone.now()
        self.save()

    def showall(self):
        return self



class User(models.Model):
    name = models.CharField(max_length = 10)
    email = models.EmailField(max_length = 50)
    password = models.CharField(max_length = 50)

    def admit(self):
        self.save()


    def showall(self):
        return self



class Post(models.Model):
    auth = models.ForeignKey(User, on_delete=models.CASCADE)



class TimeTable(models.Model):
    name = models.CharField(max_length = 10, default="과목명")
    start = models.TimeField()
    term = models.TimeField()
    end = models.TimeField()
    Tset = models.BooleanField()
