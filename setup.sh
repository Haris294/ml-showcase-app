#!/bin/bash

echo "Setting up ML Algorithms Explorer..."

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed"
    exit 1
fi

cd backend

# Create virtual environment
python3 -m venv venv

# Activate virtual environment  
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Setup database
python manage.py makemigrations
python manage.py migrate

# Create admin user
python manage.py createsuperuser --username admin --email admin@example.com --noinput
echo "from django.contrib.auth import get_user_model; User = get_user_model(); user = User.objects.get(username='admin'); user.set_password('admin123'); user.save()" | python manage.py shell

echo "Setup complete!"
echo "Start server: cd backend && source venv/bin/activate && python manage.py runserver"
