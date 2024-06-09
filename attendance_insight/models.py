from django.db import models

from attendance_insight.data import AttendanceStatus


class Student(models.Model):
    name = models.CharField(max_length=256, )
    first_name = models.CharField(max_length=256, null=True, blank=True)
    last_name = models.CharField(max_length=256, null=True, blank=True)
    roll_no = models.CharField(max_length=256, null=True, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class AttendanceTracker(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    day_number = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=64, choices=[(ast.name, ast.name) for ast in AttendanceStatus])

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['student', 'day_number'],
                                    name='unique_status_of_student_on_each_day')
        ]

    def __str__(self):
        return '{}-{}-{}'.format(self.student, self.day_number, self.status)
