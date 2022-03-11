from django.shortcuts import render,redirect,get_object_or_404
from .models import Image, Profile, Likes, Follow, Comment
from .forms import ProfileForm,CommentForm

# Create your views here.
def index(request):
    title = 'Instagram Clone'
    images = Image.objects.all()
    # comments = Comment.objects.all()

    print(images)
    return render(request, 'index.html', {"title":title,"images":images})

def profile(request):
    current_user = request.user
    profile = Profile.objects.all()
    follower = Follow.objects.filter(user = profile)

    return render(request, 'user.html',{"current_user":current_user,"profile":profile,"follower":follower})

def search_results(request):
    if 'pic' in request.GET and request.GET["pic"]:
        search_term = request.GET.get("pic")
        searched_profiles = Profile.search_profile(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"pics": searched_profiles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

#def comment(request,id):
	
	#post = get_object_or_404(Image,id=id)	
	#current_user = request.user
	#print(post)

	#if request.method == 'POST':
		#form = CommentForm(request.POST)

		#if form.is_valid():
			#comment = form.save(commit=False)
			#comment.user = current_user
			#comment.pic = post
			#comment.save()
			#return redirect('index')
	#else:
		#form = CommentForm()

	#return render(request,'comment.html',{"form":form})