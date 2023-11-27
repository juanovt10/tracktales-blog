from django.shortcuts import render
from django.views import generic
from django.views.generic import TemplateView
from .models import Post, TAGS, WORLD_AREAS

def index(request):
    return render(request, 'index.html')

class PostBoard(generic.ListView):
    model = Post
    queryset = Post.objects.filter(approved=True).order_by('-created_on')
    template_name = 'board.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = TAGS
        context['areas'] = WORLD_AREAS
        return context

