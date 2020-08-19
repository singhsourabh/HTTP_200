from django.conf import settings

from rest_framework.pagination import PageNumberPagination


def paginated_queryset(queryset, request):
    """ # noqa: E117
    Return a paginated queryset.
    """
    paginator = PageNumberPagination()
    paginator.page_size = settings.REST_FRAMEWORK['PAGE_SIZE']
    result_page = paginator.paginate_queryset(queryset, request)
    return (paginator, result_page)
