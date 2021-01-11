from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
# Create your views here.
from django.contrib.auth.models import User
from django.views.generic import TemplateView

from vaccination.models import User_reg, UserType


class IndexView(TemplateView):
    template_name = 'index.html'

class UserRegister(TemplateView):
    template_name = 'user_reg.html'

    def post(self, request,*args,**kwargs):
        fullname = request.POST['name']
        contact = request.POST['phone']
        email = request.POST['email']
        address = request.POST['addr']

        username = request.POST['Username']

        password = request.POST['Password']
        try:
            user = User.objects._create_user(username=username,password=password,first_name=fullname,email=email,last_name = 0)
            user.save()
            user_info = User_reg()
            user_info.user=user
            user_info.contact = contact
            user_info.address = address

            user_info.save()
            usertype = UserType()
            usertype.user = user
            usertype.type = "center"
            usertype.save()
            messages = "Registration Successfull"
            return render(request,'index.html',{'message':messages})
        except:
            messages = "Enter Another Username"
            return render(request,'index.html',{'message':messages})



class LoginView(TemplateView):
    template_name = 'login.html'

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password= request.POST['password']
        user = authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            if user.last_name == '1':
                if user.is_superuser:
                    return redirect('admin/')
                elif UserType.objects.get(user_id=user.id).type == "worker":
                    return redirect('/worker')
                elif UserType.objects.get(user_id=user.id).type == "user":
                    return redirect('/user')
                else:
                    return redirect('/center')
            else:
                return render(request,'index.html',{'message':" User Account Not Authenticated"})
        else:
            return render(request,'index.html',{'message':"Invalid Username or Password"})
