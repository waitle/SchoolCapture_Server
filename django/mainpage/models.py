from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.CharField(max_length=10)
    email = models.CharField(max_length=50, EmailField)
    phone = models.CharField(max_length=13)
    description = models.TextField
    symbol = models.ImageField
    
    def admit(self):
        self.published_date = timezone.now()
        self.save()

    def showall(self):
        return self

class user(models.Model):
    name = models.CharField(max_length = 10)
    email = models.CharField(max_length = 50, EmailField)
    password = models.CharField(max-length = 50)

    def admit(self):
        self.save()


    def showall(self):
        return self
    


class TimeTable(models.Model):
    name = models.CharField(max_length = 10)
    start = models.DateTimeField(TimeField)
    term = models.DateTimeField(TimeField)
    end = models.DateTimeField(TimeField)
    Tset = models.BooleanField(
    
    
