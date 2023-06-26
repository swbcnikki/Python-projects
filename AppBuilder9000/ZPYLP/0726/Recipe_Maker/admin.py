from django.contrib import admin

from .models import Recipe

"""
# inlines allow models to be edited on the same page as the parent model
class IngredientsInline(admin.TabularInline):
    model = Ingredients
    extra = 5


class InstructionsInline(admin.TabularInline):
    model = Instructions


# add the inlines to the model
class RecipeAdmin(admin.ModelAdmin):
    inlines = [
        IngredientsInline,
        InstructionsInline,
    ]
"""


admin.site.register(Recipe)
