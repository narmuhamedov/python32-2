from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from . import models, forms
from django.views import generic


# read - не полная информация
class TvShowView(generic.ListView):
    template_name = "films/film.html"
    queryset = models.Films.objects.all()

    def get_queryset(self):
        return models.Films.objects.all()


# def tv_show_view(request):
#     film = models.Films.objects.all()
#     return render(request, 'films/film.html', {'film_key': film})


# read - детальная информация об фильме
class TvShowDetailView(generic.DetailView):
    template_name = "films/film_detail.html"

    def get_object(self, **kwargs):
        show_id = self.kwargs.get("id")
        return get_object_or_404(models.Films, id=show_id)


# def tv_show_detail_view(request, id):
#     film_id = get_object_or_404(models.Films, id=id)
#     return render(request, 'films/film_detail.html', {'film_id_key': film_id})


# add tv_show
class AddTvShowView(generic.CreateView):
    template_name = "films/crud/create_film.html"
    form_class = forms.TvShowForm
    queryset = models.Films.objects.all()
    success_url = "/"

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(AddTvShowView, self).form_valid(form=form)


# def add_tv_show_view(request):
#     method = request.method
#     if method == 'POST':
#         form = forms.TvShowForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('Фильм успешно загружен')
#     else:
#         form = forms.TvShowForm()
#
#     return render(request, 'films/crud/create_film.html', {'form': form})


# delete tv_show
class DeleteTvShowView(generic.DeleteView):
    template_name = "films/crud/confirm_delete.html"
    success_url = "/"

    def get_object(self, **kwargs):
        show_id = self.kwargs.get("id")
        return get_object_or_404(models.Films, id=show_id)


# def delete_tv_show_view(request, id):
#     film_id_delete = get_object_or_404(models.Films, id=id)
#     film_id_delete.delete()
#     return HttpResponse('Фильм удален!')
#


# #update tv_show
class UpdateTvShowView(generic.UpdateView):
    template_name = "films/crud/update_films.html"
    form_class = forms.TvShowForm
    success_url = "/"

    def get_object(self, **kwargs):
        show_id = self.kwargs.get("id")
        return get_object_or_404(models.Films, id=show_id)

    def form_valid(self, form):
        return super(UpdateTvShowView, self).form_valid(form=form)


# def update_tv_show_view(request, id):
#     film_id = get_object_or_404(models.Films, id=id)
#     if request.method == 'POST':
#         form = forms.TvShowForm(instance=film_id, data=request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('Объект успешно обновлен')
#     else:
#         form = forms.TvShowForm(instance=film_id)
#
#         context = {
#             'form': form,
#             'object': film_id
#         }
#     return render(request, 'films/crud/update_films.html', context)


class Search(generic.ListView):
    template_name = "films/film.html"
    context_object_name = "film"
    paginate_by = 5

    def get_queryset(self):
        return models.Films.objects.filter(title__icontains=self.request.GET.get("q"))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["q"] = self.request.GET.get("q")
        return context
