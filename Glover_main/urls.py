from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path('', main, name='main'),
    path('user_page/', main, name='user_page'),
    path('manager_page/', manager_page, name='manager_page'),
    path('stamp_list/', stamp_list, name='stamp_list'),
    path('add_stamp/', add_stamp, name='add_stamp'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)