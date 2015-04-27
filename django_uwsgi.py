# coding: utf-8
import os
import sys

sys.setdefaultencoding('utf8')
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
sys.path.append("/opt/tiaozy")
os.environ.setdefault("DJANGO_SETTINGS_MODULE","tiaozy.settings")

from django.core.handlers.wsgi import WSGIHandler
application = WSGIHandler()