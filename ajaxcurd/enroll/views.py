from django.shortcuts import render
from .forms import StudentRegistration
from . models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def home(request):
    fm = StudentRegistration()
    stud = User.objects.all()
    return render(request, 'enroll/home.html', {'form':fm,'stu':stud})
@csrf_exempt
def datasave(request):
    if request.method =="POST":
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            name = request.POST['name']
            email = request.POST['email']
            password = request.POST['password']
            ins = User(name=name,email=email,password=password)
            ins.save()
            stud = User.objects.values()
            print(stud)
            student_data = list(stud)

            return JsonResponse({'status':'Save','student_data':student_data})
        else:
            return JsonResponse({'status': 0})

