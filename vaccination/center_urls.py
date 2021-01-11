from django.urls import path

from vaccination.center_views import IndexView, ViewRequest, ApproveView, ApprovedRequest, AddRequest, RequestStatus

urlpatterns = [
    path('', IndexView.as_view()),
    path('ViewRequest', ViewRequest.as_view()),
    path('ApproveView', ApproveView.as_view()),
    path('ApprovedRequest', ApprovedRequest.as_view()),
    path('AddRequest', AddRequest.as_view()),
    path('RequestStatus', RequestStatus.as_view()),



]

def urls():
    return urlpatterns, 'center', 'center'