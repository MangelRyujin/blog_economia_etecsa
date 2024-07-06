from django.shortcuts import render
from django.core.paginator import Paginator
from general.articles_filter import PublicationFilter
from publication.models import Category, Publication
from .forms import BlogCommentForm
from general.models import BlogComment, Gallery

# Create your views here.
def landing_page(request):
    categories = Category.objects.filter(active=True)
    get_copy = request.GET.copy()
    print(get_copy)
    parameters = get_copy.pop('page', True) and get_copy.urlencode()
    articles = PublicationFilter(request.GET, queryset=Publication.objects.filter(active=True))
    paginator = Paginator(articles.qs, 3)    # Show 25 contacts per page.
    page_number = request.GET.get("page",1)
    page_obj = paginator.get_page(page_number)
    resent_articles = Publication.objects.filter(active=True).order_by('-id')[:3]
    gallery = Gallery.objects.all()
    form = BlogCommentForm()
    start_index = (int(page_number) - 1) * 10 + 1
    end_index = start_index + len(page_obj) - 1
    context = {
        'categories':categories,
        'gallery':gallery,
        'form':form,
        'resent_articles':resent_articles,
        'pagination':page_obj,
        'parameters': parameters,
        'start_index':start_index,
        'end_index': end_index,
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


