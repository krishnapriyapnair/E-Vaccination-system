from django.views.generic import TemplateView
from vaccination.models import User_reg, UserType, Worker_reg, Children, Event, Vaccine, Request, Allocate
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views import View
import datetime
from django.shortcuts import redirect

class IndexView(TemplateView):
    template_name = 'admin/admin_index.html'




class NewCenterView(TemplateView):
    template_name = 'admin/new_center.html'

    def get_context_data(self, **kwargs):
        context = super(NewCenterView,self).get_context_data(**kwargs)
        center = User_reg.objects.filter(user__last_name='0',user__is_staff='0')
        context['center'] = center
        return context

class ApproveView(View):
    def dispatch(self, request, *args, **kwargs):

        id = request.GET['id']
        user = User.objects.get(pk=id)
        user.last_name='1'
        user.save()
        return render(request,'admin/admin_index.html',{'message':" Account Approved"})


class RejectView(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        user = User.objects.get(pk=id)
        user.last_name='1'
        user.is_active='0'
        user.save()
        return render(request,'admin/admin_index.html',{'message':"Account Removed"})

class CenterView(TemplateView):
    template_name = 'admin/view_centers.html'

    def get_context_data(self, **kwargs):
        context = super(CenterView,self).get_context_data(**kwargs)
        center = User_reg.objects.filter(user__last_name='1',user__is_staff='0',user__is_active='1')
        context['center'] = center
        return context



class WorkerRegister(TemplateView):
    template_name = 'admin/add_worker.html'

    def post(self, request,*args,**kwargs):
        fullname = request.POST['name']
        contact = request.POST['phone']
        email = request.POST['email']
        address = request.POST['addr']
        ward = request.POST['ward']

        worker = Worker_reg.objects.filter(ward=ward).count()
        if (worker>0):
            return render(request,'admin/admin_index.html',{'message':"This ward have already a asha worker!"})
        else:

            username = request.POST['Username']

            password = request.POST['Password']
            try:
                user = User.objects._create_user(username=username,password=password,first_name=fullname,email=email,last_name ='1')
                user.save()
                user_info = Worker_reg()
                user_info.user=user
                user_info.contact = contact
                user_info.address = address
                user_info.ward = ward

                user_info.save()
                usertype = UserType()
                usertype.user = user
                usertype.type = "worker"
                usertype.save()
                messages = "Added Successfull"
                return render(request,'admin/admin_index.html',{'message':messages})
            except:
                messages = "Enter Another Username"
                return render(request,'admin/admin_index.html',{'message':messages})


class WorkerView(TemplateView):
    template_name = 'admin/view_worker.html'

    def get_context_data(self, **kwargs):
        context = super(WorkerView,self).get_context_data(**kwargs)
        worker = Worker_reg.objects.filter(user__last_name='1',user__is_staff='0',user__is_active='1')
        context['worker'] = worker
        return context


class ViewChildren(TemplateView):
    template_name = 'admin/view_children.html'

    def get_context_data(self, **kwargs):
        context = super(ViewChildren,self).get_context_data(**kwargs)

        va = Vaccine.objects.all()
        chl = Children.objects.all()
        for c in chl:

            for v in va:
                today = datetime.date.today()
                a = c.age
                s = c.id

                date_time_obj = datetime.datetime.strptime(a, '%Y-%m-%d')
                ag = today.year - date_time_obj.year
                p = v.period
                vid = v.id
                vac = Vaccine.objects.filter(period=ag)


                context['va'] = vac




                al = Allocate.objects.filter(vaccine=vid,children=s,tstatus='Vaccine Tacked').count()
                if al<=0:
                    if int(p) == int(ag):
                        cl = Children.objects.get(pk=s)
                        cl.status = 'Added'


                        cl.save()


        chil = Children.objects.filter(status='Added')
        context['chil'] = chil

        return context


    def post(self, request,*args,**kwargs):
        message = request.POST['message']
        chil = request.POST['chil']
        vacci = request.POST['vacci']
        center = request.POST['center']
        altim = request.POST['altim']
        aldat = request.POST['aldat']

        children = Children.objects.get(pk=chil)
        vaccina = Vaccine.objects.get(pk=vacci)
        centers = User_reg.objects.get(pk=center)



        co = Request.objects.filter(center_id=center,vacci_id=vacci,rstatus='Request').count()
        if co>0:
            return render(request,'admin/admin_index.html',{'message':"No Vaccine In This Center"})
        else:
            # a = Allocate.objects.filter(children=children,vaccine=vaccina).count()
            # if a>0:
            #     return render(request,'admin/admin_index.html',{'message':"Already Added"})
            # else:
                m = Allocate()
                m.message = message
                m.alstatus = 'Allocated'
                m.aldate = aldat
                m.altime = altim
                m.center = centers
                m.children = children
                m.vaccine = vaccina
                m.tstatus = 'Not'
                m.save()
                messages = "Allocated"
                return render(request,'admin/admin_index.html',{'message':messages})

class TakeChildren(TemplateView):
    template_name = 'admin/taked_child.html'

    def get_context_data(self, **kwargs):
        context = super(TakeChildren,self).get_context_data(**kwargs)
        chil = Children.objects.all()
        va = Vaccine.objects.all()
        context['chil'] = chil
        context['va'] = va
        return context

class RealloRequest(TemplateView):
    template_name = 'admin/reqchild.html'

    def get_context_data(self, **kwargs):
        context = super(RealloRequest,self).get_context_data(**kwargs)
        chil = Children.objects.filter(status='Req')
        va = Vaccine.objects.all()
        context['chil'] = chil
        context['va'] = va
        return context
    def post(self, request,*args,**kwargs):
        message = request.POST['message']
        chil = request.POST['chil']
        vacci = request.POST['vacci']
        center = request.POST['center']
        altim = request.POST['altim']
        aldat = request.POST['aldat']

        children = Children.objects.get(pk=chil)

        vaccina = Vaccine.objects.get(pk=vacci)
        centers = User_reg.objects.get(pk=center)
        alo = Allocate.objects.get(children=children)
        alo.delete()



        co = Request.objects.filter(center_id=center,vacci_id=vacci,rstatus='Request').count()
        if co>0:
            return render(request,'admin/admin_index.html',{'message':"No Vaccine In This Center"})
        else:
            # a = Allocate.objects.filter(children=children,vaccine=vaccina).count()
            # if a>0:
            #     return render(request,'admin/admin_index.html',{'message':"Already Added"})
            # else:
                m = Allocate()
                m.message = message
                m.alstatus = 'Allocated'
                m.aldate = aldat
                m.altime = altim
                m.center = centers
                m.children = children
                m.vaccine = vaccina
                m.tstatus = 'Not'
                m.save()
                messages = "Allocated"
                return render(request,'admin/admin_index.html',{'message':messages})


class ViewAllocation(TemplateView):
    template_name = 'admin/view_allocate.html'
    def get_context_data(self, **kwargs):
        context = super(ViewAllocation, self).get_context_data(**kwargs)
        id = self.request.GET['c_id']
        context['chil'] = Allocate.objects.filter(children=id)
        return context




class AddEvent(TemplateView):
    template_name = 'admin/add_event.html'

    def post(self, request,*args,**kwargs):
        name = request.POST['name']
        image = request.FILES['image']
        desc = request.POST['descr']
        edate = request.POST['edate']
        etime = request.POST['etime']

        event  = Event()
        event.ename = name

        event.image = image
        event.descri = desc
        event.eventdate = edate
        event.eventtime = etime
        event.save()
        return  render(request,'admin/admin_index.html',{'message':"Event Added"})

class ViewEvents(TemplateView):
    template_name = 'admin/view_event.html'

    def get_context_data(self, **kwargs):
        context = super(ViewEvents,self).get_context_data(**kwargs)
        event = Event.objects.all()
        context['event'] = event
        return context

class AddVaccine(TemplateView):
    template_name = 'admin/add_vaccine.html'

    def post(self, request,*args,**kwargs):
        name = request.POST['name']

        desc = request.POST['descr']
        period = request.POST['period']

        qty = request.POST['qty']

        v = Vaccine()
        v.vname = name
        v.vdescri = desc
        v.vqty = qty
        v.period = period
        v.save()
        return  render(request,'admin/admin_index.html',{'message':"Vaccine Added"})

class VaccineView(TemplateView):
    template_name = 'admin/view_vaccine.html'

    def get_context_data(self, **kwargs):
        context = super(VaccineView,self).get_context_data(**kwargs)
        va = Vaccine.objects.all()
        context['va'] = va
        return context

    def post(self, request,*args,**kwargs):
        qty = request.POST['qty']

        vid = request.POST['vid']

        v =Vaccine.objects.get(pk=vid)
        cqty = v.vqty
        tqty = int(cqty)+int(qty)
        v.vqty = tqty


        v.save()
        return  render(request,'admin/admin_index.html',{'message':"Vaccine Updated"})



class RequestStatus(TemplateView):
    template_name = 'admin/request_status.html'

    def get_context_data(self, **kwargs):
        context = super(RequestStatus,self).get_context_data(**kwargs)
        va = Request.objects.all()
        context['va'] = va
        return context

class UpdateReq(View):
    def dispatch(self, request, *args, **kwargs):
        qt = request.GET['qt']
        id = request.GET['id']
        va = request.GET['va']

        vc = Vaccine.objects.get(pk=va)
        v = vc.vqty
        if qt>v:
            return render(request,'admin/admin_index.html',{'message':"Please Update vaccine."})
        else:
            r = Request.objects.get(pk=id)
            r.rstatus = 'Allocated'
            r.save()
            vc.vqty = int(v)-int(qt)
            vc.save()

        return render(request,'admin/admin_index.html',{'message':"Vaccine  allocated"})
