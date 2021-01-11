from django.urls import path

from vaccination.user_views import IndexView,VaccineStatus, Allocation, ReRequest

urlpatterns = [
    path('', IndexView.as_view()),
    path('VaccineStatus', VaccineStatus.as_view()),
    path('Allocation', Allocation.as_view()),
    path('ReRequest', ReRequest.as_view()),


]

def urls():
    return urlpatterns, 'user', 'user'