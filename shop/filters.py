from django_filters import rest_framework as filters

from shop.models import Product


def search_by_value(queryset, name, value):
    look_up = f"{name}__icontains"
    return queryset.filter(**{look_up: value})


class ProductFilter(filters.FilterSet):

    product_name = filters.CharFilter(field_name='name', method=search_by_value)
    product_category = filters.CharFilter(field_name='category', method=search_by_value)
    newest = filters.DateFilter(field_name='created_at', lookup_expr='lte')
    oldest = filters.DateFilter(field_name='created_at', lookup_expr='gte')


