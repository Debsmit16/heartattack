#!/bin/bash

# Install dependencies
pip install -r requirements.txt

# Navigate to Django project directory
cd HeartAttack_ML

# Collect static files
python manage.py collectstatic --noinput --clear
