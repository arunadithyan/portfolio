from django.urls import path
from portfolio import views

urlpatterns = [
    path('',views.home,name="home"),
    path('about/',views.about,name="about"),
    path('contact/',views.contact1,name="contact1"),
    path('resume/',views.resume,name="resume"),
    path('portfolio/',views.portfolio,name="portfolio"),
    path('services/',views.services,name="services"),
    
]
