from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Lecturer(models.Model):
    staff_id = models.AutoField(primary_key=True)
    DOB = models.DateField(blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='lecturer_user')

    def __str__(self):
        return self.staff_id.__str__() +"-"+ self.user.username +"-"+ self.user.first_name +" "+self.user.last_name

class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    DDOB = models.DateField(blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_user')

    def __str__(self):
        return self.student_id.__str__() +":"+self.user.first_name +" "+ self.user.last_name


class Semester(models.Model):
    year = models.IntegerField(blank=False)
    semester = models.CharField(max_length=50)

    def __str__(self):
        return self.semester


class Course(models.Model):
    code = models.CharField(max_length=50)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Class(models.Model):
    number = models.IntegerField(null=False, blank=False)
    semester = models.ForeignKey(Semester,  on_delete=models.CASCADE, null=False, blank=False)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=False, blank=False)
    lecturer = models.ForeignKey(Lecturer, on_delete=models.SET_NULL, null=True, blank=True)
    student = models.ManyToManyField(Student, verbose_name='enrolled student')


    def __str__(self):
        return self.number.__str__()

class CollegeDay(models.Model):
    date = models.DateField()
    theClass = models.ManyToManyField(Class, through='Attendance', null=True)

    def __str__(self):
        return self.date.__str__()

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, default=False)
    attendance = models.BooleanField(default=False)
    theClass = models.ForeignKey(Class, on_delete=models.CASCADE)
    collegeDay = models.ForeignKey(CollegeDay, on_delete=models.CASCADE)

    def __str__(self):
        return self.student.user.first_name +" "+ self.student.user.last_name
