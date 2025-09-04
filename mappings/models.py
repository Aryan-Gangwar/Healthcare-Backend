from django.db import models
from django.conf import settings
from patients.models import Patient
from doctors.models import Doctor

class PatientDoctorMapping(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="doctor_mappings")
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name="patient_mappings")
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.patient.name} assigned to {self.doctor.name}"
