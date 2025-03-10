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

# class AddStudent(CreateView):
#
#     model = Student
#     form_class = StudentForm
#     template_name = 'add_student.html'  # Student qo'shish uchun template
#     # fields = ['fullname', 'phone', 'location', 'fan']  # Student modelidagi kerakli maydonlar
#     success_url = reverse_lazy('home')  # Qo'shilgandan so'ng qayta yo'naltirish
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         # context['fanlar'] = Fanlar.objects.all()
#         return context
#     def get_queryset(self):
#         return Student.objects.all()
#
#
#
# class AddFanlar(CreateView):
#     model = Fanlar
#     form_class = FanlarForm
#     template_name = 'add_fanlar.html'  # Student qo'shish uchun template
#     # fields = [ 'title',]  # Student modelidagi kerakli maydonlar
#     success_url = reverse_lazy('home')  # Qo'shilgandan so'ng qayta yo'naltirish
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         # context['fanlar'] = Fanlar.objects.all()
#         return context
#     def get_queryset(self):
#         return Fanlar.objects.all()
#
# def get_fanlar(request, fan_id):
#     students = Student.objects.filter(fan_id=fan_id)
#     fanlar = Fanlar.objects.all()
#
#     context = {
#         "fanlar": fanlar,
#         "students": students,
#     }
#     return render(request, 'get_fanlar.html', context=context)
#
#
# # def add_fanlar(request):
# #     qr_code = generate_qr_code("https://t.me/najottalim")
# #     print(request)
# #     if request.method == "POST":
# #         form = FanlarForm(request.POST)
# #         if form.is_valid():
# #             fanlar = Fanlar.objects.create(**form.cleaned_data)
# #             return redirect('home')
# #     else:
# #         form = FanlarForm()
# #     return render(request, "add_fanlar.html", {"form": form,"qr_code":qr_code})
#
# # def add_student(request):
# #     print(request)
# #     qr_code = generate_qr_code("https://t.me/najottalim")  # Shu sahifaning QR kodi
# #     if request.method == "POST":
# #         form = StudentForm(request.POST)
# #         if form.is_valid():
# #             student = Student.objects.create(**form.cleaned_data)
# #             return redirect('home')
# #     else:
# #         form = StudentForm()
# #     return render(request, "add_student.html", {"form": form,"qr_code":qr_code},)
# def generate_pdf(request, student_id, ):
#     student = get_object_or_404(Student,id=student_id)
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = f'attachment; filename="{student.fullname}.pdf"'
#
#     p = canvas.Canvas(response)
#     p.drawString(100, 790, f"familya: {student.fullname}")
#     # p.drawString(100, 770, f"ismi: {student.ismi}")
#     # p.drawString(100, 750, f"otasini_ismi: {student.otasini_ismi}")
#     p.drawString(100, 730, f"Telefon raqami: {student.phone}")
#     p.drawString(100, 710, f"Manzil: {student.location}")
#     p.drawString(100, 690, f"Fan: {student.fan.title}")
#     qr_code = generate_qr_code("https://t.me/najottalim")
#     qr_image = ImageReader(qr_code)
#     p.drawImage(qr_image, 400, 650, width=100, height=100)
#     p.showPage()
#     p.save()
#
#     return response
#
#
# class UpdateStudent(UpdateView):
#     model = Student
#     form_class = StudentForm
#     template_name = 'update_student.html'
#     success_url = reverse_lazy('home')
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = "student update qilish"
#         return context
#
# class DeleteStudent(DeleteView):
#     model = Student
#     template_name = 'delete_student.html'
#     success_url = reverse_lazy('home')
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = "Studentni o‘chirishni tasdiqlang"
#         return context
