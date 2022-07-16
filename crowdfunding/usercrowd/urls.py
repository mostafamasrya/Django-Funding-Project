
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('register/', register_user, name = 'register'),
    path('login/', login, name = 'login'),
    path('logout/', logout, name = 'logout'),
    path('active/<id>/', activeEmail, name='active'),
    path('profile/' , profile , name='profile'),
    path('editprofile/', editProfile, name='editprofile'),
    path('deleteprofile/', deleteprofile, name='deleteprofile'),

]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)