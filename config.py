import os

class Config(object):
    SECRET_KEY = ''
    RECAPTCHA_USE_SSL = False
    RECAPTCHA_PUBLIC_KEY = '' # Obtain from google recaptcha service
    RECAPTCHA_PRIVATE_KEY = ''
    RECAPTCHA_OPTIONS = {'theme': 'white'}
