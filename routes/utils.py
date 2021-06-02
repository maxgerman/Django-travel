from django.shortcuts import render
from django.contrib import messages

from trains.models import Train
from .forms import RouteForm


def dfs_paths(graph, start, goal):
    """Функция поиска всех возможных маршрутов
    из одного города в другой. Вариант посещения
    одного и того же города более одного раза,
    не рассматривается.
    """
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        if vertex in graph.keys():
            for next_ in graph[vertex] - set(path):
                if next_ == goal:
                    yield path + [next_]
                else:
                    stack.append((next_, path + [next_]))


def get_graph(_qs):
    """Return the graph of the trains in _qs as a dictionary {city_from : set(cities_to)} """
    qs = _qs.values()
    graph = {}
    for q in qs:
        graph.setdefault(q['from_city_id'], set())
        graph[q['from_city_id']].add(q['to_city_id'])
    return graph


def get_routes(request, form):
    '''
    Функция поиска маршрута
    :param request: request
    :param form: форма с начальными данными от пользователя
    :return: список маршрутов, готовых для отображения
    '''
    # import time as _t
    # start = _t.time()
    qs = Train.objects.all().select_related('from_city', 'to_city').order_by('travel_time')
    data = form.cleaned_data
    from_city = data['from_city']
    to_city = data['to_city']
    cities = data['cities']
    travelling_time = data['travelling_time']
    graph = get_graph(_qs=qs)
    all_ways = list(dfs_paths(graph, from_city.id, to_city.id))
    if not all_ways:
        # нет ни одного маршрута для данного поиска
        raise ValueError('No routes found')
    if cities:
        # если есть города, через которые нужно проехать
        across_cities = [city.id for city in cities]
        right_ways = []
        for way in all_ways:
            # тогда отбираем те маршруты, которые проходят через них
            if all(point in way for point in across_cities):
                right_ways.append(way)
        if not right_ways:
            # когда список маршрутов пуст
            raise ValueError('There is no route via the required cities')
    else:
        right_ways = all_ways

    routes = []
    all_trains = {}
    for q in qs:
        all_trains.setdefault((q.from_city_id, q.to_city_id), [])
        all_trains[(q.from_city_id, q.to_city_id)].append(q)
    for route in right_ways:
        # для городов по пути следования, выбираем необходимые поезда
        tmp = {}
        tmp['trains'] = []
        total_time = 0
        for index in range(len(route) - 1):
            qs = all_trains[(route[index], route[index + 1])]
            qs = qs[0]
            # qs = Train.objects.filter(from_city=route[index],
            # to_city=route[index + 1])
            # qs = qs.order_by('travel_time').first()
            total_time += qs.travel_time
            tmp['trains'].append(qs)
        tmp['total_time'] = total_time
        if travelling_time is None or travelling_time and total_time <= travelling_time:
            # check the total travel time requirement if set
            routes.append(tmp)
    if not routes:
        # если список пуст, то нет таких маршрутов,
        # которые удовлетворяли бы заданным условиям
        raise ValueError('Total travel time exceeds the requirement')

    cities = {'from_city': from_city, 'to_city': to_city}

    if len(routes) == 1:
        sorted_routes = routes
    else:
        sorted_routes = sorted(routes, key=lambda route: route['total_time'])
    context = {'form': form, 'routes': sorted_routes, 'cities': cities}
    return context
