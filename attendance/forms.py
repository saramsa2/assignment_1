from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from attendance.models import Semester, Course, Class, Lecturer


class semesterCreateForm(forms.ModelForm):
    class Meta:
        model = Semester
        fields = ['year', 'semester']

        widgets = {
            'year': forms.NumberInput(attrs={"class": "form-content", "placeholder": "year"}),
            'semester': forms.TextInput(attrs={"class": "form-content", "placeholder": "semester"}),
        }


class courseCreateForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['code', 'name']

        widgets = {
            'code': forms.TextInput(attrs={"class": "form-content", "placeholder": "code"}),
            'name': forms.TextInput(attrs={"class": "form-content", "placeholder": "name"}),
        }


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']


class classCreateForm(forms.ModelForm):
    # course = forms.ModelChoiceField(queryset=Course.objects.all())
    # semester = forms.ModelChoiceField(queryset=Semester.objects.all())
    # lecturer = forms.ModelChoiceField(queryset=Lecturer.objects.all())

    class Meta:
        model = Class
        fields = ['number', 'semester', 'course', 'lecturer', 'student']
        widgets = {
            'number': forms.NumberInput(attrs={"class": "form-content", "placeholder": "code"}),
            'semester': forms.Select(attrs={'class': 'form-content'}),
            'course': forms.Select(attrs={'class': 'form-content'}),
            'lecturer': forms.Select(attrs={'class': 'form-content'}),
            'student': FilteredSelectMultiple('student', False),
        }