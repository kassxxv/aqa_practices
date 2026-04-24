import sys
import os
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))

os.environ.setdefault('POSTGRES_USER', os.getenv('DB_USER', 'postgres'))
os.environ.setdefault('POSTGRES_PASSWORD', os.getenv('DB_PASSWORD', 'postgres'))
os.environ.setdefault('POSTGRES_HOST', os.getenv('DB_HOST', 'localhost'))
os.environ.setdefault('POSTGRES_DB', os.getenv('DB_NAME', 'postgres'))

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lesson_29'))
