import os
import sys

# Add the HeartAttack_ML directory to Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'HeartAttack_ML'))

# Set Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'HeartPred.settings')

# Import Django WSGI application
from HeartPred.wsgi import application

# Vercel expects the WSGI app to be named 'app'
app = application
