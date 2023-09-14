from django.shortcuts import render, get_object_or_404
from . import models

def tv_show_view(request):
    film = models.Films.objects.all()
    return render(request, 'films/film.html', {'film_key': film})

def tv_show_detail_view(request, id):
    film_id = get_object_or_404(models.Films, id=id)
    return render(request, 'films/film_detail.html', {'film_id_key': film_id})