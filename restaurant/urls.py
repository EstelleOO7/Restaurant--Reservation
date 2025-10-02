from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('book/', views.book, name="book"),
    path('home/', views.home, name="home"),  
    path('menu/', views.menu, name="menu"),
    path('menu_item/<int:pk>', views.display_menu_item, name="menu_item"),

    # reservation dashboard
    path('dashboard/', views.reservation_dashboard, name='reservation_dashboard'),
    path('booking/<int:booking_id>/approve/', views.approve_booking, name='approve_booking'),
    path('booking/<int:booking_id>/cancel/', views.cancel_booking, name='cancel_booking'),
    path('booking/<int:booking_id>/assign/', views.assign_booking, name='assign_booking'),
    path("assign/<int:pk>/", views.assign_reservation, name="assign_reservation"),

    # authentication
    path('login/', auth_views.LoginView.as_view(template_name='restaurant/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    
    # assign-reservation
    # path('assign/<int:pk>/', views.assign_reservation, name='assign_reservation')
]
