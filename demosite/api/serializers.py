from rest_framework import serializers

from api.models import Pokemon, Invoice

# Serializers define the API representation.
class PokemonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pokemon
        fields = ['number', 'name', 'type1', 'type2', 'generation', 'legendary']

class InvoiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Invoice
        fields = ['number', 'date', 'name', 'address', 'zipcode', 'city', 'country', 'item_name', 'price_net', 'vat', 'price_gross', 'paid']