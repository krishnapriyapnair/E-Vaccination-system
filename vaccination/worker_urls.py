from django.urls import path

from vaccination.worker_views import IndexView, AddChildren, ViewChildren, ViewAllocation

urlpatterns = [
    path('', IndexView.as_view()),
    path('addchildren', AddChildren.as_view()),
    path('ViewChildren', ViewChildren.as_view()),
    path('ViewAllocation', ViewAllocation.as_view()),

]

def urls():
    return urlpatterns, 'worker', 'worker'