import os

# Set the secret key for the Flask app and configure the SQLAlchemy database
SECRET_KEY = os.environ.get('SECRET_KEY') or 'my-secret-key'
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///blog.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
