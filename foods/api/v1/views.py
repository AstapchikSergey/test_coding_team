from django.contrib.postgres.aggregates import ArrayAgg
from django.http import JsonResponse
from django.views.generic.list import BaseListView

from foods.models import Food, FoodCategory
from foods.serializers import FoodListSerializer

category_annotation = {
    f"category": ArrayAgg("category__name_ru", distinct=True)
}


class FoodsApiMixin(BaseListView):
    """Миксин для классов."""
    http_method_names = ['get']

    @staticmethod
    def render_to_response(context, **response_kwargs):
        return JsonResponse(context, safe=False)


class FoodCategoryListApi(FoodsApiMixin):
    """Класс представления списка категорий еды."""
    model = FoodCategory

    def get_queryset(self):
        food_categories = FoodCategory.objects.all().values()
        return food_categories

    def get_context_data(self, *, object_list=None, **kwargs):
        queryset = self.get_queryset()
        context = [list(queryset)]
        return context


class FoodsListApi(FoodsApiMixin):
    """Класс представления полного списка еды с категориями."""

    model = Food

    def get_queryset(self):
        """Переопределения стандартной функции получения queryset."""
        foods = Food.objects.all().select_related('category', ).filter(
            is_publish=True).values().annotate(**category_annotation)
        return foods

    def get_context_data(self, *, object_list=None, **kwargs):
        """Переопределения стандартной функции получения context_data."""
        queryset = self.get_queryset()
        result_context = []
        context = FoodCategoryListApi().get_queryset().values()

        for category in context:
            for query in list(queryset):
                if query['category'][0] == category['name_ru']:
                    if 'food' not in category.keys():
                        category['food'] = []
                    category['food'].append(query)

        for category in context:
            if 'food' in category.keys():
                result_context.append(category)

        serializer = FoodListSerializer(instance=result_context, many=True)

        return serializer.data
