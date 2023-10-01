from django.urls import path

from . import views

app_name = "scipal"
urlpatterns = [
    path("", views.index, name="index"),
    path("results/", views.results, name="results"),
    path("find/", views.find, name="find"),
    path("similar/", views.similar, name="similar"),
]