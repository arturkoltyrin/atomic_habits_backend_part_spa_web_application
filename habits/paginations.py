from rest_framework.pagination import PageNumberPagination


class ViewUserHabitPagination(PageNumberPagination):
    """Пагинация для привычек"""

    page_size = 5
