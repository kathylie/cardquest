from django.contrib import admin
from .models import Collection, PokemonCard, Trainer

@admin.register(PokemonCard)
class PokemonCardAdmin(admin.ModelAdmin):
    list_display = ('name', 'rarity', 'hp', 'card_type', 'attack', 'description', 'weakness', 'card_number', 'release_date', 'evolution_stage', 'abilities',)

@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = ('name', 'birthdate', 'location', 'email')

admin.site.register(Collection)