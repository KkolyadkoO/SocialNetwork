from django.db import models
from django.contrib.auth.models import User


class GenderChoices(models.TextChoices):
    MALE = 'male', "Мужской"
    FEMALE = 'female', "Женский"

class RelationshipChoices(models.TextChoices):
    SINGLE = 'single', "Холост"
    IN_A_REL = 'in_a-rel', "В отношениях"
    ENGAGED = 'engaged', "Помолвлен(а)"
    MARRIED = 'married', "Женат/Замужем"
    IN_LOVE = 'in_love', "Влюблен(а)"
    COMPLICATED = 'complicated', "Всё сложно"


class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name="Пользователь", on_delete=models.CASCADE)
    avatar =models.ImageField(verbose_name="Аватар", null=True, blank=True)
    bio = models.TextField(verbose_name="О себе", max_length=500, blank=True, null=True)
    city = models.CharField(verbose_name="Город", max_length=50, blank=True, null=True)
    birth_date = models.DateField(verbose_name="Дата рождения", blank=True, null=True)
    gender = models.CharField(verbose_name="Пол", choices=GenderChoices.choices, max_length=10)
    relationship = models.CharField(verbose_name="Статус отношений", choices=RelationshipChoices.choices , max_length=20)