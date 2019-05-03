from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from courses import views

router = routers.SimpleRouter()
router.register('courses', views.CourseViewSet)
router.register('reviews', views.ReviewViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('rest_framework.urls',
                              namespace='rest_framework')),  # default endpoint by DRF for login and logout
    path('api/v1/courses/', include(('courses.urls','courses'), namespace='courses')),
    path('api/v2/', include((router.urls, 'router'), namespace='apiv2')),
]
