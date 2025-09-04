🏥 Healthcare API Backend
A Django REST Framework based backend for managing patients, doctors, and patient-doctor mappings with authentication & secure data handling in PostgreSQL.

🚀 Features
✅ User Registration & Login (JWT Authentication)

✅ Patient Management (Add, Update, Delete, View)

✅ Doctor Management (Add, Update, Delete, View)

✅ Patient–Doctor Mapping (Assign / Remove doctors from patients)

✅ API Documentation using Swagger UI

✅ Admin Panel for managing all models

🛠️ Tech Stack
Backend: Django, Django REST Framework

Database: PostgreSQL

Authentication: JWT (SimpleJWT)

API Docs: drf-yasg (Swagger)

📂 Project Structure
healtcare-backend/
│── accounts/       # User registration & authentication
│── patients/       # Patient management
│── doctors/        # Doctor management
│── mappings/       # Patient-Doctor mappings
│── config/         # Main project config & URLs
│── static/         # CSS, JS, images
│── templates/      # Landing page
│── requirements.txt
│── manage.py


⚡ Setup Instructions
1️⃣ Clone the repo
git clone https://github.com/your-username/healthcare-backend.git
cd healthcare-backend
2️⃣ Create Virtual Environment & Install Dependencies
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

pip install -r requirements.txt
3️⃣ Setup Database (PostgreSQL)
Update settings.py with your PostgreSQL credentials:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'healthcare_db',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5433',
    }
}
Run migrations:

python manage.py makemigrations
python manage.py migrate
4️⃣ Create Superuser
python manage.py createsuperuser
5️⃣ Run Server
python manage.py runserver
📌 API Endpoints
🔑 Authentication
POST /api/auth/register/ → Register new user

POST /api/token/ → Login (get JWT token)

POST /api/token/refresh/ → Refresh token

🧑 Patients
POST /api/patients/ → Add patient

GET /api/patients/ → List all patients

GET /api/patients/<id>/ → Patient details

PUT /api/patients/<id>/ → Update patient

DELETE /api/patients/<id>/ → Delete patient

👨‍⚕️ Doctors
POST /api/doctors/ → Add doctor

GET /api/doctors/ → List doctors

GET /api/doctors/<id>/ → Doctor details

PUT /api/doctors/<id>/ → Update doctor

DELETE /api/doctors/<id>/ → Delete doctor

🔗 Patient–Doctor Mapping
POST /api/mappings/ → Assign doctor to patient

GET /api/mappings/ → List all mappings

GET /api/mappings/<patient_id>/ → Get doctors of a patient

DELETE /api/mappings/<id>/ → Remove doctor from patient

📖 API Documentation
Swagger UI available at → http://127.0.0.1:8000/api/docs/

🛡️ License
This project is licensed under the MIT License.



#Project Screenshots

# Landing Page

<img width="1917" height="1016" alt="Screenshot 2025-09-04 202500" src="https://github.com/user-attachments/assets/429773b1-f72a-4795-9eb9-52caf976b914" />

# Admin Panel (Users & Authentication)

<img width="1919" height="1014" alt="Screenshot 2025-09-04 202546" src="https://github.com/user-attachments/assets/c5846838-985f-4c24-97d4-bc010e40eb5c" />

# Doctors Section in Admin Panel

<img width="1919" height="1014" alt="Screenshot 2025-09-04 202600" src="https://github.com/user-attachments/assets/756f78b7-5ca5-4ba3-9754-d0bc703e1028" />

# API Documentation

<img width="1917" height="1019" alt="Screenshot 2025-09-04 202615" src="https://github.com/user-attachments/assets/d27fb194-0e1b-4d77-957e-892bd07fee23" />

# Code Structure

<img width="1919" height="1018" alt="Screenshot 2025-09-04 203313" src="https://github.com/user-attachments/assets/69f38409-33a1-4ab5-b516-7e8b1686fd18" />
