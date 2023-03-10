from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('load-excel/', views.load_excel, name='load_excel'),
    path('upload-excel/', views.upload_excel, name='upload_excel'),
]
