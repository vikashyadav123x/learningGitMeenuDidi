from django.urls import path, re_path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("exam/", views.online_exam, name="online_exam"),
    path("exam/<str:exam_name>/", views.exam, name="exam"),
    path("student/<int:student_id>", views.student, name="student"),
    path("result/", views.result, name="result"),
    re_path(r"^hallticket/(?P<hall_ticket_number>\d{6})/$", views.hall_ticket, name="hall_ticket"),
]
