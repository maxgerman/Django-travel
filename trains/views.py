from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Train


def home(request, pk=None):
    # if request.method == 'POST':
    #     form = CityForm(request.POST or None)
    #     if form.is_valid():
    #         print(form.cleaned_data)
    #         form.save()

    # if pk:
    #     # # city = City.objects.filter(id=pk).first()
    #     city = get_object_or_404(City, id=pk)
    #     context = {'object': city}
    #     return render(request, 'cities/detail.html', context)
    trains = Train.objects.all()
    paginator = Paginator(trains, 10)
    page = request.GET.get('page')
    trains = paginator.get_page(page)
    context = {'page_obj': trains,}
    return render(request, 'trains/home.html', context)