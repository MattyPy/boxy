from django.shortcuts import render

# Create your views here.


def document_view(request):
    return render(request, 'wiki/document.html', context=None)
