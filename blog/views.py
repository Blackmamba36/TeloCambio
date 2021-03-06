from django.shortcuts import render
from django.views.generic import ListView, DeleteView

from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
#from .forms import PostForm
#def home(request):
#    return render(request, 'home.html', {})

class HomeView(ListView):
    model = Post
    template_name =  'home.html'
    oredering = [' -post_date']


def categoryView(request, id):
    category_posts = Post.objects.all().filter(category=id)
    return render(request, 'categories.html', {'category_posts':category_posts})



class ArticleDetailView(DetailView):
    model = Post
    template_name =  'article_details.html'


class AddPostView(CreateView):
    template_name = 'add_post.html'
    model = Post
    fields = ['title', 'title_tag', 'category','body','image']
    #form_class = PostForm
    #template_name = 'add_post.html'
    #fields = '__all__'
    success_url='/'

class AddCategoryView(CreateView):
    template_name = 'add_category.html'
    model = Category
    fields = ['name']
    #form_class = PostForm
    #template_name = 'add_post.html'
    #fields = '__all__'
    success_url='/'

class UpdatePostView(UpdateView):
    model = Post
    template_name =  'update_post.html'
    fields = ['title', 'title_tag', 'category', 'body']
    success_url='/'

class DeletePostView(DeleteView):
    model = Post
    template_name =  'delete_post.html'
    success_url='/'