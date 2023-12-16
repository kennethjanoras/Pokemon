from django.contrib import admin

# Register your models here.
from .models import PokemonCard, Trainer, Collection

#admin.site.register(PokemonCard)

@admin.register (PokemonCard)
class PokemonAdmin (admin. ModelAdmin):
    list_display = ("name", "rarity") 
    search_fields = ("name",)

@admin.register (Trainer)
class PokemonAdmin (admin. ModelAdmin):
    list_display = ("name", "location") 
    search_fields = ("name",)

@admin.register(Collection)
class PokemonAdmin(admin.ModelAdmin):
    list_display = ('display_trainer_name', 'display_pokemon_card', 'collection_date')
    search_fields = ('trainer__name', 'card__name', 'collection_date__icontains')  # Include trainer name, card name, and collection date in search

    def display_trainer_name(self, obj):
        return obj.trainer.name if obj.trainer else None  # Check for existence to avoid errors

    def display_pokemon_card(self, obj):
        return obj.card.name if obj.card else None  # Check for existence to avoid errors

    display_trainer_name.short_description = 'Trainer Name'
    display_pokemon_card.short_description = 'Pokemon Card Name'
