from django.contrib import admin

# Register your models here.
from attendance_insight.models import AttendanceTracker, Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'first_name',
        'last_name',
        'roll_no',
        'active'
    ]
    search_fields = [
        'name'
    ]


@admin.register(AttendanceTracker)
class AttendanceTrackerAdmin(admin.ModelAdmin):
    list_display = [
        'student',
        'day_number',
        'status'
    ]
    autocomplete_fields = ['student']
