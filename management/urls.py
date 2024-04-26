from django.urls import path
from management.views.kopaliani import *
from management.views.views import *

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
    path('addAssignment/', addAssignment, name='addAssignment'),
    path('studentassignment/', studentassignment, name='studentassignment'),
    path('submitAssignment/<int:assignment_id>/', submitAssignment, name='submitAssignment'),
    path('profAssignment/<int:assignment_id>/', profAssignment, name='profAssignment'),

    # path('myAssighments/', myAssighments, name='myAssighments'),
    path('subject_list/', subject_list, name='subject_list'),
    path('subject_list/<int:subject_id>/', subject_students, name='subject_students')
]