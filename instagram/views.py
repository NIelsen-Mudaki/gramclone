from django.shortcuts import render,redirect,get_object_or_404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .models import Image, Profile, Likes, Follow, Comment
from .forms import *

# Create your views here.
# @login_required(login_url='/accounts/login/')
def index(request):
    title = 'Instagram Clone'
    images = Image.objects.all()
    comments = Comment.objects.all()

    print(images)
    return render(request, 'index.html', {"title":title,"images":images, "comments":comments})

def search_results(request):
    if "image" in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_image(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

def comment(request,id):
	
	post = get_object_or_404(Image,id=id)	
	current_user = request.user
	print(post)

	if request.method == 'POST':
		form = CommentForm(request.POST)

		if form.is_valid():
			comment = form.save(commit=False)
			comment.user = current_user
			comment.pic = post
			comment.save()
			return redirect('index')
	else:
		form = CommentForm()

	return render(request,'comment.html',{"form":form})


def profile(request):
    current_user = request.user
    profiles = Profile.objects.all()
    follower = Follow.objects.filter(user = profiles)

    return render(request, 'user.html',{"current_user":current_user,"profiles":profiles,"follower":follower})

def upload(request):
    current_user = request.user
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.uploaded_by = current_user
            image.save()
            return redirect('/')
    else:
        form = UploadForm()
    return render(request, 'post.html', {'form': form})

def login(request): 
    return render(request, 'registration/login.html')
    
def logout(request):
    logout(request)
    return HttpResponseRedirect('logout_page')