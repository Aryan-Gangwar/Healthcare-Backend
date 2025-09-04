from django.urls import path
from .views import DoctorListCreateAPIView, DoctorDetailAPIView

urlpatterns = [
    path('', DoctorListCreateAPIView.as_view(), name='doctor-list'),
    path('<int:pk>/', DoctorDetailAPIView.as_view(), name='doctor-detail'),
]
