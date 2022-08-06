from re import L
from django.db import models

# Create your models here.

class Departments(models.Model):
    DepartmentId = models.AutoField(primary_key=True)
    DepartmentName = models.CharField(max_length=100)

class Employees(models.Model):
    EmployeeId = models.AutoField(primary_key=True)
    EmployeeName = models.CharField(max_length=100)
    Department = models.CharField(max_length=100)
    DateOfJoining = models.DateField()
    PhotoFileName = models.CharField(max_length=100)

class Books(models.Model):
    bookId = models.AutoField(primary_key=True)
    bookName = models.CharField(max_length=20)
    bookTitle = models.CharField(max_length=100)
    bookAuthorName = models.CharField(max_length=20)
    price = models.IntegerField()
    # bookImage = models.FileField()

class StudentDetail(models.Model):
    studentId = models.AutoField(primary_key=True)
    studentName = models.CharField(max_length=20)
    studentAddress= models.CharField(max_length=100)
    stuEmail = models.EmailField()
    stuPhoneNumber = models.IntegerField()
    

