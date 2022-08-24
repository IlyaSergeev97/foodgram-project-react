from rest_framework.pagination import PageNumberPagination

from backend.settings import PAGE_SIZE_QUERY_PARAM, SIX


class CustomPagination(PageNumberPagination):
    page_size = SIX
    page_size_query_param = PAGE_SIZE_QUERY_PARAM
