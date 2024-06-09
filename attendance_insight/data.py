import enum


class AttendanceStatus(enum.Enum):
    PRESENT = enum.auto()
    ABSENT = enum.auto()