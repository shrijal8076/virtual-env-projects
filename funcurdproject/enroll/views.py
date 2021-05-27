from django.shortcuts import render,HttpResponseRedirect
from .forms import StudentRegistraion
from .models import User
# Create your views here.
def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistraion(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            ps = fm.cleaned_data['password']
            reg = User(name=nm ,email=em,password=ps)
            reg.save()
            fm = StudentRegistraion()

        else:
            fm = StudentRegistraion()
    else:
        fm = StudentRegistraion()

    st = User.objects.all()

    return render(request,'addandshow.html',{'form':fm ,'students':st})

def update(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = StudentRegistraion(request.POST ,instance=pi)
        if fm.is_valid():
          fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm = StudentRegistraion(instance=pi)
    return render(request, 'updatestudent.html',{'form':fm})

def delete(request,id):
    if request.method =='POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')

