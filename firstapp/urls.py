
from django.urls import  path
from .import views

urlpatterns = [
    path('',views.index,name='index'),
     path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('registration/', views.registration_form, name='registration_form'),
    path('success',views.success,name='success'),
]
