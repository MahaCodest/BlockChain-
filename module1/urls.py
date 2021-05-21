from django.urls import path

from .import views

urlpatterns = [

    path("register", views.register, name="register"),
    path("login", views.login, name="login"),
    path("Upload", views.Upload, name="Upload"),
    path("ipfs", views.ipfs, name="ipfs"),


  ]

