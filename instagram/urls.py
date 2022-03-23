from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^$', views.index, name='index'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^accounts/profile/', views.profile, name='profile'),
    url(r'^upload/', views.upload, name='upload'),
    url(r'^comment/(?P<id>[0-9]+)', views.comment, name='comment'),
    url(r'^accounts/login/accounts/register/', views.register),
    url(r'^login/', views.login, name='login'),
    url(r'^logout/', views.logout, name='logout'),
    url(r'^check/', views.checking)
]
if settings.DEBUG:
	urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) 
