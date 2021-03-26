from rest_framework import viewsets

from api.models import Pokemon, Invoice
from api.serializers import PokemonSerializer, InvoiceSerializer

# Create your views here.
# ViewSets define the view behavior.
class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer


class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
