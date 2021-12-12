from django.shortcuts import render
from .models import SocialNetworks

# Create your views here.
def social_networks(request):
    social = SocialNetworks.objects.all()
    return render(request, 'core/base.html', {'social': social})


def index(request):
    return render(request, 'core/home.html')


def blog(request):
    return render(request, 'core/blog.html')


def contact(request):
    return render(request, 'core/contact.html')