from django.http import HttpResponse
from .models import Teacher


def teachers_list(request):
    teachers = Teacher.objects.all()
    teacher_list = "\n".join(
        [
            f"First name: {teacher.first_name}, Last name: {teacher.last_name}, "
            f"Subject: {teacher.subject}; "
            for teacher in teachers
        ]
    )
    return HttpResponse(teacher_list)
