from django.shortcuts import render
from general.forms import BlogCommentForm
from publication.forms import PublicationCommentForm
from publication.models import Publication,PublicationComment

# Create your views here.
def publication_detail(request,pk):
    publication = Publication.objects.filter(pk=pk).first()
    comments = PublicationComment.objects.filter(publication= publication.id,active=True)
    form = PublicationCommentForm()
    context = {
        'publication':publication,
        'comments':comments,
        'form':form,
    }
    if request.method == "POST":
        form = PublicationCommentForm(request.POST)
        if form.is_valid():
            comment = form.save()

            return render(request,'blog/publication_detail.html',context)

    return render(request,'blog/publication_detail.html',context)

