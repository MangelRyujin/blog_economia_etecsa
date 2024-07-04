from django import forms

from general.models import BlogComment


class BlogCommentForm(forms.ModelForm):
    class Meta:
        model = BlogComment
        fields = ['email','comment']
