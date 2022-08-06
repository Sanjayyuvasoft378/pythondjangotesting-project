from shutil import ExecError
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from itsdangerous import json
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework.views import APIView
from EmployeeApp.models import Books, Departments,Employees, StudentDetail
from EmployeeApp.serializers import BookSerializer, DepartmentSerializer,EmployeeSerializer, StudentSerializer

from django.core.files.storage import default_storage

# Create your views here.
@csrf_exempt
def departmentApi(request,id=0):
    if request.method=='GET':
        departments = Departments.objects.all()
        departments_serializer = DepartmentSerializer(departments, many=True)
        return JsonResponse(departments_serializer.data, safe=False)

    elif request.method=='POST':
        department_data=JSONParser().parse(request)
        department_serializer = DepartmentSerializer(data=department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("Added Successfully!!" , safe=False)
        return JsonResponse("Failed to Add.",safe=False)
    
    elif request.method=='PUT':
        department_data = JSONParser().parse(request)
        department=Departments.objects.get(DepartmentId=department_data['DepartmentId'])
        department_serializer=DepartmentSerializer(department,data=department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method=='DELETE':
        department=Departments.objects.get(DepartmentId=id)
        department.delete()
        return JsonResponse("Deleted Succeffully!!", safe=False)

@csrf_exempt
def employeeApi(request,id=0):
    if request.method=='GET':
        employees = Employees.objects.all()
        employees_serializer = EmployeeSerializer(employees, many=True)
        return JsonResponse(employees_serializer.data, safe=False)

    elif request.method=='POST':
        employee_data=JSONParser().parse(request)
        employee_serializer = EmployeeSerializer(data=employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse("Added Successfully!!" , safe=False)
        return JsonResponse("Failed to Add.",safe=False)
    
    elif request.method=='PUT':
        employee_data = JSONParser().parse(request)
        employee=Employees.objects.get(EmployeeId=employee_data['EmployeeId'])
        employee_serializer=EmployeeSerializer(employee,data=employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method=='DELETE':
        employee=Employees.objects.get(EmployeeId=id)
        employee.delete()
        return JsonResponse("Deleted Succeffully!!", safe=False)


@csrf_exempt
def SaveFile(request):
    file=request.FILES['myFile']
    file_name = default_storage.save(file.name,file)

    return JsonResponse(file_name,safe=False)


def BookApi(request,id=0):
    if request.method =='GET':
        book = Books.objects.all()
        book_serializer = BookSerializer(book,many=True)
        return JsonResponse(book_serializer.data,safe=False)

    elif request.method =="POST":
        bookDetails = JSONParser().parse(request)
        book_serializer = BookSerializer(data=bookDetails)
        if book_serializer.is_valid():
            book_serializer.save()
            return JsonResponse("data added successfully", safe=False)
        return JsonResponse("failed to add",safe=False)
    
    elif request.method == 'PUT':
        booksDetail = JSONParser().parse(request)
        book = Books.objects.get(bookId=booksDetail['bookId'])
        book_serializer = BookSerializer(book, data=bookDetails)
        if book_serializer.is_valid():
            book_serializer.save()
            return JsonResponse("data updated sucessfully",safe=False)
        return JsonResponse("failed to upate",safe=False)

    elif request.method =="DELETE":
        bookDetails = Books.objects.get(bookId = id)
        bookDetails.delete()
        return JsonResponse("data deleted successfully",safe=False)
        

def StudentDetailAPI(request,id=0):
    if request.method == "GET":
        studentsDetail = StudentDetail.objects.all()
        student_serializer = StudentSerializer(studentsDetail, many=True)
        return JsonResponse(student_serializer.data, safe=False)

    if request.method == "POST":
        stu_detail = JSONParser().parse(request)
        stud_serializer = StudentSerializer(stu_data= stu_detail)
        if stud_serializer.is_valid():
            stud_serializer.save()
            return JsonResponse("data added successfully",safe=False)
        return JsonResponse("failed to add",safe=False)

    if request.method == "PUT":
        stud_detail = JSONParser().parse(request)
        studentInfo = StudentDetail.objects.get(studnetId = stud_detail['studnetId'])
        stud_serializer = StudentSerializer(studentInfo, data = stud_detail)
        if stud_serializer.is_valid():
            stud_serializer.save()
            return JsonResponse("Data update successfully",safe=False)
        return JsonResponse("updated to failed",safe =False)


    if request.method=="DELETE":
        studentdata = StudentDetail.objects.get(studentId=id)
        studentdata.delete()
        return JsonResponse("data delete successgully",safe=False)
    
