from django.db import models

# Create your models here.

class Course(models.Model):
    course_name = models.CharField(max_length=30)
    dur = models.IntegerField()
    fee = models.IntegerField()
    trainer = models.CharField(max_length=40)

    def __str__(self):
        return self.course_name