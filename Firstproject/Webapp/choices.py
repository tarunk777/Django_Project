from django.db import models

class ProductCategoryChoice(models.TextChoices):
    DOG = "DOG", "Dog"
    CAT = "CAT","Cat"
    FISH = "FISH", "Fish"