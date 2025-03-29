
from django.urls import path
from . import views

#this creates a url config
urlpatterns = [
    path("<int:month>", views.monthly_challenegr_by_number),
    path("<str:month>", views.monthly_challenge, name="month-challenge")
]
