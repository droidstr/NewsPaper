from django.shortcuts import render

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, get_urlconf

from .models import Post
from .forms import PostForm
from .filters import PostFilter


class PostsList(ListView):
    model = Post
    ordering = '-created'
    template_name = 'posts.html'
    context_object_name = 'posts'
    paginate_by = 10


class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'


class PostSearch(PostsList):
    template_name = 'posts_search.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class PostCreate(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post_edit.html'
    context_object_name = 'post'


class PostEdit(UpdateView):
    form_class = PostForm
    template_name = 'post_edit.html'
    context_object_name = 'post'


class PostDelete(DeleteView):
    template_name = 'post_delete.html'
    success_url = reverse_lazy('news')
    context_object_name = 'post'


class NewsCreate(PostCreate):
    def form_valid(self, form):
        post = form.save(commit=False)
        post.type = 'MW'
        return super().form_valid(form)


class NewsEdit(PostEdit):
    queryset = Post.objects.filter(type='MW')

    def form_valid(self, form):
        post = form.save(commit=False)
        post.type = 'MW'
        return super().form_valid(form)


class NewsDelete(PostDelete):
    queryset = Post.objects.filter(type='MW')


class ArticleCreate(PostCreate):
    def form_valid(self, form):
        post = form.save(commit=False)
        post.type = 'AR'
        return super().form_valid(form)


class ArticleEdit(PostEdit):
    queryset = Post.objects.filter(type='AR')

    def form_valid(self, form):
        post = form.save(commit=False)
        post.type = 'AR'
        return super().form_valid(form)


class ArticleDelete(PostDelete):
    queryset = Post.objects.filter(type='AR')