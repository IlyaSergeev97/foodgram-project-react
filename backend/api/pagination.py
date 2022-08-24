from backend.settings import PAGE_SIZE_QUERY_PARAM, SIX
from rest_framework.pagination import PageNumberPagination


class CustomPagination(PageNumberPagination):
    page_size = SIX
    page_size_query_param = PAGE_SIZE_QUERY_PARAM
