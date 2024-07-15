from django.shortcuts import render
from django.core.paginator import Paginator
from general.articles_filter import PublicationFilter
from publication.models import Category, Publication
from .forms import BlogCommentForm
from general.models import BlogComment, Gallery

# Create your views here.
def landing_page(request):
    categories,page_obj,parameters=_show_categories_and_products(request)
    resent_articles = Publication.objects.filter(active=True).order_by('-id')[:3]
    gallery = Gallery.objects.all()
    form = BlogCommentForm()
    context = {
        'categories':categories,
        'gallery':gallery,
        'form':form,
        'resent_articles':resent_articles,
        'pagination':page_obj,
        'parameters': parameters,
        
        
    }
    if request.method == "POST":
        form = BlogCommentForm(request.POST)
        if form.is_valid():
            comment = form.save()
            return render(request,'blog/index.html',context)
    return render(request,'blog/index.html',context)

# Create your views here.
def publications_results(request):
    categories,page_obj,parameters=_show_categories_and_products(request)
    context = {
        'categories':categories,
        'pagination':page_obj,
        'parameters': parameters,
    }
    return render(request,'blog/publications_results.html',context)







def _show_categories_and_products(request):
    categories = Category.objects.filter(active=True)
    get_copy = request.GET.copy()
    parameters = get_copy.pop('page', True) and get_copy.urlencode()
    articles = PublicationFilter(request.GET, queryset=Publication.objects.filter(active=True))
    paginator = Paginator(articles.qs, 4)    # Show 25 contacts per page.
    page_number = request.GET.get("page",1)
    page_obj = paginator.get_page(page_number)
    return categories,page_obj,parameters







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


