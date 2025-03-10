import re
from django import forms
from django.core.exceptions import ValidationError

from .models import Region,Employee

class RegionForm(forms.ModelForm):
    class Meta:
        model = Region
        fields = ['title']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
    }

    def clean_title(self):
        title = self.cleaned_data["title"]
        if re.match(r'^[A-Z][a-zA-Z]*$',title):
            raise ValidationError("Title raqam bo'lmasin")
        return title


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Region
        fields = ['title']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
    }
    def clean_title(self):
        title = self.cleaned_data["title"]
        if re.match(r'^[A-Z][a-zA-Z]*$',title):
            raise ValidationError("Title raqam bo'lmasin")
        return title
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name','middle_name','last_name','phone','data_file']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'middle_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'data_file': forms.FileInput(attrs={'class': 'form-control'}),
            'region_id': forms.Select(attrs={'class': 'form-control'}),
            'department_id': forms.Select(attrs={'class': 'form-control'}),
        }
    def first_name_vd(self):
        first_name = self.cleaned_data["first_name"]
        if re.match(r'^[A-Z][a-zA-Z]{3,25}$', first_name):
            raise ValidationError("First Name raqam va uzunligi 3 va 25 oraliqida bo'lsin")
        return first_name
    def last_name_vd(self):
        last_name = self.cleaned_data["last_name"]
        if re.match(r'^[A-Z][a-zA-Z]{3,25}$', last_name):
            raise ValidationError("Last Name raqam va uzunligi 3 va 25 oraliqida bo'lsin")
        return last_name
    def middle_name_vd(self):
        middle_name = self.cleaned_data["middle_name"]
        if re.match(r'^[A-Z][a-zA-Z]{3,25}$', middle_name):
            raise ValidationError("Middle Name raqam va uzunligi 3 va 25 oraliqida bo'lsin")
        return middle_name
    def phone_vd(self):
        phone = self.cleaned_data["phone"]
        if re.match(r'^\+998\d{9}$', phone):
            raise ValidationError("Telefon raqami +998XXXXXXXXX formatda bo'lsin.")
        return phone
    def email_vd(self):
        email = self.cleaned_data["email"]
        if re.match(r'^[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,6}$',email):
            raise ValidationError("Emailni to'g'ri kiriting.")
        return email
