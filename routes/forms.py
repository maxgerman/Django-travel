from django import forms
from cities.models import City
from trains.models import Train
from routes.models import Route


class RouteForm(forms.Form):
    from_city = forms.ModelChoiceField(label='From:', queryset=City.objects.all(), widget=forms.Select(
        attrs={'class': 'form-control js-example-basic-single'}), initial=1)
    to_city = forms.ModelChoiceField(label='To:', queryset=City.objects.all(), widget=forms.Select(
        attrs={'class': 'form-control js-example-basic-single'}), initial=3)
    cities = forms.ModelMultipleChoiceField(label='Via cities (optional):', queryset=City.objects.all(), required=False,
                                            widget=forms.SelectMultiple(
                                                attrs={'class': 'form-control js-example-basic-multiple'}))
    travelling_time = forms.IntegerField(label='Maximum travel time (optional)', required=False,
                                         widget=forms.NumberInput(
                                             attrs={'class': 'form-control', 'placeholder': 'Total time'})
                                         )


class RouteModelForm(forms.ModelForm):
    name = forms.CharField(label='Route name', widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Enter the name'}))
    from_city = forms.ModelChoiceField(queryset=City.objects.all(), widget=forms.HiddenInput())
    to_city = forms.ModelChoiceField(queryset=City.objects.all(), widget=forms.HiddenInput())
    trains = forms.ModelMultipleChoiceField(label='', queryset=Train.objects.all(), required=False, widget=forms.SelectMultiple(
            attrs={'class': 'form-control d-none'}))
    travel_times = forms.IntegerField(widget=forms.HiddenInput())

    class Meta:
        model = Route
        fields = '__all__'
