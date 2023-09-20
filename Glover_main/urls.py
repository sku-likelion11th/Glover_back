from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
	path('', main, name='main'),
    # path('student_stamp_status/<str:student_id>/', student_stamp_status, name='student_stamp_status'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)