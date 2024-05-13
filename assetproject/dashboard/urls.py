from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required 

urlpatterns = [
    path('dashboard/', login_required(views.index), name='dashboard-index'),
    path('staff/', views.staff, name='dashboard-staff'),
    path('product/', views.product, name='dashboard-product'),
    path('order/', views.order, name='dashboard-order'),
]