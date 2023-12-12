from django.shortcuts import render, redirect, get_object_or_404
from django.utils.text import slugify
from django.views import generic, View
from django.views.generic import TemplateView, FormView
from .models import Post, TAGS, WORLD_AREAS, Comment, UserProfile, ContactInfo
from .forms import PostForm, CommentForm, ProfileForm, EditPostForm, ContactUsForm, UserDeleteForm
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.db.models import Count, Q
from django.views.decorators.http import require_POST
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib import messages

def index(request):
    return render(request, 'index.html')


def about_us(request):
    return render(request, 'aboutus.html')


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
        context['edit_post_form'] = EditPostForm()

        #create an empty dictionary for the post_comments
        context['post_comments'] = {}

        #populate the dicitonary with the approved comments as value and the post.id as keys
        for post in context['posts']:
            comments = Comment.objects.filter(post=post, approved=True).order_by('created_on')
            context['post_comments'][post.id] = comments
            

        return context    

    #method to post the user post into the database and like posts 
    def post(self, request, *args, **kwargs):

        #define context
        post_form = PostForm(data=request.POST)
        comment_form = CommentForm(data=request.POST)
        edit_post_form = EditPostForm(data=request.POST)
        posts = Post.objects.filter(approved=True).order_by('-created_on')
        post_comments = {}
        for post in posts:
            comments = Comment.objects.filter(post=post, approved=True).order_by('created_on')
            post_comments[post.id] = comments

        #check for the id in the request POST and add or delete likes    
        if 'blogpost_id_like' in request.POST:
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
            messages.success(request, 'Your comment has been recorded and is awaiting for approval, this will take a couple of minutes.')

        #method to edit posts
        elif 'edit_post_id' in request.POST:
            post_slug = request.POST['edit_post_id']
            post = get_object_or_404(Post, slug=post_slug)
            post.approved = False
            edit_form = EditPostForm(instance=post, data=request.POST) 
            if edit_form.is_valid():
                edit_form.save()
                messages.success(request, 'Your post has been edited and is awaiting for approval, this will take a couple of minutes.')
            else:
                print("Edit Form Errors:", edit_form.errors)
                return render(request,
                'board.html', {
                    'post_form': post_form,
                    'comment_form': comment_form,
                    'edit_post_form': edit_form,
                    'tags': TAGS,
                    'areas': WORLD_AREAS,
                    'filter_tags': TAGS[1:],
                    'filter_areas': WORLD_AREAS[1:],
                    'posts': posts,
                    'post_comments': post_comments,
                })

        else: 
            #check if teh post form is valid and post the form the database
            if post_form.is_valid():
                post_form.instance.author = request.user
                post_form.instance.slug = slugify(post_form.instance.title)
                post_form.save()
                messages.success(request, 'Thank you! Your post is awaiting for approval, this will take a couple of minutes.')
            else: 
                return render(request,
                'board.html', {
                    'post_form': post_form,
                    'comment_form': comment_form,
                    'edit_post_form': edit_post_form,
                    'tags': TAGS,
                    'areas': WORLD_AREAS,
                    'filter_tags': TAGS[1:],
                    'filter_areas': WORLD_AREAS[1:],
                    'posts': posts,
                    'post_comments': post_comments,
                })

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
        

class DeletePostView(View):
    def post(self, request, *args, **kwargs):
        print("Delete is being triggered")
        post_slug = request.POST.get('delete_post_id')
        print(post_slug)
        post = get_object_or_404(Post, slug=post_slug)
        print(post)
        post.delete()
        return redirect('post_board')


class CreateProfile(generic.ListView):
    model = UserProfile
    template_name = 'createprofile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = TAGS
        context['areas'] = WORLD_AREAS
        context['profile_form'] = ProfileForm()

        return context

    def post(self, request, username, *args, **kwargs):
        print("Entering post method")
        profile_instance = request.user.userprofile
        profile_form = ProfileForm(data=request.POST, instance=profile_instance)

        print(profile_instance)

        if profile_form.is_valid():
            print("Form is valid")
            profile_form.save()
            messages.success(request, f'{username}, you have successfully created your profile!')
            return HttpResponseRedirect(reverse_lazy('profile_detail', kwargs={'username': username}))
        else:
            return render(request,
            'createprofile.html', {
                'tags': TAGS,
                'areas': WORLD_AREAS,
                'profile_form': profile_form
            })


class ProfileDetail(generic.DetailView):
    model = UserProfile
    template_name = 'userprofile.html'
    context_object_name = 'profile_users'
    slug_field = 'username'
    slug_url_kwarg = 'username'

    def get_object(self, queryset=None):
        username = self.kwargs.get('username')
        return get_object_or_404(User, username=username).userprofile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = TAGS
        context['areas'] = WORLD_AREAS
        context['profile_form'] = ProfileForm()

        user_profile = self.get_object()
        context['user_posts'] = Post.objects.filter(author=user_profile.username)
        context['post_comments'] = {}

        for post in context['user_posts']:
            comments = Comment.objects.filter(post=post, approved=True).order_by('created_on')
            context['post_comments'][post.id] = comments

        profile_instance = user_profile
        context['profile_form'] = ProfileForm(instance=profile_instance)
        context['user_profile'] = user_profile

        context['delete_form'] = UserDeleteForm()
        return context

    def post(self, request, username, *args, **kwargs):
        print("Entering post method")
        post_form = PostForm(data=request.POST)
        delete_form = UserDeleteForm(data=request.POST)
        comment_form = CommentForm(data=request.POST)
        edit_post_form = EditPostForm(data=request.POST)
        user_profile = self.get_object()
        posts = Post.objects.filter(author=user_profile.username)
        profile_instance = user_profile
        profile_form = ProfileForm(data=request.POST, instance=profile_instance)
        post_comments = {}
        for post in posts:
            comments = Comment.objects.filter(post=post, approved=True).order_by('created_on')
            post_comments[post.id] = comments

        print(profile_instance)

        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Your profile has been successfully updated!')
            return HttpResponseRedirect(reverse_lazy('profile_detail', kwargs={'username': username}))

        elif 'delete_user_id' in request.POST:
                print("Entering delete user method")
                app_user = request.user
                username = user_profile.username
                database_user = get_object_or_404(UserProfile, username=username)
                print(database_user)
                print(app_user)
                logout(request)
                database_user.delete()
                app_user.delete()
                messages.success(request, f"Account {username} has been successfully deleted")
                return HttpResponseRedirect(reverse_lazy('post_board'))
        else:
            print("Form is not valid")
            return render(
                request, 
                'userprofile.html', {
                'username': self.kwargs['username'],
                'user_profile': user_profile,
                'post_form': post_form,
                'comment_form': comment_form,
                'edit_post_form': edit_post_form,
                'profile_form': profile_form,
                'tags': TAGS,
                'areas': WORLD_AREAS,
                'posts': posts,
                'post_comments': post_comments,                
                })



class ContactUs(FormView):
    template_name = 'contactus.html'
    form_class = ContactUsForm
    success_url = reverse_lazy('contact_success')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact_form'] = ContactUsForm()

        return context

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


    def form_invalid(self, form):
        error_message = "There was an error with your submission. Please check the form and try again."
        return self.render_to_response(self.get_context_data(form=form, error_message=error_message))


def contact_success(request):
    return render(request, 'contactsuccess.html')
        

def account_signup_redirect(request):
    username = request.user.username
    redirect_url = f"/create_profile/{username}"

    return redirect(redirect_url)