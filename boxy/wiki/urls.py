from django.conf.urls import url
from django.urls import path

from .views import document_view

app_name = 'wiki'
urlpatterns = [
    path('doc/', document_view, name='list')
]
