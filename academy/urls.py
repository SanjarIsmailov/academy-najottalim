from django.urls import path
from .views import attendance_page, update_attendance

app_name = 'academy'

urlpatterns = [
    path('', attendance_page, name='attendance_page'),
    path("update_attendance/", update_attendance, name="update_attendance")
]
