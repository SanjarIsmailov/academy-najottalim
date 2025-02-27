from django.contrib import admin
from .models import Mentor, Student, Attendance

class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('student', 'lesson_number', 'present')  # Show in list
    list_filter = ('lesson_number', 'present')  # Filter options
    list_editable = ('present',)  # Allow inline checkbox editing

admin.site.register(Mentor)
admin.site.register(Student)
admin.site.register(Attendance, AttendanceAdmin)
