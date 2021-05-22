from django.urls import path
from .views import home, CityDetailView

urlpatterns = [
        path('', home, name='home'),
        path('detail/<int:pk>/', CityDetailView.as_view(), name='detail'),
]
