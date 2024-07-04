from django.contrib import admin
from .models import Category, Publication, PublicationComment
# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name','active']
    list_editable = ('active',)

@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ['id','title','author','date_time_create','image','active']
    list_editable = ('active',)

@admin.register(PublicationComment)
class PublicationCommentAdmin(admin.ModelAdmin):
    list_display = ['id','email','publication','date_time_create','active','likes']
    list_editable = ('active',)