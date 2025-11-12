# Deployment

## Local Development
\`\`\`bash
./setup.sh
cd backend
source venv/bin/activate
python manage.py runserver
\`\`\`

## Production
- Use PostgreSQL instead of SQLite
- Set DEBUG=False
- Collect static files
- Use Gunicorn + Nginx
