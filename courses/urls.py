from django.urls import path

from . import views

urlpatterns = [
    path('', views.ListCreateCourse.as_view(), name='course_list'),
    path('<pk>/', views.RetrieveUpdateDestroyCourse.as_view(), name='course_detail'),
    path('<course_pk>/reviews/', views.ListCreateReview.as_view(), name='review_list'),
    path('<course_pk>/reviews/<pk>/', views.RetrieveUpdateDestroyReview.as_view(), name='review_detail'),
]