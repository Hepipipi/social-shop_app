from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import Post, Profile


# Create your views here.


def social_main_page(request):

    return render(request, 'sociaty/index.html')

def register(request):
    pass


def profile(request):
    pass


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import SignUpForm, PostForm, CommentForm


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Аккаунт {username} был успешно создан! Теперь вы можете войти.')
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'sociaty/register.html', {'form': form})



def profile(request):
    posts = Post.objects.all()
    return render(request, 'sociaty/profile.html', {'posts': posts})


@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('profile')
    else:
        form = PostForm()
    return render(request, 'sociaty/create_post.html', {'form': form})


@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if post.author == request.user:
        post.delete()
    return redirect('profile')



@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('social_feed')
    else:
        form = CommentForm()
    return render(request, 'sociaty/add_comment.html', {'form': form, 'post': post})






def feed(request):
    if request.method == 'POST':
        author_id = request.POST.get('author')
        author = User.objects.get(id=author_id)

        user = request.user

        if user.profile.followers.filter(id=author.id).exists():
            user.profile.followers.remove(author)
        else:
            user.profile.followers.add(author)

    posts = Post.objects.all()
    authors = User.objects.all()

    return render(request, 'sociaty/feed.html', {'posts' : posts, 'authors': authors})

#
# def all_au(request):
#     authors = Profile.objects.all()
#     return render(request, 'sociaty/feed.html', {'authors': authors})

def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return redirect('social_feed')

def personal_feed(request):
    followed_authors = request.user.profile.followers.all()
    posts = Post.objects.filter(author__in=followed_authors)
    return render(request, 'sociatyfeed.html', {'posts': posts})

