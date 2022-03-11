from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Image(models.Model):
	pic = models.ImageField(upload_to = "images/",null = True)
	user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
	pic_name = models.CharField(max_length = 30,null = True)
	likes = models.IntegerField(default=0)
	pic_caption = models.TextField(null = True, blank=True)
	pub_date = models.DateTimeField(auto_now_add=True,null=True)
	comments = models.IntegerField(default=0)


	def __str__(self):
		return self.pic_name

	def delete_image(self):
		self.delete()

	def save_image(self):
		self.save()

	def update_caption(self,new_caption):
		self.pic_caption = new_caption
		self.save()


	@classmethod
	def get_image_by_user(cls,id):
		sent_image = Image.objects.filter(user_id=id)
		return sent_image

	@classmethod
	def get_image_by_id(cls,id):
		get_image = Image.objects.get(id = id)
		return  get_image

	class Meta:
		ordering = ['-pub_date']


	def __str__(self):
		return self.user.username

	def save_profile(self):
		self.save()

	@classmethod
	def search_image(cls,search_term):
		get_images = cls.objects.filter(first_name__icontains = search_term)
		return get_images

class Profile(models.Model):
	username = models.CharField(default='User',max_length=30)
	profile_pic = models.ImageField(upload_to = "profile/",null=True)
	bio = models.TextField(default='',blank = True)
	first_name = models.CharField(max_length =30)
	last_name = models.CharField(max_length =30)

	def __str__(self):
		return self.username

	def delete_profile(self):
		self.delete()

	def save_profile(self):
		self.save()

	@classmethod
	def search_profile(cls,search_term):
		got_profiles = cls.objects.filter(first_name__icontains = search_term)
		return got_profiles

class Comment(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, null= True)
	image = models.ForeignKey(Image, on_delete=models.CASCADE, null= True,related_name='comment')
	comment= models.TextField( blank=True)
	
	def __str__(self):
		return self.comment


	def delete_comment(self):
		self.delete()

	def save_comment(self):
		self.save()

class Follow(models.Model):
	user = models.ForeignKey(Profile, on_delete=models.CASCADE,null=True)
	follower = models.ForeignKey(User, on_delete=models.CASCADE,null=True)

	def __int__(self):
		return self.name

	def save_follower(self):
		self.save()

	def delete_follower(self):
		self.save()

class Unfollow(models.Model):
	user = models.ForeignKey(Profile,on_delete=models.CASCADE,null=True)
	follower = models.ForeignKey(User,on_delete=models.CASCADE,null=True)

	def __int__(self):
		return self.name

class Likes(models.Model):
	user = models.ForeignKey(Profile,on_delete=models.CASCADE,null=True)


	def __int__(self):
		return self.name

	def unlike(self):
		self.delete()

	def save_like(self):
		self.save() 