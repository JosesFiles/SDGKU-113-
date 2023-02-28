from django.view.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post
from django.urls import reverse_lazy


class PostListView(ListView):
    template_name = "post/list.html"
    model = Post

class PostDetailView(DetailView):
    template_name = "post/detail.html"
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    template_name = "post/new.html"
    model = Post
    fields = ["title", "subtitle", "body", "active"]

    def from_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, Updateview):
    template_name = "posts/edit.html"
    model =Post
    fields = ["title", "subtitle", "body", "active"]

    def test_func(self):
        user = self.request.user
        post = self.get_object()
        return user ==post.author

class PostDeletView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = "post/delete.html"
    model = Post
    success_url = reverse_lazy("list")

    def test_func(self):
        user = self.request.user
        post = self.get_object()
        return user ==post.author 