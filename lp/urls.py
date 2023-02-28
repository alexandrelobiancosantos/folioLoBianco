from django.urls import path

from lp.views import index

urlpatterns = [
    path('', index),
]
