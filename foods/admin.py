from django.contrib import admin

from .models import Food, FoodCategory


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    """Класс для отображения таблицы food."""
    list_display = ('category',
                    'is_vegan',
                    'is_special',
                    'code',
                    'internal_code',
                    'name_ru',
                    'description_ru',
                    'description_en',
                    'description_ch',
                    'cost',
                    'is_publish',
                    )
    search_fields = ('name_ru',)
    fieldsets = (
        ('Food', {
            'fields': (
                'category',
                'is_vegan',
                'is_special',
                'code',
                'internal_code',
                'name_ru',
                'description_ru',
                'description_en',
                'description_ch',
                'cost',
                'is_publish',
                'additional',
            ),
        },),
    )


@admin.register(FoodCategory)
class FoodCategoryAdmin(admin.ModelAdmin):
    """Класс для отображения таблицы food_category."""
    list_display = ('name_ru', 'name_en', 'name_ch', 'order_id')
    fields = ('name_ru', 'name_en', 'name_ch', 'order_id')
    search_fields = ('name_ru',)


admin.site.site_title = 'Foods'
admin.site.site_header = 'Foods'
