from django.contrib import admin
from .models import Image,Profile,Comment,Follow, Unfollow, Likes

# Register your models here.
admin.site.register(Image)
admin.site.register(Profile)
admin.site.register(Comment)
admin.site.register(Follow)
admin.site.register(Unfollow)
admin.site.register(Likes)
