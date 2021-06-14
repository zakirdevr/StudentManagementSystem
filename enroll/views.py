from enroll.models import User
from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
# Create your views here.

#Create and GET Data
def add_show(request):
    if request.method=='POST':
        fm=StudentRegistration(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pw=fm.cleaned_data['password']
            reg=User(name=nm,email=em, password=pw)
            reg.save()
            fm=StudentRegistration()
    else:
        fm=StudentRegistration()
    stud=User.objects.all()

    return render(request, "enroll/addAndShow.html", {"form":fm, "stu":stud})

#Update Data
def update_data(request, id):
    if request.method=='POST':
        dataForUpdate=User.objects.get(pk=id)
        fm=StudentRegistration(request.POST, instance=dataForUpdate)
        if fm.is_valid():
            fm.save()
    else:
        dataForUpdate=User.objects.get(pk=id)
        fm=StudentRegistration(instance=dataForUpdate)
    return render(request, "enroll/updateStudent.html", {"form":fm})

#Delete Data
def delete_data(request, id):
    if request.method=='POST':
        dataForDelete=User.objects.get(pk=id)
        dataForDelete.delete()
        return HttpResponseRedirect("/")