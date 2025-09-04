from rest_framework import generics
from .models import Patient
from .serializers import PatientSerializer

# GET (list) + POST (create)
class PatientListCreateView(generics.ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

# GET (retrieve), PUT/PATCH (update), DELETE
class PatientDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
