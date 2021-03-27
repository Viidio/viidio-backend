from django.db import models

# Create your models here.

class Pokemon(models.Model):
    number = models.PositiveIntegerField('PokeDex index number')
    name = models.CharField('Name of the Pokemon', max_length=100)

    type1 = models.CharField('Type of Pokemon', max_length=50)
    type2 = models.CharField('Other Type of Pokemon', max_length=50)

    hp = models.IntegerField('Hit Points')
    attack = models.IntegerField('Attack Strength')
    defense = models.IntegerField('Defensive Strength')
    sp_atk = models.IntegerField('Special Attack Strength')
    sp_def = models.IntegerField('Special Defensive Strength')
    speed = models.IntegerField('Speed')
    generation = models.IntegerField('Generation')
    legendary = models.BooleanField('Legendary Pokemon?', default=False)

    class Meta:
        ordering = ('number', 'name')


class VideoCall(models.Model):
    number = models.PositiveIntegerField('PokeDex index number')
    name = models.CharField('Name of the Pokemon', max_length=100)

    type1 = models.CharField('Type of Pokemon', max_length=50)
    type2 = models.CharField('Other Type of Pokemon', max_length=50)

    hp = models.IntegerField('Hit Points')
    attack = models.IntegerField('Attack Strength')
    defense = models.IntegerField('Defensive Strength')
    sp_atk = models.IntegerField('Special Attack Strength')
    sp_def = models.IntegerField('Special Defensive Strength')
    speed = models.IntegerField('Speed')
    generation = models.IntegerField('Generation')
    legendary = models.BooleanField('Legendary Pokemon?', default=False)

    class Meta:
        ordering = ('number', 'name')


class Invoice(models.Model):
    date = models.DateField('Date of invoice')
    number = models.PositiveIntegerField('Invoice number')
    
    name = models.CharField('Full Name', max_length=100)
    address = models.CharField('Address', max_length=100)
    zipcode = models.CharField('Zip Code', max_length=100)
    city = models.CharField('City', max_length=100)
    country = models.CharField('Country', max_length=100)

    item_name = models.CharField('Item Purchased', max_length=100)
    price_net = models.FloatField('Net Price', max_length=100)
    vat = models.FloatField('VAT', max_length=100)
    price_gross = models.FloatField('Gross Price', max_length=100)

    paid = models.BooleanField('Is this invoice already paid?', default=False)

    class Meta:
        ordering = ('-number', )

