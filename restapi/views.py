from django.shortcuts import render
from restapi.models import Course
from restapi.serializers import CourseSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse,JsonResponse
import io
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
# Create your views here.

@method_decorator(csrf_exempt,name='dispatch')
class CourseAPI(View):
    def get(self,request,*args,**kwargs):
        json_data = request.body
        streamdata = io.BytesIO(json_data)
        pydata = JSONParser().parse(streamdata)
        id = pydata.get('id',None)  
        if id is not None:
            course = Course.objects.get(id=id)
            serializerdata = CourseSerializer(course)
            json_data = JSONRenderer().render(serializerdata.data)
            return HttpResponse(json_data,content_type='application/json')
        else:
            course = Course.objects.all()
            serializerdata = CourseSerializer(course,many=True)
            json_data = JSONRenderer().render(serializerdata.data)
            return HttpResponse(json_data,content_type='application/json')

    def post(self,request,*args,**kwargs): 
        json_data = request.body
        streamdata = io.BytesIO(json_data)
        pydata = JSONParser().parse(streamdata)
        serializerdata = CourseSerializer(data=pydata)
        if serializerdata.is_valid():
            serializerdata.save()
            res = {'msg':'Record Inserted Successfully'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data = JSONRenderer().render(serializerdata.errors)
        return HttpResponse(json_data,content_type='application/json')
    
    
    def put(self,request,*args,**kwargs):
        json_data = request.body
        streamdata = io.BytesIO(json_data)
        pydata = JSONParser().parse(streamdata)
        id = pydata.get('id')
        course = Course.objects.get(id=id)
        serializerdata = CourseSerializer(course,data=pydata,partial=True)
        if serializerdata.is_valid():
            serializerdata.save()
            resp = {'msg':'One Record Updated successfully!!'}
            json_data = JSONRenderer().render(resp)
            return HttpResponse(json_data,content_type='application/json')
        json_data = JSONRenderer().render(serializerdata.errors)
        return HttpResponse(json_data,content_type='application/json')
    
    def delete(self,request,*args,**kwargs):
        json_data = request.body
        streamdata = io.BytesIO(json_data)
        pydata = JSONParser().parse(streamdata)
        id = pydata.get('id')
        course = Course.objects.get(id=id)
        course.delete()
        resp = {'msg':'One Record Deleted!!'}
        json_data = JSONRenderer().render(resp)
        return HttpResponse(json_data,content_type='application/json')



# @csrf_exempt
# def courseapi(request):
#     if request.method == 'GET':
#         json_data = request.body
#         streamdata = io.BytesIO(json_data)
#         pydata = JSONParser().parse(streamdata)
#         id = pydata.get('id',None)
#         if id is not None:
#             course = Course.objects.get(id=id)
#             serializerdata = CourseSerializer(course)
#             json_data = JSONRenderer().render(serializerdata.data)
#             return HttpResponse(json_data,content_type='application/json')
#         else:
#             course = Course.objects.all()
#             serializerdata = CourseSerializer(course,many=True)
#             json_data = JSONRenderer().render(serializerdata.data)
#             return HttpResponse(json_data,content_type='application/json')
    
#     if request.method == 'POST':
#         json_data = request.body
#         streamdata = io.BytesIO(json_data)
#         pydata = JSONParser().parse(streamdata)
#         serializerdata = CourseSerializer(data=pydata)
#         if serializerdata.is_valid():
#             serializerdata.save()
#             res = {'msg':'Record Inserted Successfully'}
#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data,content_type='application/json')
#         json_data = JSONRenderer().render(serializerdata.errors)
#         return HttpResponse(json_data,content_type='application/json')
    
#     if request.method == 'PUT':
#         json_data = request.body
#         streamdata = io.BytesIO(json_data)
#         pydata = JSONParser().parse(streamdata)
#         id = pydata.get('id')
#         course = Course.objects.get(id=id)
#         serializerdata = CourseSerializer(course,data=pydata,partial=True)
#         if serializerdata.is_valid():
#             serializerdata.save()
#             resp = {'msg':'One Record Updated successfully!!'}
#             json_data = JSONRenderer().render(resp)
#             return HttpResponse(json_data,content_type='application/json')
#         json_data = JSONRenderer().render(serializerdata.errors)
#         return HttpResponse(json_data,content_type='application/json')
    
#     if request.method == 'DELETE':
#         json_data = request.body
#         streamdata = io.BytesIO(json_data)
#         pydata = JSONParser().parse(streamdata)
#         id = pydata.get('id')
#         course = Course.objects.get(id=id)
#         course.delete()
#         resp = {'msg':'One Record Deleted!!'}
#         json_data = JSONRenderer().render(resp)
#         return HttpResponse(json_data,content_type='application/json')



# @csrf_exempt
# def newcourse(request):
#     if request.method == 'POST':
#         json_data = request.body
#         streamdata = io.BytesIO(json_data)
#         pydata = JSONParser().parse(streamdata)
#         serializerdata = CourseSerializer(data=pydata)
#         if serializerdata.is_valid():
#             serializerdata.save()
#             resp = {'msg':'Data Inserted Successfully!!'}
#             json_data = JSONRenderer().render(resp)
#             return HttpResponse(json_data,content_type='application/json')
#         json_data = JSONRenderer().render(serializerdata.errors)
#         return HttpResponse(json_data,content_type='applications/json')
    

def index(request):
    context = {'msg':'This is Index Page'}
    return render(request,'restapi/index.html',context)

# def coursedata(request,id=None):
#     if id is None:
#         course = Course.objects.all()
#         serializer_data = CourseSerializer(course,many=True)
#     else:
#         course = Course.objects.get(id=id)
#         serializer_data = CourseSerializer(course)
#     json_data = JSONRenderer().render(serializer_data.data)
#     return HttpResponse(json_data,content_type='application/json')

def coursedata(request,id=None):
    if id is None:
        course = Course.objects.all()
        serializer_data = CourseSerializer(course,many=True)
    else:
        course = Course.objects.get(id=id)
        serializer_data = CourseSerializer(course)
    return JsonResponse(serializer_data.data,safe=False)



# def coursedata1(request):
#     course = Course.objects.get(id=1)
#     serializer_data = CourseSerializer(course)
#     json_data = JSONRenderer().render(serializer_data.data)
#     return HttpResponse(json_data,content_type='application/json')

# def coursedata2(request,id):
#     course = Course.objects.get(id=id)
#     serializer_data = CourseSerializer(course)
#     json_data = JSONRenderer().render(serializer_data.data)
#     return HttpResponse(json_data,content_type='application/json')
