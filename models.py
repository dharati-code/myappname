from django.db import models
from datetime import datetime


# Create your models here.

class School(models.Model):
    name = models.CharField(max_length = 400,null=True)
    def __str__(self):
        return self.name
      
class Certificate(models.Model):
    name = models.CharField(max_length = 400,null=True)
    def __str__(self):
        return self.name

class Faculty(models.Model):
    name = models.CharField(max_length = 400,null=True)
    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length = 400,null=True)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    def __str__(self):
        return self.name 

class Grade(models.Model):
    type = models.CharField(max_length = 3)
    def __str__(self):
        return self.type

class Student(models.Model):
    fullname = models.CharField(max_length = 40,null=True)
    year_of_graduation = models.IntegerField
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE, blank=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    certificate_type = models.ForeignKey(Certificate, on_delete=models.CASCADE)

    def __str__(self):
        return self.fullname 