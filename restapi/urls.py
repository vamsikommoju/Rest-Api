from django.urls import path
from restapi import views

app_name = 'restapi'

urlpatterns = [
    path('',views.index,name='restapi'),
    # path('coursedata',views.coursedata,name='coursedata'),
    # path('coursedata/<int:id>',views.coursedata,name='coursedata2'),
    # path('newcourse',views.newcourse,name='newcourse'),
    path('courseapi',views.CourseAPI.as_view(),name='courseapi'),
    path('courseapi/<int:id>',views.CourseAPI.as_view(),name='newcourseapi'),
]