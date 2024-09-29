# settings.py

# Email settings (using Gmail for example)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your_gmail_address@gmail.com'
EMAIL_HOST_PASSWORD = 'your_gmail_password'

DEFAULT_FROM_EMAIL = 'your_gmail_address@gmail.com'
