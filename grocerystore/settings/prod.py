from grocerystore.settings.dev import DEBUG, SECRET_KEY
from .common import *
import dj_database_url

SECRET_KEY = os.environ['SECRET_KEY']

DEBUG = False

ALLOWED_HOSTS = [
    'peaceful-basin-59755.herokuapp.com'
]

DATABASES = {
    'default': dj_database_url.config()
}
