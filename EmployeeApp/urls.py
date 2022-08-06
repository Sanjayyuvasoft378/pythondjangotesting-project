# from django.conf.urls import url
from django.urls import path
from EmployeeApp import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    path("books/",views.BookApi,name='bookApi'),
    path("department/",views.departmentApi,name='department'),
    path("department/([0-9]+)/",views.departmentApi,name='departmentApi'),
    path("employee/",views.employeeApi,name='employeeApi'),
    path("employee/([0-9]+)/",views.employeeApi,name='employeeApi'),
    path("Employee/SaveFile/",views.SaveFile,name='SaveFile'),
    path("employee/",views.employeeApi,name='employeeApi'),
    path("StudentDetailAPI/",views.StudentDetailAPI,name='StudentDetailAPI'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)