# Django filters imports
import django_filters


class TaskFilter(django_filters.filterset.FilterSet):
    min_points = django_filters.rest_framework.filters.NumberFilter(field_name='points', lookup_expr='gte')
    max_points = django_filters.rest_framework.filters.NumberFilter(field_name='points', lookup_expr='lte')
    order = django_filters.rest_framework.filters.OrderingFilter(fields=('title', 'points', 'task', 'exam'))


class ExamFilter(django_filters.filterset.FilterSet):
    order = django_filters.rest_framework.filters.OrderingFilter(fields=('name', 'grade', 'comments'))


class AnswersFilter(django_filters.filterset.FilterSet):
    order = django_filters.rest_framework.filters.OrderingFilter(fields=('student', 'answers', 'test'))
