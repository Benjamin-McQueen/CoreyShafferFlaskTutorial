import os

class Config:
    SECRET_KEY = 'erfderfmcgirf'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    #MAIL_USE_SSL = True
    MAIL_USERNAME = 'BenaSPACE.TESTING@gmail.com'
    MAIL_PASSWORD = 'trivial reoccupy caloric disregard igloo ranch banner'