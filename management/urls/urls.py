from django.urls import path
from management.views.views import get_student, get_students, get_faculty, get_faculties
app_name = 'management'
urlpatterns = [
    path('students/', get_students, name='get_students'),
    path('students/<int:pk>/', get_student, name='get_student'),
    path('faculties/', get_faculties, name='get_faculties'),
    path('faculty/<int:pk>/', get_faculty, name='get_faculty'),
]
