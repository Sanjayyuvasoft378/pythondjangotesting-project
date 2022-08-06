from pyexpat import model
from attr import fields
from rest_framework import serializers
from EmployeeApp.models import Books, Departments, Employees, StudentDetail

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = ('DepartmentId',
                  'DepartmentName')

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = ('EmployeeId',
                  'EmployeeName',
                  'Department',
                  'DateOfJoining',
                  'PhotoFileName')

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentDetail
        fields='__all__'
        
                  