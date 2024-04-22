from django.urls import path
from .views.kopaliani import *

urlpatterns = [
    path('', index, name='index'),
    path('professor/', professor, name='professor'),
    path('sabject/', sabject, name='sabject'),
    # path('professor/', professor, name='professor'),
    # path('professor/', professor, name='professor'),

]