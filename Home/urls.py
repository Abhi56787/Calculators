from django.contrib import admin
from django.urls import path
from Home import views


urlpatterns = [
    path('', views.index, name='HomePage'),
    path('mon_inv', views.monthly_investment, name='Monthly Investment'),
    path('vis_time', views.vis_time, name='Vision Times'),
    path('step_up_mon_inv', views.step_up_mon_inv, name='Step up Monthly investment'),
    path('vis_time_up', views.vis_time_up, name='Vision Time(Step-up)'),
]
