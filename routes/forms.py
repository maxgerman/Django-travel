from django import forms
from cities.models import City
from .models import Route


class RouteForm(forms.Form):
    from_city = forms.ModelChoiceField(label='From:', queryset=City.objects.all(), widget=forms.Select(
        attrs={'class': 'form-control js-example-basic-single'}))
    to_city = forms.ModelChoiceField(label='To:', queryset=City.objects.all(), widget=forms.Select(
        attrs={'class': 'form-control js-example-basic-single'}))
    cities = forms.ModelMultipleChoiceField(label='Via cities:', queryset=City.objects.all(),required=False,
                                            widget=forms.SelectMultiple(
            attrs={'class': 'form-control js-example-basic-multiple'}))
    travelling_time = forms.IntegerField(label='Maximum total travel time', widget=forms.NumberInput(attrs={
        'class': 'form-control', 'placeholder': 'Время в пути'})
                                         )


