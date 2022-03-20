from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from .forms import StudentRegistration
from .models import Student
# testing api
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer

# Create your views here.
# Using second method first one is right form.save
def home(r):
    form = StudentRegistration()
    stu = Student.objects.all()
    if r.method == 'POST':
        form = StudentRegistration(r.POST)
        if form.is_valid():
            nm = form.cleaned_data['name']
            rl = form.cleaned_data['roll']
            sl = form.cleaned_data['school']
            reg = Student(name=nm, roll=rl, school=sl)
            reg.save()
            return redirect(home)
    return render(r, 'enroll/home.html', {'form':form, 'stu':stu})

def update(request, pk):
    stu = Student.objects.get(id=pk)
    form = StudentRegistration(instance=stu)
    if request.method == 'POST':
        form = StudentRegistration(request.POST, instance=stu)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'enroll/update.html', {'form':form})


def delete(r, pk):
    if r.method == 'GET':
        pi = Student.objects.get(id=pk)
        pi.delete()
        return redirect('home')

# This is Serializers test to create api

def list_students(request):
    student = Student.objects.all()
    serializer = StudentSerializer(student, many=True)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data)

def student(request, pk):
    stu = Student.objects.get(id=pk)
    serializer = StudentSerializer(stu)
    # json_data = JSONRenderer().render(serializer.data)
    return JsonResponse(serializer.data, safe=False)