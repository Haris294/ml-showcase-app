#!/bin/bash
echo "Setting up ML Algorithms Explorer..."
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser --username admin --email admin@example.com --noinput
echo "Setup complete! Run: cd backend && source venv/bin/activate && python manage.py runserver"
