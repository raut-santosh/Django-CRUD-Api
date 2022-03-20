from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Student
from api.serializers import StudentSerializers
from rest_framework.renderers import JSONRenderer

# Create your views here.
def details(request, pk):
    stu = Student.objects.get(id=pk)
    serializer = StudentSerializers(stu)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data)

def all_info(request):
    stu = Student.objects.all()
    serializer = StudentSerializers(stu, many=True)
    # json_data = JSONRenderer().render(serializer.data)
    return JsonResponse(serializer.data, safe=False)