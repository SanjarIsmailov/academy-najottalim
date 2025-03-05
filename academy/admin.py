from django.contrib import admin
from .models import Group, Student, Lesson, Attendance

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ("name", "mentorGmail")
    search_fields = ("name", "mentorGmail")

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("name", "phone_number", "group")
    list_filter = ("group",)
    search_fields = ("name", "phone_number")

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ("group", "number", "date", "closed")
    list_filter = ("group", "closed")
    search_fields = ("group__name",)
    ordering = ("group", "number")

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ("student", "lesson", "status")
    list_filter = ("lesson__group", "status")
    search_fields = ("student__name", "lesson__group__name")
    ordering = ("lesson", "student")

