from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import Http404

from django.views.generic import ListView


from .models import Post


class PostListView(ListView):
    queryset = Post.published.all()
    template_name = 'blog/post/list.html'
    context_object_name = 'posts'
    paginate_by = 3


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post,
                            slug=post,
                            publish__year=year,
                            publish__month=month,
                            publish__day=day,
                            status=Post.Status.PUBLISHED)
 
    return render(request, 'blog/post/detail.html', {'post': post})