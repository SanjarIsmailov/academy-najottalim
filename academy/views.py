from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Group, Student, Lesson, Attendance

from django.contrib.auth.decorators import login_required

@login_required
def attendance_page(request):
    # Get groups where the logged-in user is the mentor
    user_email = request.user.email
    mentor_groups = Group.objects.filter(mentorGmail=user_email)

    selected_group_id = request.GET.get("group_id")

    # If user is not a mentor of any group, return an empty response
    if not mentor_groups.exists():
        return render(request, "attendance.html",
                      {"students": [], "lessons": [], "attendance_data": {}, "selected_group_id": None, "groups": []})

    # If no specific group is selected, default to the first group
    if not selected_group_id:
        selected_group_id = mentor_groups.first().id

    # Ensure the selected group belongs to the mentor
    selected_group = mentor_groups.filter(id=selected_group_id).first()
    if not selected_group:
        return render(request, "attendance.html",
                      {"students": [], "lessons": [], "attendance_data": {}, "selected_group_id": None,
                       "groups": mentor_groups})

    # Get students and lessons for the selected group
    students = Student.objects.filter(group=selected_group)
    lessons = Lesson.objects.filter(group=selected_group)

    # Build attendance data
    attendance_data = {student.id: {lesson.id: False for lesson in lessons} for student in students}
    for attendance in Attendance.objects.filter(student__group=selected_group):
        attendance_data[attendance.student.id][attendance.lesson.id] = attendance.status

    return render(request, "attendance.html", {
        "students": students,
        "lessons": lessons,
        "attendance_data": attendance_data,
        "selected_group_id": selected_group.id,
        "groups": mentor_groups
    })


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
