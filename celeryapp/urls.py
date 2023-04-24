
from django.urls import path
from celeryapp import views

urlpatterns = [
    path('',views.testView,name="testview"),
]