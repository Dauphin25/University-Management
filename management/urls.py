
from django.urls import path
from .views.kopaliani import *
from .views.views import get_students, get_student, get_faculties, get_faculty

urlpatterns = [
    path('', index, name='index'),
    path('professor/', professor, name='professor'),
    path('sabject/', sabject, name='sabject'),
    path('students/', get_students, name='get_students'),
    path('students/<int:pk>/', get_student, name='get_student'),
    path('faculties/', get_faculties, name='get_faculties'),
    path('faculty/<int:pk>/', get_faculty, name='get_faculty'),
    path('user_login/', user_login, name='user_login'),
    path('user_logout/', user_logout, name='user_logout'),
    path('takingsabject/', takingsabject, name='takingsabject'),
]
=======
# management/urls.py
from django.urls import path
from management.views.log_in import login_view

app_name = 'management'
urlpatterns = [
    # Define your URL patterns here
    path('login/', login_view, name='login'),  # Change 'login' to the name of your login URL pattern
    # Other URL patterns
]

