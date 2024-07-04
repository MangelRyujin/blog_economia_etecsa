from django.contrib import admin

from general.customUser import CustomUserAdmin
from publication.models import PublicationComment
from .models import BlogComment, Presentation,Social,Gallery
from solo.admin import SingletonModelAdmin # type: ignore
from django.contrib.auth.models import User

# Register your models here.
admin.site.register(Presentation , SingletonModelAdmin)
admin.site.register(Social , SingletonModelAdmin)
@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ['id','name','image']

@admin.register(BlogComment)
class BlogCommentAdmin(admin.ModelAdmin):
    list_display = ['id','email','date_time_create','active','likes']
    list_editable = ('active',)
    
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)