from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('captcha/', include('captcha.urls')),
   path('', user_views.home, name='home'),]
