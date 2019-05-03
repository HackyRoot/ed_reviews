from django.shortcuts import get_object_or_404

from rest_framework import generics
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response

from . import models
from . import serializers


class ListCreateCourse(generics.ListCreateAPIView):
    """
    get: returns a list of courses
    post: create a new course
    """
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer


class RetrieveUpdateDestroyCourse(generics.RetrieveUpdateDestroyAPIView):
    """
    get: return a course based on given pk
    put: update the course
    """
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer


class ListCreateReview(generics.ListCreateAPIView):
    """
    get: returns a list of reviews
    post: create a new review
    """
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer

    def get_queryset(self):
        """
        returns queryset for given course_pk
        """
        return self.queryset.filter(course_id=self.kwargs.get('course_pk'))

    def perform_create(self, serializer):
        """
        Prevent user from giving different course_pk. This method runs right when an object is being created by the view.
        """
        course = get_object_or_404(models.Course,
                                   pk=self.kwargs.get('course_pk'))
        serializer.save(course=course)


class RetrieveUpdateDestroyReview(generics.RetrieveUpdateDestroyAPIView):
    """
    get: return a review for a specific course
    put: update the review
    """
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer

    def get_object(self):
        """
        Returns a review for given course_id

        """
        return get_object_or_404(self.get_queryset(),
                                 course_id=self.kwargs.get('course_pk'),
                                 pk=self.kwargs.get('pk')
                                 ),


class CourseViewSet(viewsets.ModelViewSet):
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer

    @detail_route(methods=['get'])
    def reviews(self, request, pk=None):
        course = self.get_object()
        serializer = serializers.ReviewSerializer(
            course.reviews.all(), many=True)
        return Response(serializer.data)


class ReviewViewSet(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    viewsets.GenericViewSet):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer


