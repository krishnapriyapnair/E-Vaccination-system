from django.views.generic import TemplateView, View
from vaccination.models import Children, Allocate
from django.shortcuts import render


class IndexView(TemplateView):
    template_name = 'user/user_index.html'

class VaccineStatus(TemplateView):
    template_name = 'user/vaccin_status.html'

    def get_context_data(self, **kwargs):
        context = super(VaccineStatus,self).get_context_data(**kwargs)
        chil = Children.objects.filter(user_id=self.request.user.id)
        context['chil'] = chil
        return context

class Allocation(TemplateView):
    template_name = 'user/view_allocation.html'

    def get_context_data(self, **kwargs):
        context = super(Allocation,self).get_context_data(**kwargs)
        chil = Allocate.objects.filter(children__user_id=self.request.user.id)
        context['chil'] = chil
        return context

class ReRequest(View):
    def dispatch(self, request, *args, **kwargs):

        user = Children.objects.get(user_id=self.request.user.id)
        user.status = 'Req'
        user.save()
        return render(request,'user/user_index.html',{'message':"Requested To Reallocate."})