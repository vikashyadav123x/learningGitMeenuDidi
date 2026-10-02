from django.http import HttpResponse


def home(request):
    return HttpResponse(
        "Online Examination Portal<br>"
        '<a href="/exam/?subject=Python&duration=60">Online Exam</a><br>'
        '<a href="/exam/Pythoon/">Exam Name</a><br>'
        '<a href="/student/2024">Student ID</a><br>'
        '<a href="/result/?roll=202&semester=8">Result</a><br>'
        '<a href="/hallticket/123456/">Hall Ticket</a>'
    )


def online_exam(request):
    subject = request.GET.get("subject", "")
    duration = request.GET.get("duration", "")
    return HttpResponse(f"subject:{subject} | Duration:{duration} Minutes.")


def exam(request, exam_name):
    return HttpResponse(f"Exam Name:{exam_name}")


def student(request, student_id):
    return HttpResponse(f"Student ID:{student_id}")


def result(request):
    roll = request.GET.get("roll", "")
    semester = request.GET.get("semester", "")
    return HttpResponse(f"Roll:{roll} | Semester:{semester}")


def hall_ticket(request, hall_ticket_number):
    return HttpResponse(f"Hall Ticket:{hall_ticket_number}")
