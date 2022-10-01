from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView

from attendance.forms import semesterCreateForm, courseCreateForm, RegistrationForm, classCreateForm
from attendance.models import Semester, Course, Lecturer, Class, Student


def index(request):
    return HttpResponseRedirect(reverse('home'))


class semestersList(ListView):
    model = Semester
    template_name = 'semesters_list.html'
    ordering = ['-id']


class semesterCreate(CreateView):
    model = Semester
    template_name = 'semester_create.html'
    form_class = semesterCreateForm
    success_url = reverse_lazy("semesters_list")


class semesterUpdate(UpdateView):
    model = Semester
    template_name = 'semester_update.html'
    form_class = semesterCreateForm
    success_url = reverse_lazy("semesters_list")


def semesterDelete(request, pk):
    semester = Semester.objects.get(id=pk)
    semester.delete()
    return HttpResponseRedirect(reverse('semesters_list'))


class coursesList(ListView):
    model = Course
    template_name = 'course_list.html'


class courseCreate(CreateView):
    model = Course
    template_name = 'course_create.html'
    form_class = courseCreateForm
    success_url = reverse_lazy('courses_list')


class courseUpdate(UpdateView):
    model = Course
    template_name = 'course_update.html'
    form_class = courseCreateForm
    success_url = reverse_lazy('courses_list')


def courseDelete(request, pk):
    course = Course.objects.get(id=pk)
    course.delete()
    return HttpResponseRedirect(reverse('courses_list'))


class RegistrationView(CreateView):
    model = User
    form_class = RegistrationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class lecturerList(ListView):
    model = Lecturer
    template_name = 'lecturer_list.html'


def lecturerCreate(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        dob = request.POST.get('dob')
        if password1 == password2:
            user = User.objects.create_user(
                username=username,
                email=email,
                first_name=firstname,
                last_name=lastname,
            )
            user.set_password(password1)
            user.save()
            lecturer = Lecturer(user=user)
            lecturer.DOB = dob
            lecturer.save()
            return HttpResponseRedirect(reverse_lazy('lecturer_list'))
        else:
            return render(request, 'lecturer_create.html')
    return render(request, "lecturer_create.html")


def lecturerDetail(request, staff_id):
    lectuer = Lecturer.objects.get(staff_id=staff_id)
    context = {"lecturer": lectuer}
    return render(request, 'lecturer_update.html', context)


def lecturerUpdate(request):
    if request.method == 'POST':
        staff_id = request.POST.get('staff_id')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        dob = request.POST.get('dob')
        if password1 == password2:
            lecturer = Lecturer.objects.get(staff_id = staff_id)
            lecturer.DOB = dob
            user = User.objects.get(id=lecturer.user_id)
            user.first_name = firstname
            user.last_name = lastname
            user.email = email
            user.set_password(password1)
            user.save()
            lecturer.save()
            return HttpResponseRedirect(reverse_lazy('lecturer_list'))
        else:
            return render(request, 'lecturer_update.html')
    return render(request, "lecturer_update.html")

def lecturerDelete(request, staff_id):
    lecturer = Lecturer.objects.get(staff_id=staff_id)
    user = User.objects.get(id=lecturer.user_id)
    lecturer.delete()
    user.delete()
    return redirect('lecturer_list')


class studentList(ListView):
    model = Student
    template_name = 'student_list.html'


def studentCreate(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        dob = request.POST.get('dob')
        if password1 == password2:
            user = User.objects.create_user(
                username=username,
                email=email,
                first_name=firstname,
                last_name=lastname,
            )
            user.set_password(password1)
            user.save()
            student = Student(user=user)
            student.DOB = dob
            student.save()
            return HttpResponseRedirect(reverse_lazy('student_list'))
        else:
            return render(request, 'student_create.html')
    return render(request, "student_create.html")


def studentDetail(request, student_id):
    student = Student.objects.get(student_id = student_id)
    context = {"student": student}
    return render(request, 'student_update.html', context)


def studentUpdate(request):
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        dob = request.POST.get('dob')
        if password1 == password2:
            student = Student.objects.get(student_id=student_id)
            student.DOB = dob
            user = User.objects.get(id=student.user_id)
            user.first_name = firstname
            user.last_name = lastname
            user.email = email
            user.set_password(password1)
            user.save()
            student.save()
            return HttpResponseRedirect(reverse_lazy('student_list'))
        else:
            return render(request, 'student_update.html')
    return render(request, "student_update.html")

def studentDelete(request, student_id):
    student = Student.objects.get(student_id=student_id)
    user = User.objects.get(id=student.user_id)
    student.delete()
    user.delete()
    return redirect('student_list')


class classList(ListView):
    model = Class
    template_name = 'class_list.html'


class classCreate(CreateView):
    model = Class
    template_name = 'class_create.html'
    form_class = classCreateForm
    success_url = reverse_lazy('class_list')


class classUpdate(UpdateView):
    model = Class
    template_name = 'class_update.html'
    form_class = classCreateForm
    success_url = reverse_lazy('class_list')


def classDelete(request, pk):
    theClass = Class.objects.get(id=pk)
    theClass.delete()
    return HttpResponseRedirect(reverse('class_list'))
