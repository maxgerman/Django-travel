from django.db import models
from cities.models import City


class Route(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Route name')
    travel_times = models.PositiveIntegerField(verbose_name='Total travel time')
    from_city = models.ForeignKey(
        City, on_delete=models.CASCADE, related_name='route_from_city_set',
        verbose_name='Из какого города')
    to_city = models.ForeignKey(
        'cities.City', on_delete=models.CASCADE, related_name='route_to_city_set',
        verbose_name='В какой город')
    trains = models.ManyToManyField('trains.Train', verbose_name='Список поездов')

    def __str__(self):
        return f'Route {self.name} ({self.from_city} - {self.to_city})'

    class Meta:
        verbose_name = 'Route'
        verbose_name_plural = 'Routes'
        ordering = ['travel_times']
