import os

class Config:
    # VULNERABILITY 1: Hardcoded secret key & AWS credential
    SECRET_KEY = "flask_prod_super_secret_key_99887766"
    AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
    
    # VULNERABILITY 2: Debug mode enabled in production config
    DEBUG = True
    DATABASE_URI = os.getenv("DATABASE_URI", "sqlite:///enterprise_users.db")