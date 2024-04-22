# management/urls.py
from django.urls import path
from management.views.log_in import login_view

app_name = 'management'
urlpatterns = [
    # Define your URL patterns here
    path('login/', login_view, name='login'),  # Change 'login' to the name of your login URL pattern
    # Other URL patterns
]
