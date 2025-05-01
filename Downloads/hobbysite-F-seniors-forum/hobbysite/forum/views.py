from django.shortcuts import render, get_object_or_404, redirect
from .models import Profile, Thread, ThreadCategory, Comment
from .forms import ThreadForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    template_name = 'login.html'

def index(request):
    categories = ThreadCategory.objects.all()
    return render(request, 'forum/index.html', {'categories': categories})

def thread_list(request):
    categories = ThreadCategory.objects.all()
    threads = Thread.objects.all()

    user_threads = []
    other_threads = []

    if request.user.is_authenticated:
        try:
            user_profile = Profile.objects.get(user=request.user)
            user_threads = threads.filter(author=user_profile)
            other_threads = threads.exclude(author=user_profile)
        except Profile.DoesNotExist:
            user_threads = []
            other_threads = threads
    else:
        other_threads = threads

    return render(request, 'forum/forum_threads.html', {
        'categories': categories,
        'user_threads': user_threads,
        'other_threads': other_threads,
    })

def thread_detail(request, pk):
    thread = get_object_or_404(Thread, pk=pk)
    print(f"Thread category: {thread.category}")
    comments = thread.comments.all().order_by('created_on')

    related_threads = Thread.objects.filter(
        category=thread.category
    ).exclude(pk=thread.pk)[:2]

    if request.method == "POST":
        if request.user.is_authenticated:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.thread = thread
                comment.author = request.user.profile
                comment.save()
                messages.success(request, 'Your comment has been posted.')
                return redirect('forum:forum_thread_1', pk=thread.pk)
        else:
            messages.error(request, 'You must be logged in to comment.')
            return redirect('forum:forum_thread_1', pk=thread.pk)
    else:
        form = CommentForm()

    return render(request, 'forum/forum_thread_1.html', {
        'thread': thread,
        'comments': comments,
        'comment_form': form,
        'related_threads': related_threads,
    })


@login_required
def thread_create(request):
    if request.method == "POST":
        form = ThreadForm(request.POST)
        if form.is_valid():
            thread = form.save(commit=False)
            thread.author = request.user.profile
            thread.save()
            messages.success(request, 'Thread created successfully.')
            return redirect('forum:forum_thread_1', pk=thread.pk)
    else:
        form = ThreadForm()

    return render(request, 'forum/forum_thread_form.html', {'form': form})

@login_required
def thread_update(request, pk):
    thread = get_object_or_404(Thread, pk=pk)

    if thread.author != request.user:
        messages.error(request, 'You are not allowed to edit this thread.')
        return redirect('forum:forum_thread_1', pk=pk)

    if request.method == "POST":
        form = ThreadForm(request.POST, instance=thread)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thread updated successfully.')
            return redirect('forum:forum_thread_1', pk=thread.pk)
    else:
        form = ThreadForm(instance=thread)

    return render(request, 'forum/forum_thread_form.html', {'form': form})
