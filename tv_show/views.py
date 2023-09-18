from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from . import models, forms

#read - не полная информация
def tv_show_view(request):
    film = models.Films.objects.all()
    return render(request, 'films/film.html', {'film_key': film})

#read - детальная информация об фильме
def tv_show_detail_view(request, id):
    film_id = get_object_or_404(models.Films, id=id)
    return render(request, 'films/film_detail.html', {'film_id_key': film_id})

#add tv_show
def add_tv_show_view(request):
    method = request.method
    if method == 'POST':
        form = forms.TvShowForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('Фильм успешно загружен')
    else:
        form = forms.TvShowForm()

    return render(request, 'films/crud/create_film.html', {'form': form})

#delete tv_show
def delete_tv_show_view(request, id):
    film_id_delete = get_object_or_404(models.Films, id=id)
    film_id_delete.delete()
    return HttpResponse('Фильм удален!')