from django.urls import path
from .views.kopaliani import *

urlpatterns = [
    path('', index, name='index'),
    path('professor/', professor, name='professor'),
    path('sabject/', sabject, name='sabject'),
    path('takingsabject/', takingsabject, name='takingsabject'),
    path('user_login/', user_login, name='user_login'),
    path('user_logout/', user_logout, name='user_logout'),
    # path('professor/', professor, name='professor'),

]