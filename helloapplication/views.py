from django.shortcuts import render,redirect
from .models import Data,Feedbackpost
from django.contrib.auth.models import auth,User
from django.http import HttpResponse

# Create your views here.

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
    allData = User.objects.all()
    print(allData)
    data=allData
    print(type(data))

    return render(request, "data.html", {"data" : data})


def post(request):
    if 'delete' in request.POST:
        #if request.method == "POST":

        PriKey = str(request.POST.get("indexKey"))
        print(PriKey,"Delete")
        filterData = Feedbackpost.objects.filter(index=PriKey).delete()
        return redirect("post")

        #Allpostfeedback = Feedbackpost.objects.all()
        #return render(request, "post.html",{"Allpostfeedback":Allpostfeedback})

    if 'edit' in request.POST:
        #if request.method == 'POST':

        PriKey = str(request.POST.get("indexKey"))
        updatedtxtfield = str(request.POST.get("editabletxt"))
        filterData = Feedbackpost.objects.get(index=PriKey)
        filterData.txtfield = updatedtxtfield
        filterData.save()
        return redirect("post")

        #Allpostfeedback = Feedbackpost.objects.all()
        #return render(request, "post.html",{"Allpostfeedback":Allpostfeedback})

    if 'search' in request.POST:
        #if request.method == 'POST':

        start = request.POST.get("startingDate")
        end = request.POST.get("endingDate")
        Allpostfeedback = Feedbackpost.objects.filter(date__range=[start, end])
        return render(request, "post.html",{"Allpostfeedback":Allpostfeedback})


    elif request.method == "POST":
        txtfield = str(request.POST.get("posttxt"))
        date = request.POST.get("date")
        time = request.POST.get("time")
        postFeedback = Feedbackpost()
        postFeedback.txtfield=txtfield
        postFeedback.date = date
        postFeedback.time = time
        postFeedback.save()
        return redirect("post")

        #Allpostfeedback=Feedbackpost.objects.all()
        #return render(request, "post.html", {"Allpostfeedback": Allpostfeedback})

    else:
        Allpostfeedback = Feedbackpost.objects.all().order_by('-index')
        #print(Allpostfeedback)
        return render(request,"post.html",{"Allpostfeedback":Allpostfeedback})

