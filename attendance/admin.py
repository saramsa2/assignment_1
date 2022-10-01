from django.contrib import admin

# Register your models here.
from attendance.models import Lecturer, Student, Semester, Course, Class, CollegeDay

admin.site.register(Lecturer)
admin.site.register(Student)
admin.site.register(Semester)
admin.site.register(Course)
admin.site.register(Class)
admin.site.register(CollegeDay)