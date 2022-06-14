from django import forms
from .models import Train
from cities.models import City


class TrainForm(forms.ModelForm):
    class Meta:
        model = Train
        fields = ('name', 'from_city', 'to_city', 'travel_time')

    name = forms.CharField(
        label='Train',
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Enter train number'}))
    from_city = forms.ModelChoiceField(
        label='From', queryset=City.objects.all(),
        widget=forms.Select(
            attrs={'class': 'form-control', 'placeholder': 'From'}))
    to_city = forms.ModelChoiceField(
        label='To', queryset=City.objects.all(),
        widget=forms.Select(
            attrs={'class': 'form-control', 'placeholder': 'To'}))
    travel_time = forms.IntegerField(
        label='Travel time',
        widget=forms.NumberInput(
            attrs={'class': 'form-control', 'placeholder': 'Travel time'}))