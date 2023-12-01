from django.shortcuts import render, redirect, get_object_or_404
from django.utils.text import slugify
from django.views import generic, View
from django.views.generic import TemplateView
from .models import Post, TAGS, WORLD_AREAS
from .forms import PostForm, CommentForm
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.db.models import Count
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

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
        context['comment_form'] = CommentForm()
        return context


    #method to post the user post into the database and like posts 
    def post(self, request, *args, **kwargs):
        post_form = PostForm(data=request.POST)
        comment_form = CommentForm(data=request.POST)

        if post_form.is_valid():
            post_form.instance.author = request.user
            post_form.instance.slug = slugify(post_form.instance.title)
            post_form.save()
        elif 'blogpost_id_like' in request.POST:
            post_slug = request.POST['blogpost_id_like']
            post = get_object_or_404(Post, slug=post_slug)

            if post.likes.filter(id=request.user.id).exists():
                post.likes.remove(request.user)
            else:
                post.likes.add(request.user)
        elif comment_form.is_valid():
            post_slug = request.POST.get('blogpost_id_comment')
            post = get_object_or_404(Post, slug=post_slug)

            comment_form.instance.author = request.user
            comment = comment_form.save(commit=False)   
            comment.post = post
            comment.save()     
        
        return HttpResponseRedirect(reverse_lazy('post_board'))
