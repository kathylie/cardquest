from django.db import models

# Create your models here.
class BaseModel(models.Model):


    class Meta:
        abstract = True

class Trainer(BaseModel):
    name = models.CharField(max_length=100, null=True, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=250, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)

    def show_info(self):
        return (
            f"Name: {self.name}\n"
            f"Age: {self.birthdate}\n"
            f"Location: {self.location}\n"
            f"Email: {self.email}"
        )

    def __str__(self):
        return self.name

class PokemonCard(BaseModel):
    RARITY_CHOICES = (
        ('Common','Common'),
        ('Uncommon', 'Uncommon'),
        ('Rare','Rare')

    )
    CARDTYPE_CHOICES = (
        ('Fire','Fire'),
        ('Water','Water'),
        ('Grass','Grass'),
        ('Electric', 'Electric'),
        ('Psychic', 'Psychic'),
        ('Ice','Ice'),
        ('Dragon','Dragon'),
        ('Dark','Dark'),
        ('Normal','Normal'),
        ('Fighting','Fighting'),
        ('Flying','Flying'),
        ('Poison','Poison'),
        ('Ground','Ground'),
        ('Rock','Rock'),
        ('Bug','Bug'),
        ('Ghost','Ghost'),
        ('Steel','Steel'),
        ('Fairy','Fairy'),
    )
    name = models.CharField(max_length=100, null=True, blank=True)
    rarity = models.CharField(
        max_length=100, null=True, blank=True, choices=RARITY_CHOICES)
    hp = models.IntegerField(null=True, blank=True)
    card_type = models.CharField (
        max_length=100, null=True, blank=True, choices=CARDTYPE_CHOICES)
    attack = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=250, null=True, blank=True)
    weakness = models.CharField(max_length=250, null=True, blank=True)
    card_number = models.IntegerField(null=True, blank=True)
    release_date = models.DateField(null=True, blank=True)
    evolution_stage = models.CharField(max_length=250, null=True, blank=True)
    abilities = models.CharField(max_length=250, null=True, blank=True)

    def show_info(self):
        return (
            f"Name: {self.name}\n"
            f"Rarity: {self.rarity}\n"
            f"HP: {self.hp}\n"
            f"Card Type: {self.card_type}\n"
            f"Attack: {self.attack}\n"
            f"Description: {self.description}\n"
            f"Weakness: {self.weakness}\n"
            f"Card Number: {self.card_number}\n"
            f"Release Date: {self.release_date}\n"
            f"Evolution Stage: {self.evolution_stage}\n"
            f"Abilities: {self.abilities}\n"
        )

    def __str__(self):
        return self.name


class Collection(models.Model):
    card= models.ForeignKey(PokemonCard, blank =True, null=True, on_delete=models.CASCADE)
    trainer = models.ForeignKey(
        Trainer, blank=True, null=True, on_delete=models.CASCADE)
    collection_date=models.DateField()

