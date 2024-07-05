from django.shortcuts import render
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


def create_publications_comments(request,pk):
    publication = Publication.objects.filter(pk=pk).first()
    
    
    form = PublicationCommentForm()
    context = {
        'form':form,
        'publication':publication
    }
    if request.method == "POST":
        
        form = PublicationCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.publication = publication
            comment.save()
            return render(request,'comments/create_publications_comments.html',context)
    
    return render(request,'comments/create_publications_comments.html',context)



def publications_comments(request,pk,comment_id):
    comments=[]
    if request.method == "POST":
        comment = PublicationComment.objects.get(pk = comment_id)
        if comment.user_has_comment(request.user.id):
            comment.users.remove(request.user)
            comment.likes-=1
            comment.save()
        else:
            comment.users.add(request.user)
            comment.likes+=1
            comment.save()
            
    all_comments = PublicationComment.objects.filter(publication=pk,active=True)
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
    
    return render(request,'comments/publications_comments.html',context)


