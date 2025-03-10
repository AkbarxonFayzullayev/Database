# from django.http import HttpResponse

from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
# from reportlab.lib.utils import ImageReader

from .forms import *
from .models import *
# from .utils import generate_qr_code
from django.http import HttpResponse
# from reportlab.pdfgen import canvas

def index(request):
    region = Region.objects.all()
    department = Department.objects.all()
    employee = Employee.objects.all()

    context={
        "region":region,
        "departament":department,
        "employee":employee,
    }
    return render(request,'index.html',context=context)




class HomeDepartment(ListView):
    model = Department

    template_name = 'index.html'
    context_object_name = 'department'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['employees'] = Employee.objects.all()
        return context
    def get_queryset(self):
        return Department.objects.all()

class AddEmployee(CreateView):

    model = Employee
    form_class = EmployeeForm
    template_name = 'add_employee.html'
    # fields = ['fullname', 'phone', 'location', 'fan']
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['fanlar'] = Fanlar.objects.all()
        return context
    def get_queryset(self):
        return Employee.objects.all()

class AddRegion(CreateView):

    model = Region
    form_class = RegionForm
    template_name = 'add_region.html'
    # fields = ['fullname', 'phone', 'location', 'fan']
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['fanlar'] = Fanlar.objects.all()
        return context
    def get_queryset(self):
        return Region.objects.all()

class AddDepartment(CreateView):

    model = Department
    form_class = DepartmentForm
    template_name = 'add_department.html'
    # fields = ['fullname', 'phone', 'location', 'fan']
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['fanlar'] = Fanlar.objects.all()
        return context
    def get_queryset(self):
        return Department.objects.all()

