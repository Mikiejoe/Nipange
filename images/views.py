from django.shortcuts import render
from .models import Profile

# Create your views here.
def image(request ,img):
    image = Profile.objects.get(image=img)
    return render(image)