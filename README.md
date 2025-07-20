# 🚀 Django Portfolio Website (able)

This is a dynamic Django-based **Portfolio Website** where anyone can upload their personal details, skills, projects, and generate their own online portfolio.

✅ No hardcoding needed.  
✅ Easily able from Django Admin Panel.  
✅ Pre-installed `venv2` included for fast setup.

---

## 💻 How to Run on Your Laptop
This project includes a pre-installed virtual environment (`venv2`), so you don’t need to install Python packages manually. Just follow these steps:

### 1️⃣ Clone the Repository
First, clone this repository to your local machine:
```
git clone https://github.com/Rudra616/portfolio.git

cd portfolio

2️⃣ Activate Pre-installed Virtual Environment
This project includes a venv2 folder with all dependencies already installed.

On Windows:
venv2\Scripts\activate

On macOS/Linux:
source venv2/bin/activate

3️⃣ Create Your Own .env File
In the project root, create a .env file:
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost

# Email Settings
EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-email-password
DEFAULT_FROM_EMAIL=your-email@gmail.com
4️⃣ Run Database Migrations
Apply migrations to set up the database:


python manage.py makemigrations
python manage.py migrate
5️⃣ Collect Static Files (Optional)
If running in production or testing static files:


python manage.py collectstatic
6️⃣ Create Superuser (Optional)
To log into the admin panel and  your portfolio:


python manage.py createsuperuser
7️⃣ Start the Development Server
Run the server:


python manage.py runserver
Open your browser at: http://127.0.0.1:8000


📢 Edit Your Details
Log into the admin panel at http://127.0.0.1:8000/admin
Use your superuser credentials to update:
✅ Personal Info
✅ Skills
✅ Projects
✅ Contact Info



📁 Folder Structure
portfolio/
│
├── manage.py
├── portfolio/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── info/
│   ├── models.py
│   ├── views.py
│   └── ...
├── venv2/                <-- Pre-installed virtual environment
├── .env.example          <-- Example .env file
├── requirements.txt
└── README.md

