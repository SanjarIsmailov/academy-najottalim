from django.db import models

class Group(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20, unique=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="students")

    def __str__(self):
        return self.name + " " + self.phone_number

class Lesson(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="lessons")
    date = models.DateField()
    number = models.IntegerField()  # Lesson number (1-12)
    closed = models.BooleanField(default=False)  # Lock attendance when closed

    def __str__(self):
        return f"{self.group.name} | Lesson {self.number}"

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="attendances")
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name="attendances")
    status = models.BooleanField(default=False)  # True = Present, False = Absent

    class Meta:
        unique_together = ('student', 'lesson')  # Ensure no duplicate attendance per lesson
