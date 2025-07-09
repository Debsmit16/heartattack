import os
import sys

# Get the directory paths
current_dir = os.path.dirname(__file__)
project_root = os.path.dirname(current_dir)
django_project = os.path.join(project_root, 'HeartAttack_ML')

# Add the HeartAttack_ML directory to Python path
sys.path.insert(0, django_project)
sys.path.insert(0, project_root)

# Set Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'HeartPred.settings')

# Debug: Print paths
print(f"Current dir: {current_dir}")
print(f"Project root: {project_root}")
print(f"Django project: {django_project}")
print(f"Python path: {sys.path[:3]}")

# Import Django WSGI application
from HeartPred.wsgi import application

# Vercel expects the WSGI app to be named 'app'
app = application
