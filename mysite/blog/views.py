from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from .models import Post,Comment
from .forms import PostForm,CommentForm
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse,reverse_lazy
from django.views.generic import CreateView,DeleteView,UpdateView,ListView,DetailView,TemplateView

# Create your views here.listlist

class AboutView(TemplateView):
    template_name = 'blog/blog_about.html'

class PostListView(ListView):
    model = Post
    #template_name = 'blog/blog_list.html'
    def get_queryset(self):
        return Post.objects.filter(publish_date__lte=timezone.now()).order_by('-publish_date')

class PostCreateView(LoginRequiredMixin,CreateView):
    login_url = "/login/"
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post
    
class PostUpdateView(LoginRequiredMixin,UpdateView):
    login_url = "/login/"
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post

class PostDetailView(DetailView):
    model = Post
    #template_name = 'blog/blog_detail.html'

class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = Post

    success_url = reverse_lazy('list')

class DraftListView(LoginRequiredMixin,ListView):
    
    login_url = '/login/'
    redirect_field_name = 'blog/post_draft_list.html'
    template_name = 'blog/post_draft_list.html'
    
    model = Post
    # template_name = 'blog/post_draft_list.html'
    context_object_name = 'post_draft_list'

    def get_queryset(self):
       return Post.objects.filter(publish_date__isnull=True).order_by('create_date')
    #template_name = 'blog/draft_list.html'

######################################################
######################################################
@login_required
def publishPost(request,pk):
    post = get_object_or_404(Post,pk=pk)
    post.get_publish_date()
    return redirect('blog:list')

@login_required
def add_comment_to_post(request,pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('blog:post_detail', pk=comment.post.pk)

    else:
        form = CommentForm()

    return render(request,'blog/comment_form.html',{'form':form})

@login_required
def approveComment(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    comment.approve()
    return redirect('blog:post_detail',pk=comment.post.pk)

@login_required
def removeComment(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('blog:post_detail', pk=post_pk)

