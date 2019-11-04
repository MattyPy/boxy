from django.shortcuts import render, reverse, redirect
from django.views.generic import CreateView, DeleteView, DetailView

from .models import Document
from .forms import DocumentForm

# Create your views here.


def document_view(request):
    return render(request, 'wiki/document.html', context=None)

class DocumentDetailView(DetailView):
    model = Document


class DocumentCreateView(CreateView):
    model = Document
    form_class = DocumentForm
    success_url = '/wiki/doc/'


class DocumentDeleteView(DeleteView):
    model = Document
    success_url = '/'
