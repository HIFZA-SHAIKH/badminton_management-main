from django.urls import path
from .views import register, user_login, user_logout
from .views import admin_dashboard, player_dashboard, dashboard, home
from .views import add_court, book_court, view_bookings, manage_bookings
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('dashboard/', dashboard, name='dashboard'),
    path('register/', register, name='register'),
    path('', home, name='home'), 
    path('admin-dashboard/', admin_dashboard, name='admin_dashboard'),
    path('player-dashboard/', player_dashboard, name='player_dashboard'),

      # Court Management
    path('add-court/', add_court, name='add_court'),
    path('book-court/', book_court, name='book_court'),
    path('view-bookings/', view_bookings, name='view_bookings'),
    path('manage-bookings/', manage_bookings, name='manage_bookings'),

    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),

    
]
