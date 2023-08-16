from django.urls import path
from authapp import views

urlpatterns = [
    path('signup/',views.signup,name="signup"),
    path('login/',views.login1,name="login1"),
    path('logout/',views.logout1,name="logout1"),
    
]
