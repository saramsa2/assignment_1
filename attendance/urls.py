from django.contrib.auth import login
from django.contrib.sitemaps.views import index
from django.views.generic import TemplateView

from django.urls import path

from attendance.views import semestersList, semesterUpdate, semesterDelete, semesterCreate, coursesList, courseCreate, \
    courseUpdate, courseDelete, lecturerList, lecturerCreate, RegistrationView, lecturerUpdate, lecturerDetail, \
    lecturerDelete, classList, classCreate, classUpdate, classDelete, studentList, studentCreate, studentDetail, \
    studentUpdate, studentDelete

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('login/', TemplateView.as_view(template_name='registration/login.html'), name='login'),
    path('account/register/', RegistrationView.as_view(), name='register'),
    path('semesters/', semestersList.as_view(), name='semesters_list'),
    path('semester/create', semesterCreate.as_view(), name='semester_create'),
    path('semester/<int:pk>/update/', semesterUpdate.as_view(), name='semester_update'),
    path('semester/<int:pk>/delete/', semesterDelete, name='semester_delete'),
    path('courses/', coursesList.as_view(), name='courses_list'),
    path('course/create/', courseCreate.as_view(), name='course_create'),
    path('course/<int:pk>/update/', courseUpdate.as_view(), name='course_update'),
    path('course/<int:pk>/delete/', courseDelete, name='course_delete'),
    path('lecturers/', lecturerList.as_view(), name='lecturer_list'),
    path('lecturer/create/', lecturerCreate, name='lecturer_create'),
    path('lecturer/<int:staff_id>/detail', lecturerDetail, name='lecturer_detail'),
    path('lecturer/update/', lecturerUpdate, name='lecturer_update'),
    path('lecturer/<int:staff_id>/delete/', lecturerDelete, name='lecturer_delete'),
    path('student/', studentList.as_view(), name='student_list'),
    path('student/creat/', studentCreate, name='student_create'),
    path('studnet/<int:student_id>/detail/', studentDetail, name='student_detail' ),
    path('student/update/', studentUpdate, name='student_update'),
    path('student/<int:student_id>/delete/', studentDelete, name='student_delete'),
    path('class/', classList.as_view(), name='class_list'),
    path('class/create/', classCreate.as_view(), name='class_create'),
    path('class/<int:pk>/update/', classUpdate.as_view(), name='class_update'),
    path('class/<int:pk>/delete/', classDelete, name='class_delete'),
]