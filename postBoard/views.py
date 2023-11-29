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

    # def get(self, request, slug=None, *args, **kwargs):
    #     if slug is not None:
    #         queryset = Post.objects
    #         post = get_object_or_404(queryset, slug=slug)
    #         comments = post.comments.filter(approved=True).order_by('created_on')
    #         like = False
    #         if request.user.is_authenticated and post.likes.filter(id=request.user.id).exists():
    #             liked = True

    #         return render(
    #             request,
    #             'board.html',  
    #             {
    #                 'post': post,
    #                 'comments': comments,
    #                 'liked': liked
    #             },
    #         )
    #     else:
            
    #         posts = Post.objects.all()
    #         return render(
    #             request,
    #             'board.html',  
    #             {
    #                 'posts': posts,
    #             },
    #         )

    # def get(self, request, slug, *args, **kwargs):
    #     queryset: Post.objects
    #     post = get_object_or_404(queryset, slug=slug)
    #     comments = post.comments.filter(approved=True).order_by('created_on')
    #     liked = False
    #     if post.likes.filter(id=self.request.user.id).exists():
    #         liked = True

    #     return render(
    #         request,
    #         'board.html',
    #         {
    #             'post': post,
    #             "comments": comments,
    #             "liked": liked
    #         },
    #     )


    # method to display world_areas and tags lists in post form
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = TAGS
        context['areas'] = WORLD_AREAS
        context['post_form'] = PostForm()
        return context


    #method to post the user post into the database
    def post(self, request, *args, **kwargs):
        post_form = PostForm(data=request.POST)
        
        if post_form.is_valid():
            post_form.instance.author = request.user
            post_form.instance.slug = slugify(post_form.instance.title)
            post_form.save()
        else:
            post_form = PostForm()
        return HttpResponseRedirect(reverse_lazy('post_board'))


class PostLike(View):

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse_lazy('post_board'))