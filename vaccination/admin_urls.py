from django.urls import path

from vaccination.admin_views import IndexView, NewCenterView, ApproveView, RejectView, CenterView, WorkerRegister, \
    WorkerView, ViewChildren, AddEvent, ViewEvents, AddVaccine, ViewAllocation,TakeChildren, RealloRequest, VaccineView,RequestStatus, \
    UpdateReq

urlpatterns = [
    path('', IndexView.as_view()),
    path('newcenter', NewCenterView.as_view()),
    path('approve', ApproveView.as_view()),
    path('reject', RejectView.as_view()),
    path('centerview', CenterView.as_view()),
    path('workerreg', WorkerRegister.as_view()),
    path('workerview', WorkerView.as_view()),
    path('ViewChildren', ViewChildren.as_view()),
    path('TakeChildren', TakeChildren.as_view()),
    path('RealloRequest', RealloRequest.as_view()),
    path('ViewAllocation', ViewAllocation.as_view()),
    path('AddEvent', AddEvent.as_view()),
    path('ViewEvents', ViewEvents.as_view()),
    path('AddVaccine', AddVaccine.as_view()),
    path('VaccineView', VaccineView.as_view()),
    path('RequestStatus', RequestStatus.as_view()),
    path('UpdateReq', UpdateReq.as_view()),

]

def urls():
    return urlpatterns, 'admin', 'admin'