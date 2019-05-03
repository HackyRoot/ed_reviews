from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from . import models
from . import serializers


class ListCreateCourse(APIView):
    def get(self, request, format=None):
        """
        Returns a list of courses
        Responses only to the get request
        """
        courses = models.Course.objects.all()
        serializer = serializers.CourseSerializer(courses, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        """
        Takes data from post request, check if it's valid and save it to database.
        Works almost as same as model form
        Responses only to the post request
        """
        serializer = serializers.CourseSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

