from attendance_insight.models import Student


class AttendancePatternGenerator:
    def __init__(self, academic_days):
        self.academic_days = academic_days
        self.all_pattern_list = []
        self.prohibited_patterns = []
        self.recursive_pattern_strategy(self.academic_days, "")
        self.filter_probhited_patterns()

    def recursive_pattern_strategy(self, days, pattern):
        if days == 0:
            self.all_pattern_list.append(pattern)
        else:
            self.recursive_pattern_strategy(days - 1, pattern + 'A')
            self.recursive_pattern_strategy(days - 1, pattern + 'P')

    def filter_probhited_patterns(self):
        self.prohibited_patterns = list(filter(lambda pattern: "AAAA" in pattern, self.all_pattern_list))

    def compute_eligible_ways_to_attend_classes(self):
        eligible_ways_to_attend = []
        for way in list(set(self.all_pattern_list).difference(set(self.prohibited_patterns))):
            eligible_ways_to_attend.append(list(way))
        return eligible_ways_to_attend

    def compute_ways_to_miss_last_day(self):
        last_day_miss_patterns = []
        for way in self.compute_eligible_ways_to_attend_classes():
            if way[-1] == 'A':
                last_day_miss_patterns.append(list(way))
        return last_day_miss_patterns

    def probability_to_miss_class_on_graduation_day(self):
        return f"{len(self.compute_ways_to_miss_last_day())}/{len(self.compute_eligible_ways_to_attend_classes())}"


def save_student_info(name):
    student, created = Student.objects.get_or_create(
        name=name,
        first_name=name,
        last_name=name
    )
    if created:
        student.roll_no = student.id
        student.save(update_fields=['roll_no'])
    return student, student.roll_no
