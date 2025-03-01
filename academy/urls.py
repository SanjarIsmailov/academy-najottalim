from django.urls import path
from .views import attendance_page, update_attendance, start_lesson, close_lesson

app_name = "academy"

urlpatterns = [
    path('', attendance_page, name='attendance_page'),
    path('update_attendance/', update_attendance, name='update_attendance'),
    path('start_lesson/', start_lesson, name='start_lesson'),
    path('close_lesson/', close_lesson, name='close_lesson'),
]
