from django.urls import path
from . import views

urlpatterns = [
    path('<int:destination_id>/', views.write_review, name='submit_review'),
]
