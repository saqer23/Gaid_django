from django.urls import path
from . import views
from knox import views as knox_views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('login/', views.login_api),
    path('user/', views.get_user_data),
    path('update_profile_data/',views.update_profile_data),

    path('logout/', knox_views.LogoutView.as_view()),
    path('logoutall/', knox_views.LogoutAllView.as_view()),
]+ static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)