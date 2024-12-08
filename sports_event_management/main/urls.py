# main/urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('home/', home, name='home'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('admin_dashboard/', admin_dashboard, name='admin_dashboard'),
    path('coach_dashboard/', coach_dashboard, name='coach_dashboard'),
    path('viewer_dashboard/', viewer_dashboard, name='viewer_dashboard'),
    path('know-more/', know_more, name='know_more'),  # Add this line
    path('add-event/', add_event, name='add_event'), 
    path('events/', event_list, name='event_list'), # URL for adding an event
    path('chatbot/', chatbot_view, name='chatbot'),
]