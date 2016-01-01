"""source URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from blat import views

urlpatterns = [
    #url(r'^$',views.home,name="homepage"),
    #url(r'^updated_profile/$',views.register_user),
    # url(r'^adduser/$',views.register,name="adduser"),
    url(r'^$',views.IndexView.as_view(),name="homepage"),
    url(r'^(?P<pk>[0-9]+)/$',views.DetailView.as_view(),name='detail'),
    url(r'^my/$',views.MyView.as_view(),name="myview"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$',auth_views.login,name="login"),
    url(r'^logout/$',auth_views.logout,name="logout"),
    url(r'^create/$',views.NewBlatView.as_view(),name="newblat"),
    url(r'^(?P<pk>[0-9]+)/edit/$',views.EditBlatView.as_view(),name='editblat'),
    #url(r'^register/$','register',name='accounts_register'),
    url('^register/', CreateView.as_view(
            template_name='register.html',
            form_class=UserCreationForm,
            success_url='/'
    )),
    url('^accounts/', include('django.contrib.auth.urls')),

    # rest of your URLs as normal


]

