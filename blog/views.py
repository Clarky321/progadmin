from django.shortcuts import render, get_object_or_404
from .models import Section, Post

def home(request):
    sections = Section.objects.all()
    latest_posts = Post.objects.filter(status='published')[:12]
    return render(request, 'blog/home.html', {
        'sections': sections,
        'latest_posts': latest_posts,
    })

def section_detail(request, slug):
    section = get_object_or_404(Section, slug=slug)
    posts = section.posts.filter(status='published')
    return render(request, 'blog/section_detail.html', {
        'section': section,
        'posts': posts,
    })

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, status='published')
    return render(request, 'blog/post_detail.html', {'post': post})