from django.contrib import admin
from api.models import Pokemon
from api.models import VideoCall
from api.models import Invoice

class PokemonAdmin(admin.ModelAdmin):
    search_fields = ('name',)

    list_display = (
        'number', 'name', 'type1', 'type2', 'generation', 'legendary', 
        )

    list_filter = (
        'type1', 'type2', 'generation', 'legendary',
    )

    fieldsets = (
        (None, {
            'fields': ('name', 'number', 'type1', 'type2', 'generation', 'legendary')
        }),
        ('Stats', {
            'fields': ('hp', 'speed', 'attack', 'sp_atk', 'defense', 'sp_def', ),
        }),
    )    

admin.site.register(Pokemon, PokemonAdmin)



class VideoCallAdmin(admin.ModelAdmin):
    search_fields = ('name',)

    list_display = (
        'number', 'name', 'type1', 'type2', 'generation', 'legendary', 
        )

    list_filter = (
        'type1', 'type2', 'generation', 'legendary',
    )

    fieldsets = (
        (None, {
            'fields': ('name', 'number', 'type1', 'type2', 'generation', 'legendary')
        }),
        ('Stats', {
            'fields': ('hp', 'speed', 'attack', 'sp_atk', 'defense', 'sp_def', ),
        }),
    )    

admin.site.register(VideoCall, VideoCallAdmin)



class InvoiceAdmin(admin.ModelAdmin):
    search_fields = ('name',)

    list_display = (
        'number', 'name', 'address', 'zipcode', 'city', 'paid', 
        )

admin.site.register(Invoice, InvoiceAdmin)


