from django.urls import path

from . import views

urlpatterns = [
    path('', views.ListCourse.as_view(), name='course_list'),
]