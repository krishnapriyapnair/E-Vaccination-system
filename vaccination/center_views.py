from django.views.generic import TemplateView, View
from vaccination.models import Children, Allocate, Vaccine, Request, User_reg
from django.shortcuts import render
import  datetime

class IndexView(TemplateView):
    template_name = 'center/center_index.html'

class ViewRequest(TemplateView):
    template_name = 'center/view_request.html'

    def get_context_data(self, **kwargs):
        context = super(ViewRequest,self).get_context_data(**kwargs)
        chil = Allocate.objects.filter(center__user_id=self.request.user.id,alstatus='Allocated')
        context['chil'] = chil
        return context


class ApprovedRequest(TemplateView):
    template_name = 'center/approve_req.html'

    def get_context_data(self, **kwargs):
        context = super(ApprovedRequest,self).get_context_data(**kwargs)
        chil = Allocate.objects.filter(center__user_id=self.request.user.id,alstatus='Approve')
        context['chil'] = chil
        return context
    def post(self, request,*args,**kwargs):
        sta = request.POST['sta']
        pid = request.POST['pid']
        cid = request.POST['cid']
        vid = request.POST['vid']

        v = Vaccine.objects.get(pk=vid)
        vq = v.vqty

        k = Children.objects.get(pk=cid)
        if sta == 'Vaccine Tacked':
            k.status = 'Taked'
            v.vqty = int(vq)-1
            v.save()
        k.save()


        event  = Allocate.objects.get(pk=pid)
        event.tstatus = sta
        event.alstatus = 'Reject'
        event.save()
        return  render(request,'center/center_index.html',{'message':"Updated"})

class ApproveView(View):
    def dispatch(self, request, *args, **kwargs):

        id = request.GET['id']
        user = Allocate.objects.get(pk=id)
        user.alstatus = 'Approve'
        user.save()
        return render(request,'center/center_index.html',{'message':" Request Approved"})


class AddRequest(TemplateView):
    template_name = 'center/request_vaccine.html'

    def get_context_data(self, **kwargs):
        context = super(AddRequest,self).get_context_data(**kwargs)
        va = Vaccine.objects.all()
        context['va'] = va
        return context

    def post(self, request,*args,**kwargs):
        qty = request.POST['qty']
        vac = request.POST['vac']

        today = datetime.date.today()
        v = Vaccine.objects.get(pk=vac)

        ce = User_reg.objects.get(user_id=self.request.user.id)

        r = Request()
        r.rdate = today
        r.rqty = qty
        r.rstatus = 'Request'
        r.center_id = ce
        r.vacci = v

        r.save()

        return  render(request,'center/center_index.html',{'message':"Requested"})


class RequestStatus(TemplateView):
    template_name = 'center/request_status.html'

    def get_context_data(self, **kwargs):
        context = super(RequestStatus,self).get_context_data(**kwargs)
        va = Request.objects.filter(center_id__user_id=self.request.user.id)
        context['va'] = va
        return context
