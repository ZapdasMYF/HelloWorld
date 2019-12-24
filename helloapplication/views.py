from django.shortcuts import render
from .models import Data
from django.contrib.auth.models import auth,User

# Create your views here.

from django.http import HttpResponse


def index(request):
    if request.method == "POST":
        lname = str(request.POST.get("lname"))
        fname = str(request.POST.get("fname"))
        username = str(request.POST.get("username"))
        email = str(request.POST.get("email"))
        password = str(request.POST.get("password"))

        obj = Data()
        obj.fname = fname
        obj.lname = lname
        obj.username = username
        obj.email = email
        obj.password=password
        obj.save()

        data = Data.objects.all()
        print(data)
        print(type(data))
        return render(request, "data.html", {"data":data})

    else:

        return render(request,"index.html")

def data(request):
    allData = Data.objects.all()
    print(allData)
    data=allData
    print(type(data))
    return render(request, "data.html", {"data" : data})
