from django.urls import path,include
from . import  views
urlpatterns = [
    path('', views.index, name='home'),
    path('logout', views.Userlogout, name='logout'),
    path('profile', views.profile, name='profile'),
    path('login', views.Ulogin, name='login'),
    path('register', views.register, name='register'),
    path('password_change', views.passwordchange, name='password_change'),
    path('password_reset', views.password_reset_request, name="password_reset")
]