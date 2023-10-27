from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from django.views.generic import ListView, DetailView
"""from .models import Post"""


def postList(request):
    return render(request,'blog/post_list.html')



""""class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView): 
    model = Post
    template_name = 'blog/post_detail.html'"""