from django.urls import path
from .views import import_logs

urlpatterns = [
    path('import_logs/', import_logs, name='import_logs'),
]