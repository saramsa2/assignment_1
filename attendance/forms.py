from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from attendance.models import Semester, Course, Class


class semesterCreateForm(forms.ModelForm):
    class Meta:
        model = Semester
        fields = ['year', 'semester']

        widgets = {
            'year': forms.NumberInput(attrs={"class": "form-control", "placeholder": "year"}),
            'semester': forms.TextInput(attrs={"class": "form-control", "placeholder": "semester"}),
        }


class courseCreateForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['code', 'name']

        widgets = {
            'code': forms.TextInput(attrs={"class": "form-control", "placeholder": "code"}),
            'name': forms.TextInput(attrs={"class": "form-control", "placeholder": "name"}),
        }


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']


class classCreateForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = ['number', 'semester', 'course', 'lecturer', 'student']
        widgets = {
            'number': forms.NumberInput(attrs={"class": "form-control mb-3", "placeholder": "code"}),
            'semester': forms.Select(attrs={'class': 'form-control form-select mb-3'}),
            'course': forms.Select(attrs={'class': 'form-control form-select mb-3'}),
            'lecturer': forms.Select(attrs={'class': 'form-control form-select mb-3'}),
            'student': FilteredSelectMultiple('student', False),
        }