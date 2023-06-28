from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    capacity = models.IntegerField()

    def __str__(self):
        return self.name

    def spots_available(self):
        registered_count = self.course_registration.all().count()
        return self.capacity - registered_count

    def registered_count(self):
        return self.course_registration.all().count()


class CourseRegistration(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course_registration')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} registered for {self.course}"
