# import module base
from .base import *

# decouple
from decouple import config, Csv

# variables of base
SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', cast=bool)
ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())

# DATABASES = default SQLITE
