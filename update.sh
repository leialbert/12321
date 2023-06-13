#!/bin/bash

echo "Changing to the correct directory..."
# Change to the directory where your git repository is located
cd /data/v12321
echo "Activating virtual environment..."
source env/bin/activate
# Run git pull
git pull origin main 
# Run any migrations and restart the server
echo "Running migrations..."
python manage.py makemigrations
python manage.py migrate
echo "Collecting static files..."
python manage.py collectstatic
echo "Restarting server..."
systemctl restart gunicorn
echo "Completed."
