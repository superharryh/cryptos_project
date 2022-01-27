from django.urls import path

from .views import index
urlpatterns = [
    path('', index), #! 4.) root will be an index function from views.py
]