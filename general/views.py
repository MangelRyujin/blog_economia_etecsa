from django.shortcuts import render

from publication.models import Publication, PublicationComment
from .forms import BlogCommentForm
from general.models import BlogComment, Gallery

# Create your views here.
def landing_page(request):
    # comments = BlogComment.objects.filter(active=True)
    articles = Publication.objects.filter(active=True)
    resent_articles = Publication.objects.filter(active=True).order_by('-id')[:3]
    gallery = Gallery.objects.all()
    form = BlogCommentForm()
    context = {
        'gallery':gallery,
        'articles':articles,
        'form':form,
        'resent_articles':resent_articles
    }
    if request.method == "POST":
        form = BlogCommentForm(request.POST)
        if form.is_valid():
            comment = form.save()
            return render(request,'blog/index.html',context)
    return render(request,'blog/index.html',context)


def create_blog_comments(request):
    form = BlogCommentForm()
    context = {
        'form':form,
    }
    if request.method == "POST":
        form = BlogCommentForm(request.POST)
        if form.is_valid():
            comment = form.save()
            return render(request,'comments/create_blog_comments.html',context)
    return render(request,'comments/create_blog_comments.html',context)



def blog_comments(request,pk):
    comments=[]
    if request.method == "POST":
        comment = BlogComment.objects.get(pk = pk)
        if comment.user_has_comment(request.user.id):
            comment.users.remove(request.user)
            comment.likes-=1
            comment.save()
        else:
            comment.users.add(request.user)
            comment.likes+=1
            comment.save()
            
    all_comments = BlogComment.objects.filter(active=True)
    for comment in all_comments:
        like=comment.user_has_comment(request.user.id)
        comments.append(
                {
                    'like':like,
                    'comment':comment
                }
            )
    context = {
        'comments':comments,
    }
    
    return render(request,'comments/blog_comments.html',context)


