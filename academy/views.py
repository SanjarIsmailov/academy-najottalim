from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Group, Student, Lesson, Attendance

def attendance_page(request):
    selected_group_id = request.GET.get("group_id")
    groups = Group.objects.all()

    if not selected_group_id:
        return render(request, "attendance.html", {"students": [], "lessons": [], "attendance_data": {}, "selected_group_id": None, "groups": groups})

    students = Student.objects.filter(group_id=selected_group_id)
    lessons = Lesson.objects.filter(group_id=selected_group_id)

    attendance_data = {student.id: {lesson.id: False for lesson in lessons} for student in students}

    for attendance in Attendance.objects.filter(student__group_id=selected_group_id):
        attendance_data[attendance.student.id][attendance.lesson.id] = attendance.status

    return render(request, "attendance.html", {"students": students, "lessons": lessons, "attendance_data": attendance_data, "selected_group_id": int(selected_group_id), "groups": groups})

@csrf_exempt
def update_attendance(request):
    data = json.loads(request.body)
    for key, status in data.items():
        student_id, lesson_id = map(int, key.split("-"))
        student = get_object_or_404(Student, id=student_id)
        lesson = get_object_or_404(Lesson, id=lesson_id)
        attendance, _ = Attendance.objects.get_or_create(student=student, lesson=lesson)
        attendance.status = status
        attendance.save()
    return JsonResponse({"success": True})

@csrf_exempt
def start_lesson(request):
    lesson = get_object_or_404(Lesson, id=json.loads(request.body)["lesson_id"])
    lesson.closed = False
    lesson.save()
    return JsonResponse({"success": True})

@csrf_exempt
def close_lesson(request):
    lesson = get_object_or_404(Lesson, id=json.loads(request.body)["lesson_id"])
    lesson.closed = True
    lesson.save()
    return JsonResponse({"success": True})
