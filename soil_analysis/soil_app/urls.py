from django.urls import path
from soil_app import views

urlpatterns = [
    path('', views.upload_soil_data, name='upload'),
    path('chatbot/', views.chatbot_response, name='chatbot'),
]