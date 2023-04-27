from django.contrib import admin
from restapi.models import Course
# Register your models here.

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['id','course_name','dur','fee','trainer']
