from django.contrib import admin
from recipes.models import (Favorite, Ingredient, Recipe, RecipeIngredient,
                            ShoppingCart, Tag)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    search_fields = ('name',)
    list_filter = ('name',)


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'measurement_unit')
    list_filter = ('measurement_unit',)
    search_fields = ('name', 'measurement_unit',)


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    extra = 0


class RecipeTagInLine(admin.TabularInline):
    model = Recipe.tags.through


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'author',
        'tags',
        'favorite_count',
        'cooking_time',
    )

    search_fields = (
        'author__username',
        'name',
        'tags',
    )

    readonly_fields = ('favorite_count',)
    list_filter = [
        'tags',
        'author',
    ]
    inlines = [RecipeIngredientInline]

    def tags(self, obj):
        tag = obj
        return ','.join([x.name for x in tag.recipes.all()])

    @admin.display(description='Добавлений в избранное')
    def favorite_count(self, obj):
        return Favorite.objects.filter(recipe=obj).count()
    favorite_count.short_description = 'Кол-во добавлений в избранное'


@admin.register(ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe')
    search_fields = ('user',)
    list_filter = ('user',)


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe')
    search_fields = ('user',)
    list_filter = ('user',)
