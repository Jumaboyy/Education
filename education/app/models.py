from django.db import models

# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=100,verbose_name='Course Name')
    description = models.TextField(verbose_name='Course Description')
    price = models.IntegerField(verbose_name='Course Price')
    lifetime=models.IntegerField(verbose_name='Course Lifetime')

    def __str__(self):
        return self.name



class Teacher(models.Model):
    full_name = models.CharField(max_length=255,verbose_name='Teacher Full Name')
    status = models.CharField(max_length=255,verbose_name='Teacher Status')
    experience=models.IntegerField(verbose_name='Teacher Experience')
    course = models.ForeignKey(Course,on_delete=models.CASCADE,verbose_name='Course')

    def __str__(self):
        return self.full_name

class Student(models.Model):
    full_name = models.CharField(max_length=255,verbose_name='Student Full Name')
    phone = models.CharField(max_length=255,verbose_name='Student Phone')
    email = models.CharField(max_length=255,verbose_name='Student Email')
    parentsphone = models.CharField(max_length=255,verbose_name='Parents Phone')
    address = models.CharField(max_length=255,verbose_name='Address')
    course = models.ForeignKey(Course,on_delete=models.CASCADE,verbose_name='Course')
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE,verbose_name='Teacher')

    def __str__(self):
        return self.full_name

