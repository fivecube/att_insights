
from django.contrib import admin
from django.urls import path, include

from attendance_insight.views import AttendanceSelectorView, AttendanceTrackerDropDownView, AttendanceTrackerView

urlpatterns = [
    path('attendance_selector/', AttendanceSelectorView.as_view(), name='attendance_selector'),
    path('attendance_tracker_dropdown/', AttendanceTrackerDropDownView.as_view(), name='attendance_tracker_dropdown'),
    path('attendance_tracker/', AttendanceTrackerView.as_view(), name='attendance_tracker'),
]
