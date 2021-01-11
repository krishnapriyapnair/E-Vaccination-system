from django.views.generic import TemplateView
from vaccination.models import User_reg, Children, Worker_reg, UserType, Allocate
from django.contrib.auth.models import User
from django.shortcuts import render

class IndexView(TemplateView):
    template_name = 'asha_worker/worker_index.html'


class AddChildren(TemplateView):
    template_name = 'asha_worker/add_children.html'

    def get_context_data(self, **kwargs):
         context = super(AddChildren, self).get_context_data(**kwargs)
         id = User_reg.objects.filter(user__last_name='1',user__is_active='1')
         context['id'] = id
         return context

    def post(self, request,*args,**kwargs):
        r = Worker_reg.objects.get(user_id=self.request.user.id)
        fullname = request.POST['name']
        contact = request.POST['contact']

        address = request.POST['address']
        ward = request.POST['ward']
        Disease = request.POST['disease']
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        age = request.POST['age']

        center = request.POST['center']


        p = User_reg.objects.get(pk=center)
        user = User.objects._create_user(username=username,password=password,first_name=fullname,email=email,last_name = 1)
        user.save()
        user_info = Children()

        user_info.c_contact = contact
        user_info.c_address = address
        user_info.ward = ward
        user_info.c_name = fullname
        user_info.status = 'Added'
        user_info.age = age
        user_info.center = p
        user_info.user = user
        user_info.worker = r
        user_info.disease = Disease



        user_info.save()
        usertype = UserType()
        usertype.user = user
        usertype.type = "user"
        usertype.save()

        messages = "Added Successfull"
        return render(request,'asha_worker/worker_index.html',{'message':messages})


class ViewChildren(TemplateView):
    template_name = 'asha_worker/view_children.html'

    def get_context_data(self, **kwargs):
        context = super(ViewChildren,self).get_context_data(**kwargs)
        chil = Children.objects.filter(worker__user_id=self.request.user.id)
        context['chil'] = chil
        return context

class ViewAllocation(TemplateView):
    template_name = 'asha_worker/view_allocate.html'
    def get_context_data(self, **kwargs):
        context = super(ViewAllocation, self).get_context_data(**kwargs)
        id = self.request.GET['c_id']
        context['chil'] = Allocate.objects.filter(children=id)
        return context