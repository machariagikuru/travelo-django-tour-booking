from django.urls import path
from . import views

urlpatterns = [
    path('<int:destination_id>/', views.book_trip, name='book_trip'),
]
