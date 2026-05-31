from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import BlogPost
from .forms import PostForm

def index(request):
    posts = BlogPost.objects.order_by('-date')
    context = {'posts': posts}
    return render(request, 'blogs/index.html', context)

@login_required
def new_entry(request):
    if request.method != 'POST':
        form = PostForm()
    else:
        form = PostForm(data=request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.owner = request.user
            new_post.save()
            return redirect('blogs:index')
    context = {'form': form}
    return render(request, 'blogs/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    entry = BlogPost.objects.get(id=entry_id)

    if entry.owner != request.user:
        raise Http404
    if request.method != 'POST':
        form = PostForm(instance=entry)
    else:
        form = PostForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:index')
    context = {'entry': entry, 'form': form}
    return render(request, 'blogs/edit_entry.html', context)


