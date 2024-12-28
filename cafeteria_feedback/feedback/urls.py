from django.urls import path
from . import views

urlpatterns = [
    path('', views.starting_page, name='starting_page'),  
    path('feedback/', views.feedback_view, name='feedback_form'),
    path('thank-you/', views.thank_you, name='thank_you'),
]
