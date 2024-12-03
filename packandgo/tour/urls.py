from django.urls import path
from .views import create_tour, tour_list, tour_detail, update_tour, delete_tour

urlpatterns = [
    path('', tour_list, name='tour_list'),
    path('create/', create_tour, name='create_tour'),
    path('<int:pk>/', tour_detail, name='tour_detail'),
    path('<int:pk>/edit/', update_tour, name='update_tour'),
    path('<int:pk>/delete/', delete_tour, name='delete_tour'),
]
