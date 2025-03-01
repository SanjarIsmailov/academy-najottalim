from django.contrib import admin
from .models import Group, Student, Lesson, Attendance

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone_number', 'group')

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('id', 'group', 'number', 'date')

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'student', 'lesson', 'status')
