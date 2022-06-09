from django.urls import path
from . import views
from knox import views as knox_views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('get_lecture_subject/',views.get_lecture_subject),
    path('post_lecture/',views.post_lecture),
] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)