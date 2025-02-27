from django.db import models

class Mentor(models.Model):
    phone_number = models.CharField(max_length=15, unique=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Student(models.Model):
    phone_number = models.CharField(max_length=15, unique=True)
    name = models.CharField(max_length=100)
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    lesson_number = models.IntegerField()  # 1 to 12 lessons
    present = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student.name} - Lesson {self.lesson_number} - {'Present' if self.present else 'Absent'}"
