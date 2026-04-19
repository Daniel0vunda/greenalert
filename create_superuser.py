import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'greenalert.settings')
django.setup()

from django.contrib.auth import get_user_model
User = get_user_model()

if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@greenalert.com', 'greenalert2026')
    print("Superuser created")
else:
    print("Superuser already exists")