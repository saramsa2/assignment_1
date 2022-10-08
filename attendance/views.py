
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView

from attendance.forms import semesterCreateForm, courseCreateForm, RegistrationForm, classCreateForm
from attendance.models import Semester, Course, Lecturer, Class, Student, CollegeDay, Attendance

import pandas as pd

def index(request):
    if(request.user.is_authenticated):
        if Student.objects.filter(user=request.user).exists():
            return redirect('student_attendance')
        else:
            return redirect('class_list')
    else:
        return redirect('login')


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
    template_name = 'semester_create.html'
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
    template_name = 'course_create.html'
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
            try:
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
            except:
                return redirect('lecturerCreate')
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


def studentAddFromFile(request):
    try:
        if request.method=='POST' and request.FILES["myfile"]:
            myfile = request.FILES["myfile"]
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            upload_file_url = fs.url(filename)
            excel_data = pd.read_excel(myfile)
            data = pd.DataFrame(excel_data)
            usernames = data["Username"].tolist()
            firstnames = data["First Name"].tolist()
            lastnames = data["Last Name"].tolist()
            emails = data["Email"].tolist()
            dobs = data["DOB"].tolist()

            i = 0
            while i < len(usernames):
                username = usernames[i]
                firstname = firstnames[i]
                lastname = lastnames[i]
                email = emails[i]
                dob = dobs[i]
                password = str(dobs[i]).split(" ")[0].replace("-", "")
                user = User.objects.create_user(username=username)
                user.first_name = firstname
                user.last_name = lastname
                user.email = email
                user.set_password(password)
                user.save()
                student = Student(user=user)
                student.DOB = dob
                student.save()
                i = i + 1
            return HttpResponseRedirect(reverse_lazy('student_list'))
        return HttpResponseRedirect(reverse_lazy('student_list'))
    except:
        return HttpResponseRedirect(reverse_lazy('student_list'))


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
    template_name = 'class_create.html'
    form_class = classCreateForm
    success_url = reverse_lazy('class_list')


def classDelete(request, pk):
    theClass = Class.objects.get(id=pk)
    theClass.delete()
    return HttpResponseRedirect(reverse('class_list'))


def classAttendanceList(request, pk, att_date_id):
    theClass = Class.objects.get(id=pk)
    students_id = theClass.student.values_list('pk', flat=True)
    students = list()
    attend_numbers = list()
    for student_id in students_id:
        students.append(Student.objects.get(student_id=student_id))
        total_attend = Attendance.objects.filter(student_id=student_id).filter(theClass=theClass)
        attended_class = total_attend.filter(attendance=True)
        if total_attend.count() == 0:
            attend_ratio = '-'
        else:
            attend_ratio = attended_class.count() * 100 / total_attend.count()
        attend_numbers.append({'total_attend':total_attend.count(), 'num_attended':attended_class.count(), 'attend_ratio': attend_ratio})
    attendance = Attendance.objects.filter(theClass=theClass).order_by('-collegeDay__date')
    attendanceDay = attendance.values_list('collegeDay').distinct()
    attDateList = list()
    for dayId in attendanceDay:
        newId = str(dayId)
        newId = newId[1:len(newId)-2]
        attDateList.append(CollegeDay.objects.get(id=newId))

    context = {'class': theClass,
               'students': students,
               'attendance': attendance,
               'attDateList': attDateList,
               'attDateId': att_date_id,
               'attended_numbers': attend_numbers}
    return render(request, 'class_attendance_list.html', context)


def collegeDayCreate(request, pk):
    if request.method == 'POST':
        date = request.POST.get('new_college_day')
        theClass = Class.objects.get(id=pk)
        if CollegeDay.objects.filter(date=date).count() == 0:
            collegeDay = CollegeDay(date=date)
            collegeDay.save()
        else:
            collegeDay = CollegeDay.objects.get(date=date)

        for student in theClass.student.all():
            attendance = Attendance(student=student)
            attendance.collegeDay = collegeDay
            attendance.theClass = theClass
            attendance.save()
    return redirect('class_attendance_list', pk, '1')

def attendanceToggle(request, pk, attend_id, att_date_id):
    attendance = Attendance.objects.get(id=attend_id)
    attendance.attendance = not attendance.attendance
    attendance.save()
    return redirect('class_attendance_list', pk, att_date_id)


def studentAttendance(request):
    user = request.user;
    student = Student.objects.get(user=user)
    attendance = Attendance.objects.filter(student=student).order_by('theClass__number')
    theClasses = attendance.values_list('theClass__number').order_by().distinct()
    theClass = list()
    for oldClass in theClasses:
        tempClass = oldClass.__str__()
        theClass.append(tempClass[1:len(tempClass)-2])
    context = {'user': user,
               'student': student,
               'attendance': attendance,
               'class': theClass}
    return render(request, 'student_attendance.html', context)


def sendEmail(request):
    users = User.objects.all()
    if request.method == "POST":
        subject = request.POST.get("subject")
        body = request.POST.get("body")
        receiver = User.objects.get(id=request.POST.get("user"))
        senderEmail = "gabriel_sl19798@hotmail.com"
        try:
            send_mail(subject, body, senderEmail, [receiver.email], fail_silently=False)
            return render(request, "emailsending.html",{
                "message": "email sending out",
                "users": users
            })
        except:
            return render(request, "emailsending.html", {
                "message": "email sending failed",
                "users": users
            })
    return render(request, "emailsending.html", {
        "message": "",
        "users": users
    })

