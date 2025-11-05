from django.urls import path
from . import views

urlpatterns = [
    path('', views.package_list, name='packages'),
    path('package/<int:package_id>/', views.package_detail, name='package_detail'),
    path('booking/<int:package_id>/', views.booking, name='booking'),
    path('booking-confirmation/<int:booking_id>/', views.booking_confirmation, name='booking_confirmation'),
    path('cancel-booking/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),
    path('my-bookings/', views.my_bookings, name='my_bookings'),
    path('search/', views.search_packages, name='search_packages'),
]
