from rest_framework import generics, permissions
from .models import PatientDoctorMapping
from .serializers import PatientDoctorMappingSerializer

class MappingListCreateAPIView(generics.ListCreateAPIView):
    queryset = PatientDoctorMapping.objects.all()
    serializer_class = PatientDoctorMappingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class MappingDetailAPIView(generics.RetrieveDestroyAPIView):
    queryset = PatientDoctorMapping.objects.all()
    serializer_class = PatientDoctorMappingSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = "id"


# Custom: Get all doctors for a patient
from rest_framework.response import Response
from rest_framework.views import APIView

class PatientDoctorsAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, patient_id):
        mappings = PatientDoctorMapping.objects.filter(patient_id=patient_id)
        serializer = PatientDoctorMappingSerializer(mappings, many=True)
        return Response(serializer.data)
