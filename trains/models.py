from django.core.exceptions import ValidationError
from django.db import models
from cities.models import City


class Train(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Train number')
    from_city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='From', related_name='from_city_set')
    to_city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='To', related_name='to_city_set')
    travel_time = models.IntegerField(verbose_name='Travel time')

    class Meta:
        verbose_name = 'Train'
        verbose_name_plural = 'Trains'
        ordering = ['name']

    def __str__(self):
        return self.name

    def clean(self, *args, **kwargs):
        if self.from_city == self.to_city:
            raise ValidationError('To-city and from-city cannot be the same. Change either of them')

        qs = Train.objects.filter(from_city=self.from_city,
                                  to_city=self.to_city,
                                  travel_time = self.travel_time).exclude(pk=self.pk)

        if qs.exists():
            raise ValidationError('Such train already exists. Change departure, destination or travel time')

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

