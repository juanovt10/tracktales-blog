from django.shortcuts import render, redirect
from django.views import generic, View
from django.views.generic import TemplateView
from .models import Post, TAGS, WORLD_AREAS
from .forms import PostForm

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
        return context

 
    # def get(self, request, slug, *args, **kwargs):
    #     queryset = Post.objects
    #     post = get_object_or_404(queryset, slug=slug)

    #     return render(
    #         request,
    #         'board.html',
    #         {
    #             'post_form': PostForm()
    #         },
    #     )    

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            return redirect('post_board')
    else:
        form = PostForm()

    return render(request, 'board.html', {'form': form})
