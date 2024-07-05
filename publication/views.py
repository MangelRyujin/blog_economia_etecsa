from django.shortcuts import render
from general.forms import BlogCommentForm
from publication.forms import PublicationCommentForm
from publication.models import Publication,PublicationComment

# Create your views here.
def publication_detail(request,pk):
    publication = Publication.objects.filter(pk=pk).first()
    comments = PublicationComment.objects.filter(publication= publication.id,active=True)
    form = PublicationCommentForm()
    resent_articles = Publication.objects.filter(active=True).order_by('-id')[:3]
    context = {
        'publication':publication,
        'comments':comments,
        'form':form,
        'resent_articles':resent_articles
    }
    if request.method == "POST":
        form = PublicationCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.publication = publication
            comment.save()

            return render(request,'blog/publication_detail.html',context)

    return render(request,'blog/publication_detail.html',context)

