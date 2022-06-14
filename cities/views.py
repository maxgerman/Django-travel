from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView
from django.core.paginator import Paginator

from cities.forms import HtmlForm, CityForm
from cities.models import City


def home(request, pk=None):
    if request.method == 'POST':
        form = CityForm(request.POST or None)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()

    # if pk:
    #     # # city = City.objects.filter(id=pk).first()
    #     city = get_object_or_404(City, id=pk)
    #     context = {'object': city}
    #     return render(request, 'cities/detail.html', context)
    form = CityForm()
    cities = City.objects.all()
    paginator = Paginator(cities, 5)
    page = request.GET.get('page')
    cities = paginator.get_page(page)
    context = {'page_obj': cities, 'form': form}
    return render(request, 'cities/home.html', context)


class CityDetailView(DetailView):
    queryset = City.objects.all()
    context_object_name = 'object'
    template_name = 'cities/detail.html'


class CityCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    login_url = 'cities:home'  # works without it
    model = City
    form_class = CityForm
    template_name = 'cities/create.html'
    success_url = reverse_lazy('cities:home')
    success_message = 'The city has been created successfully'


class CityUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = City
    form_class = CityForm
    template_name = 'cities/update.html'
    success_url = reverse_lazy('cities:home')
    success_message = 'The city has been updated'


class CityDeleteView(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    model = City
    template_name = 'cities/delete.html'
    success_url = reverse_lazy('cities:home')

    def get(self, request, *args, **kwargs):
        messages.success(request, 'The city has been deleted')
        return self.post(request, *args, **kwargs)


class CityListView(ListView):
    model = City
    template_name = 'cities/home.html'
    paginate_by = 5

    # if we need form on the city list page we include it into the context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = CityForm()
        context['form'] = form
        return context
