from django.shortcuts import render,redirect
from .models import Image, Profile, Likes, Follow, Comment

# Create your views here.
def index(request):
    title = 'Instagram Clone'
    images = Image.objects.all()
    # comments = Comment.objects.all()

    print(images)
    return render(request, 'index.html', {"title":title,"images":images})
