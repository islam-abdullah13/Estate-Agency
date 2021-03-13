import django_filters
from .models import Estate

class EstateFilter(django_filters.FilterSet):
    class Meta:
        model = Estate
        fields = '__all__'
