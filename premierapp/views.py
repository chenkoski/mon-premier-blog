# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Post
from django.shortcuts import render
from django.utils import timezone

# Create your views here.
from django.http import HttpResponse

def hello(request, number):
   text = "<h1>welcome to my app number %s!</h1>"% number
   return HttpResponse(text)

#def post_list(request):
 #   return render(request, 'premierapp/mon_site/index.html', {})
def mon_cv(request):
    return render(request, 'premierapp/mon_site/Mon_CV.html', {})

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'premierapp/mon_site/post_list.html', {'posts': posts})

