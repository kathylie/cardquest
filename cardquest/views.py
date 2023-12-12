from django.views.generic.list import ListView
from cardquest.models import PokemonCard, Collection, Trainer

class HomePageView(ListView):
    model = PokemonCard
    context_object_name = 'base'  # The name used in the template for the list of objects
    template_name = "base.html"   # The template file to be rendered

    def get_context_data(self, kwargs):
        context = super().get_context_data(kwargs)
        # Add any additional context data you want to pass to the template
        return context

class TrainerList(ListView):
    model = Trainer
    context_object_name = 'trainer'  # The name used in the template for the list of objects
    template_name = "trainer.html"  # The template file to be rendered
    paginate_by = 15  # Number of items to display per page

class PokemonList(ListView):
    model = PokemonCard
    context_object_name = 'pokemon'  # The name used in the template for the list of objects
    template_name = "pokemon-card.html"  # The template file to be rendered
    paginate_by = 15  # Number of items to display per page

class CollectionList(ListView):
    model = Collection
    context_object_name = 'collection'  # The name used in the template for the list of objects
    template_name = "collection.html"  # The template file to be rendered
    paginate_by = 15  # Number of items to display per page