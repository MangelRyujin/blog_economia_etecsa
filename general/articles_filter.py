import django_filters
from publication.models import Category, Publication


class PublicationFilter(django_filters.FilterSet):
    category = django_filters.ModelChoiceFilter(queryset=Category.objects.all())
    title=  django_filters.CharFilter(lookup_expr='icontains')
    
    class Meta:
        model = Publication
        fields = ['title','category']

            