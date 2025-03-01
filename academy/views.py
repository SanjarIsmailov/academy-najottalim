from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Student, Lesson, Attendance, Group

def attendance_page(request):
    selected_group_id = request.GET.get("group_id")

    groups = Group.objects.all()

    if not selected_group_id:
        return render(request, "attendance.html", {
            "students": [],
            "lessons": [],
            "attendance_data": {},
            "selected_group_id": None,
            "groups": groups,
        })

    students = Student.objects.filter(group_id=selected_group_id)
    lessons = Lesson.objects.filter(group_id=selected_group_id)

    # Build attendance dictionary
    attendance_data = {
        student.id: {lesson.id: False for lesson in lessons} for student in students
    }

    for attendance in Attendance.objects.filter(student__group_id=selected_group_id):
        attendance_data[attendance.student.id][attendance.lesson.id] = attendance.status

    return render(request, "attendance.html", {
        "students": students,
        "lessons": lessons,
        "attendance_data": attendance_data,
        "selected_group_id": int(selected_group_id),
        "groups": groups,
    })


from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Student, Lesson, Attendance

from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Student, Lesson, Attendance

@csrf_exempt
def update_attendance(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)

            if not data:
                return JsonResponse({"success": False, "error": "Empty data received"}, status=400)

            for key, status in data.items():
                student_id, lesson_id = map(int, key.split("-"))
                student = get_object_or_404(Student, id=student_id)
                lesson = get_object_or_404(Lesson, id=lesson_id)

                attendance, created = Attendance.objects.get_or_create(student=student, lesson=lesson)
                attendance.status = status
                attendance.save()

            return JsonResponse({"success": True})
        except json.JSONDecodeError:
            return JsonResponse({"success": False, "error": "Invalid JSON format"}, status=400)
        except Exception as e:
            return JsonResponse({"success": False, "error": str(e)}, status=500)

    return JsonResponse({"success": False, "error": "Invalid request method"}, status=405)
