from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # 사용자 페이지
	path('', main, name='main'),
    path('search/', main, name='search'),
    
    # 관리자 페이지
    path('manager_page/', a_main, name='manager_page'),
    path('stamp_list/', stamp_list, name='stamp_list'),
    path('add_stamp/', add_stamp, name='add_stamp'),
    path('user_check/',user_check,name='user_check'),
    path('edit_stamp/<str:event_name>/', edit_stamp, name='edit_stamp'),
    path('delete_stamp/<str:event_name>/', delete_stamp, name='delete_stamp'),
    
    # 
    path('introduce/', introduce, name='introduce'),
    path('makers/', makers, name='makers'),
    # path('edit_X_check/', edit_X_check, name='edit_X_check'),
    # path('edit_save_check/', edit_save_check, name='edit_save_check'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)