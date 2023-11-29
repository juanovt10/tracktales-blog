from django.shortcuts import render, redirect, get_object_or_404
from django.utils.text import slugify
from django.views import generic, View
from django.views.generic import TemplateView
from .models import Post, TAGS, WORLD_AREAS
from .forms import PostForm
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

def index(request):
    return render(request, 'index.html')

class PostBoard(generic.ListView):
    model = Post
    queryset = Post.objects.filter(approved=True).order_by('-created_on')
    template_name = 'board.html'
    context_object_name = 'posts'

    # method to display world_areas and tags lists in post form
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = TAGS
        context['areas'] = WORLD_AREAS
        context['post_form'] = PostForm()
        return context

    def post(self, request, *args, **kwargs):
        post_form = PostForm(data=request.POST)
        
        if post_form.is_valid():
            post_form.instance.author = request.user
            post_form.instance.slug = slugify(post_form.instance.title)
            post_form.save()
        else:
            post_form = PostForm()
        return HttpResponseRedirect(reverse_lazy('post_board'))
