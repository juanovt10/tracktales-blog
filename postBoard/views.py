from django.shortcuts import render, redirect, get_object_or_404
from django.utils.text import slugify
from django.views import generic, View
from django.views.generic import TemplateView
from .models import Post, TAGS, WORLD_AREAS, Comment
from .forms import PostForm, CommentForm
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.db.models import Count, Q
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
        context['filter_tags'] = TAGS[1:]
        context['filter_areas'] = WORLD_AREAS[1:]
        context['post_form'] = PostForm()
        context['comment_form'] = CommentForm()

        #create an empty dictionary for the post_comments
        context['post_comments'] = {}

        #populate the dicitonary with the approved comments as value and the post.id as keys
        for post in context['posts']:
            comments = Comment.objects.filter(post=post, approved=True).order_by('created_on')
            context['post_comments'][post.id] = comments
        
        return context


    #method to post the user post into the database and like posts 
    def post(self, request, *args, **kwargs):

        #define post and comment forms
        post_form = PostForm(data=request.POST)
        comment_form = CommentForm(data=request.POST)

        #check if teh post form is valid and post the form the database
        if post_form.is_valid():
            post_form.instance.author = request.user
            post_form.instance.slug = slugify(post_form.instance.title)
            post_form.save()

        #check for the id in the request POST and add or delete likes    
        elif 'blogpost_id_like' in request.POST:
            post_slug = request.POST['blogpost_id_like']
            post = get_object_or_404(Post, slug=post_slug)

            if post.likes.filter(id=request.user.id).exists():
                post.likes.remove(request.user)
            else:
                post.likes.add(request.user)

        #check for the comment form is valid then post the form 
        elif comment_form.is_valid():
            post_slug = request.POST.get('blogpost_id_comment')
            post = get_object_or_404(Post, slug=post_slug)
            comment_form.instance.author = request.user
            comment = comment_form.save(commit=False)   
            comment.post = post
            comment.save()     

        return HttpResponseRedirect(reverse_lazy('post_board'))

    #method to filter posts in post board
    def get_queryset(self):
        #redefine the posts in the post board
        queryset = Post.objects.filter(approved=True).order_by('-created_on')

        #check that the method is GET and define the filters
        if self.request.method == 'GET':
            holiday_types = self.request.GET.getlist('holiday_type')
            world_areas = self.request.GET.getlist('world_area')

            #if teh filters are existent, filter the posts
            if holiday_types:
                queryset = queryset.filter(tags__in=holiday_types).distinct()

            if world_areas:
                queryset = queryset.filter(world_area__in=world_areas).distinct()

        return queryset


# class userProfile(View):

#     def get(self, request, slug)

