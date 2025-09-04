from django.urls import path
# from .views import (
#     PatientDoctorMappingListCreateAPIView,
#     PatientDoctorMappingDetailAPIView,
#     PatientDoctorsAPIView,
# )

# urlpatterns = [
#     path('', PatientDoctorMappingListCreateAPIView.as_view(), name='mapping-list'),
#     path('<int:pk>/', PatientDoctorMappingDetailAPIView.as_view(), name='mapping-detail'),
#     path('patient/<int:patient_id>/', PatientDoctorsAPIView.as_view(), name='mapping-by-patient'),
# ]

from .views import MappingListCreateAPIView, MappingDetailAPIView, PatientDoctorsAPIView

urlpatterns = [
    path('', MappingListCreateAPIView.as_view(), name="mapping-list-create"),
    path('<int:id>/', MappingDetailAPIView.as_view(), name="mapping-detail"),
    path('<int:patient_id>/doctors/', PatientDoctorsAPIView.as_view(), name="patient-doctors"),
]
