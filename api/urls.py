
from django.urls import path
from . import views

urlpatterns = [
    path('',views.getrouter,name="getrouter"),
    path('newapplicationlist/',views.new_application,name="newapplicationlist"),
    path('pendingapplicationlist/',views.pending_application,name="pendingapplicationlist"),
    path('openregistration/<str:id>',views.one_application,name="openregistration"),
    path('api/registration/',views.registration,name="registration"),
    path('recordtrack/',views.recordtrack,name="recordtrack"),
]