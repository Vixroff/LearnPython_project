import os

from dotenv import load_dotenv

basedir = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config(object):
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'DataBase.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    YANDEX_API_KEY_MAP = os.getenv('YANDEX_API_KEY_MAP')
    TGBOT_TOKEN = os.getenv('TGBOT_TOKEN')
    CHAT_ID = os.getenv('TGBOT_CHAT_ID')
