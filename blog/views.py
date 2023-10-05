from django.shortcuts import render
from . import models


def program_lang_view(request):
    lang = models.ProgramLang.objects.all()
    return render(request, "blog.html", {"lang_key": lang})
