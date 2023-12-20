from django.urls import path
from . import views


app_name='site'
urlpatterns=[
    path('',views.Home,name='home'),
    path('details/<int:new1_id>/',views.details,name='details'),
    path('delete/<int:new2_id>/',views.delete,name='delete'),
    path('regnew/',views.Regnew,name='regnew'),
    path('update/<int:new3_id>/',views.update,name='update'),
]