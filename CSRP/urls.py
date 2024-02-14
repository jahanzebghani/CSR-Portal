from django import views
from django.urls import path
from CSRP import views

urlpatterns = [
    path('', views.home, name="CSRP-home"),
    path('home/', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('contactus/', views.contactus, name="contactus"),
    path('portal/', views.portal, name="portal"),
    path('register/', views.Register, name="register"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path("requistionportal/", views.addrequistion, name="Addrequistion"),
    path('requistionform/', views.Requistionform, name="requistionform"),
    path("electricalrequistionform/", views.electricalrequistionform, name="electricalrequistionform"),
    path("requistiondetails/", views.requistiondetails, name="requistiondetails"),
    path("updatesection/", views.update, name="updatesection"),
    path('delete/<int:requistionid>/', views.delete, name='delete'),
    path('logsheetdetails/', views.logsheetdetails, name='logsheetdetails'),
#    path('comments/<int:requistionid>/', views.comments, name='comments'),
    path('feedbackform/', views.feedbackform, name='feedbackform'),
    path('feedbacksdetails/', views.feedbacksdetails, name='feedbacksdetails')
]

