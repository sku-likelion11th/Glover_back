from django.urls import path
from .views import *
from .views import info_stamp
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path('', main, name='main'),
    path('user_page/', main, name='user_page'),
    path('manager_page/', manager_page, name='manager_page'),
    path('stamp_list/', stamp_list, name='stamp_list'),
    path('add_stamp/', add_stamp, name='add_stamp'),
    path('user_check/',user_check,name='user_check'),
    path('edit_stamp/<str:event_name>/', edit_stamp, name='edit_stamp'),
    path('delete_stamp/<str:event_name>/', delete_stamp, name='delete_stamp'),
    path('edit_X_check/', edit_X_check, name='edit_X_check'),
    path('edit_save_check/', edit_save_check, name='edit_save_check'),
    path('info_stamp/<str:event_name>/', info_stamp, name='info_stamp'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)