from django.shortcuts import render

# Create your views here.


def add_subscription(request):
    return render(request, 'core/add_subscription.html')
