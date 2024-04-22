from django.urls import path
from .views.kopaliani import *
from .views.views import get_students, get_student, get_faculties, get_faculty
app_name = "management"
urlpatterns = [
    path('', index, name='index'),
    path('professor/', professor, name='professor'),
    path('sabject/', sabject, name='sabject'),
    path('students/', get_students, name='get_students'),
    path('students/<int:pk>/', get_student, name='get_student'),
    path('faculties/', get_faculties, name='get_faculties'),
    path('faculty/<int:pk>/', get_faculty, name='get_faculty'),
]