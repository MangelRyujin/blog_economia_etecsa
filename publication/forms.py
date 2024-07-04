from django import forms

from publication.models import PublicationComment


class PublicationCommentForm(forms.ModelForm):
    class Meta:
        model = PublicationComment
        fields = ['email','comment']