from django.contrib import admin
from .models import Patient  # Import your Patient model

# Register the model so it appears in the admin
admin.site.register(Patient)

# Register your models here.
