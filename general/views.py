from django.shortcuts import render

from publication.models import Publication, PublicationComment
from .forms import BlogCommentForm
from general.models import BlogComment, Gallery

# Create your views here.
def landing_page(request):
    comments = BlogComment.objects.filter(active=True)
    articles = Publication.objects.filter(active=True)
    resent_articles = Publication.objects.filter(active=True).order_by('-id')[:3]
    gallery = Gallery.objects.all()
    form = BlogCommentForm()
    context = {
        'comments':comments,
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





