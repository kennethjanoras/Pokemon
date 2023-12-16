from django.shortcuts import render

# Create your views here.
from django.views.generic.list import ListView
from cardquest.models import PokemonCard, Trainer , Collection

class HomePageView(ListView):
    model = PokemonCard
    context_object_name = 'home'
    template_name = "base.html"
    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       return context

class TrainerList(ListView):
    model = Trainer
    context_object_name = 'trainer'
    template_name = 'trainers.html'
    paginate_by =15

class PokemonCardList(ListView):
    model = PokemonCard
    context_object_name = 'pokemon_cards'
    template_name = 'pokemon-cards.html'
    paginate_by = 8

class CollectionList(ListView):
    model = Collection
    context_object_name = 'collections'
    template_name = "collections.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Include the related Trainer and PokemonCard in the context
        context['collections'] = Collection.objects.select_related('trainer', 'card').all()
        return context

# In the view
def my_view(request):
    pokemon_cards = PokemonCard.objects.all()

    # Print image URLs for debugging
    for card in pokemon_cards:
        print(f"{card.name}: {card.image_url}")

    return render(request, 'pokemon-cards.html', {'pokemon_cards': pokemon_cards})

