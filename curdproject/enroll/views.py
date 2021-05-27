from django.shortcuts import render,HttpResponseRedirect
from .forms import StudentRegistraion
from .models import User
from django.views.generic.base import TemplateView,RedirectView
from django.views import View
class UserAndShowView(TemplateView):

    template_name = 'addandshow.html'

    def get_context_data(self,*args,**kwargs):
        context = super().get_context_data(**kwargs)
        fm = StudentRegistraion()
        st = User.objects.all()
        context = {'form':fm ,'students':st}
        return context
    def post(self,request):
        fm = StudentRegistraion(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            ps = fm.cleaned_data['password']
            reg = User(name=nm, email=em, password=ps)
            reg.save()
            fm = StudentRegistraion()
            return HttpResponseRedirect('/')





# Create your views here.
"""def add_show(request):
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
"""
class UserUpdateView(View):
    template_name = 'updatestudent.html'

    def get(self,request,id):
        pi = User.objects.get(pk=id)
        fm = StudentRegistraion(instance=pi)
        return render(request, 'updatestudent.html',{'form':fm})
    def post(self,request,id):
        pi = User.objects.get(pk=id)
        fm = StudentRegistraion(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()

            fm = StudentRegistraion()
        return  render(request, 'updatestudent.html',{'form':fm})

    """
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
    """


class UserDeleteView(RedirectView):
    url='/'
    """def post(self,request,id):
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')"""
    def get_redirect_url(self,*args,**kwargs):
        del_id = kwargs['id']
        User.objects.get(pk=del_id).delete()
        return super().get_redirect_url(*args,**kwargs)



"""def delete(request,id):
    if request.method =='POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')

"""