import os
import sys
from django.core.wsgi import get_wsgi_application

# Add current working directory to Python module search path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BookApp.settings')

application = get_wsgi_application()

# Required entrypoint variable for Vercel Serverless Functions
app = application