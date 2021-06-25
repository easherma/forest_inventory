from factory import Faker, fuzzy
from factory.django import DjangoModelFactory, ImageField
from forest_inventory.forests.models import Forest, ForestType


class ForestFactory(DjangoModelFactory):
    class Meta:
        model = Forest

    name = Faker("text", max_nb_chars=15)
    type = fuzzy.FuzzyChoice(ForestType)
    image = ImageField()
    latitude = Faker("latitude")
    longitude = Faker("longitude")
    area_covered = Faker("random_int")
    country = Faker("country")
    description = Faker("text")
    carbon_stored = Faker("random_int")
    change_in_carbon_stored_in_last_30_days = Faker("random_int")
