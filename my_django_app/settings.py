import environ
from decouple import config

# Initialize environment variables
env = environ.Env()
environ.Env.read_env()

# Example of reading database credentials
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASSWORD'),
        'HOST': env('DB_HOST'),
        'PORT': env('DB_PORT', default='5432'),
    }
}

# Example of reading a secret key
SECRET_KEY = env('SECRET_KEY')

# Example of reading Cloudinary credentials
CLOUDINARY = {
    'cloud_name': env('CLOUDINARY_CLOUD_NAME'),
    'api_key': env('CLOUDINARY_API_KEY'),
    'api_secret': env('CLOUDINARY_API_SECRET'),
}

# Example of reading Cloudinary URL
CLOUDINARY_URL = env('CLOUDINARY_URL')

# Example of reading Autodesk credentials
AUTODESK = {
    'client_id': env('AUTODESK_CLIENT_ID'),
    'client_secret': env('AUTODESK_CLIENT_SECRET'),
}

# Example of reading Stripe credentials
STRIPE = {
    'public_key': env('STRIPE_PUBLIC_KEY'),
    'secret_key': env('STRIPE_SECRET_KEY'),
}

# Example of reading Google Maps API key
GOOGLE_MAPS_API_KEY = env('GOOGLE_MAPS_API_KEY')

# Example of reading Mapbox API key
MAPBOX_API_KEY = env('MAPBOX_API_KEY')

# Example of reading Ngrok auth token
NGROK_AUTHTOKEN = env('NGROK_AUTHTOKEN')

# Example of reading OpenAI API key
OPENAI_API_KEY = env('OPENAI_API_KEY')
