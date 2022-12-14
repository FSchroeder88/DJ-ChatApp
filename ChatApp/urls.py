from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls import path, include
from chat.views import chat
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from account.views import (
    register_view,
    login_view,
    logout_view,
    profile_view,
    
)

urlpatterns = [
    path('',  login_view, name ="login"),
    path('admin/', admin.site.urls),
    path('chat/', chat, name ="chat"),
    path('login/', login_view, name ="login"),
    path('logout/', logout_view, name ="logout"),
    path('register/', register_view, name ="register"),
    path('profile/', profile_view, name  ="profile"),
    
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns() 

