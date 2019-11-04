from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'wiki'
urlpatterns = [
    path('doc/', views.document_view, name='list'),
    path('create/', views.DocumentCreateView.as_view(), name='create'),
    path('delete/<slug:slug>/', views.DocumentDeleteView.as_view(), name='delete'),
]
