from django.shortcuts import render , redirect
from django.contrib.auth.models import auth,User
from django.contrib.auth.forms import UserChangeForm
# Create your views here.



def register(request):

    if request.method == 'POST':
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password']
        password2 = request.POST['retypepassword']

        if password1 == password2:

            if User.objects.filter(username=username):
                print("Username Already Taken")
                return redirect("register")
            elif User.objects.filter(email=email):
                print("Email Already Used")
                return redirect("register")
            else:
                user_data = User.objects.create_user(first_name=first_name, last_name=last_name, password=password1,
                                                     email=email, username=username)
                user_data.save()
                print("User Created")

                return redirect("login")
        else:
            print("Password Not matched")
            return redirect("register")


    else:
        return render(request,'register.html')

def login(request):
    if request.method == 'POST':
        user_name= request.POST["username"]
        password = request.POST["password"]

        user_login = auth.authenticate(username=user_name , password = password)

        if user_login is not None:
            auth.login(request,user_login)
            print("User Login")
            return redirect("helloapplication/post")
        else:
            print("Username or Password is invalid")
            return redirect("login")
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect("/")

