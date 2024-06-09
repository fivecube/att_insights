from django.shortcuts import render
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
from attendance_insight.data import AttendanceStatus
from attendance_insight.models import AttendanceTracker, Student
from attendance_insight.tasks import AttendancePatternGenerator, save_student_info


class AttendanceSelectorView(APIView):
    def get(self, request):
        query_data = request.query_params
        academic_days = int(query_data.get('academic_days'))
        apg = AttendancePatternGenerator(academic_days)
        ways_to_attend_classes = apg.compute_eligible_ways_to_attend_classes()
        ways_to_miss_last_day = apg.compute_ways_to_miss_last_day()
        probability_to_miss_class_on_grad_day = apg.probability_to_miss_class_on_graduation_day()
        return Response({
            'success': True,
            'data': {
                "ways_to_attend_classes": {
                    "number_of_ways": len(ways_to_attend_classes),
                    "ways": ways_to_attend_classes
                    },
                "ways_to_miss_last_day": {
                    "number_of_ways": len(ways_to_miss_last_day),
                    "ways": ways_to_miss_last_day
                    },
                "probability_to_miss_class_on_grad_day": probability_to_miss_class_on_grad_day
                }
            })

    def post(self, request):
        data = request.data
        selected_way_to_attend_class = data.get('selected_way_to_attend_class')
        name = data.get('name')
        student = save_student_info(name)
        AttendanceTracker.objects.filter(student=student).delete()
        for day_number_index, day_status in enumerate(selected_way_to_attend_class):
            print(day_status, day_number_index)
            if day_status == 'P':
                status = AttendanceStatus.PRESENT.name
            elif day_status == 'A':
                status = AttendanceStatus.ABSENT.name
            else:
                raise APIException('Incorrect value in status')
            AttendanceTracker.objects.create(
                student=student,
                day_number=day_number_index+1,
                status=status
            )
        return Response({
            'success': True
        })


class AttendanceTrackerDropDownView(APIView):
    def get(self, request):
        students_list = []
        for student in Student.objects.all():
            student_info = {
                "name": student.name,
                "roll_no": student.roll_no
            }
            students_list.append(student_info)
        return Response({
            'success': True,
            'data': students_list})


class AttendanceTrackerView(APIView):
    def get(self, request):
        query_data = request.query_params
        roll_no = int(query_data.get('roll_no'))
        student = Student.objects.get(id=roll_no)
        attendance_data = AttendanceTracker.objects.filter(student_id=roll_no).order_by('day_number')
        way = []
        for day in attendance_data:
            day_status = 'P' if day.status == AttendanceStatus.PRESENT.name else 'A'
            way.append(day_status)
        return Response({
            'success': True,
            'data': {
                "name": student.name,
                "way": way
            }
        })
