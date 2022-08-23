from rest_framework.pagination import PageNumberPagination

from backend.settings import LIMIT, SIX


class CustomPagination(PageNumberPagination):
    page_size = SIX
    page_size_query_param = LIMIT
