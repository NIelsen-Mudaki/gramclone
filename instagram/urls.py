from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'', views.index, name='index'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^accounts/profile/', views.profile, name='profile'),
    url(r'^upload/', views.upload, name='upload'),
    url(r'^comment/$', views.comment, name='comment'),
    url(r'^login/', views.login(template_name='registration/login.html'), name='login'),
    url(r'^logout/', views.logout(template_name='index.html'), name='logout'),
]
if settings.DEBUG:
	urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) 
