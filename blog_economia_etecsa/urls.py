"""
URL configuration for blog_economia_etecsa project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from general.views import blog_comments, create_blog_comments, landing_page,publications_results
from publication.views import create_publications_comments, publication_detail, publications_comments
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin/logout/', LogoutView.as_view(), name='logout'),
    path('',landing_page,name='landing-page'),
    path('publications_results/',publications_results,name='publications_results'),
    
    path('blog_comments/<int:pk>/',blog_comments,name='blog_comments'),
    path('blog_comments/create/',create_blog_comments,name='create_blog_comments'),
    
    path('publicacions_comments/<int:pk>/<int:comment_id>/',publications_comments,name='publications_comments'),
    
    
    path('publications_comments/create/<int:pk>/', create_publications_comments, name='create_publications_comments'),
    path('publicacion/<int:pk>/',publication_detail,name='publication_detail-page')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
