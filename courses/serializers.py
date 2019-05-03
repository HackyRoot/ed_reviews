from rest_framework import serializers
from . import models


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
            """ 
            write_only means it's written in db while saving the review but doesn't back out when we serializer a 
            review and send it back out.
            """
            'email': {'write_only': True}
        }

        fields = (
            'id',
            'course',
            'name',
            'email',  # Reviewer's email id shouldn't be shared publicly
            'comment',
            'rating',
            'created_at',
        )

        model = models.Review


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'url'
        )
        model = models.Course

"""

Serializer to JSON

>>> from rest_framework.renderers import JSONRenderer
>>> from courses.models import Course
>>> from courses.serializers import CourseSerializer
>>> course = Course.objects.latest('id')

>>> course.title
'Python Collections'

>>> serializer = CourseSerializer(course)
>>> serializer
CourseSerializer(<Course: Python Collections>):
    id = IntegerField(label='ID', read_only=True)
    title = CharField(max_length=255)
    url = URLField(max_length=200, validators=[<UniqueValidator(queryset=Course.objects.all())>])

>>> serializer.data
{'id': 2, 'title': 'Python Collections', 'url': 'https://teamtreehouse.com/library/python-collections'}
>>> JSONRenderer().render(serializer.data)
b'{"id":2,"title":"Python Collections","url":"https://teamtreehouse.com/library/python-collections"}'

here b means byte string

"""