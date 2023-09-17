from django.urls import path, include
from .views import *




urlpatterns = [
	path('', main, name='main'),
 	path('user_page/', user_page, name='user_page'),
    path('manager_page/', manager_page, name='manager_page'),
]