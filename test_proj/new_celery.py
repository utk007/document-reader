from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_proj.settings')
app = Celery('test_proj')
app.config_from_object('django.conf:settings', namespace='CELERY')
#app.auto_discover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def foo(self):
    print('celery working in background')
    print(self.request)
