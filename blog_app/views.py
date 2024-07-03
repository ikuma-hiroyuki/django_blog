from django.shortcuts import render

from blog_app.models import Post


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'list.html', {'posts': posts})
