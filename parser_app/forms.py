from django import forms
from . import models, parser


class ParserForm(forms.Form):
    MEDIA_CHOICES = (("manas.kg", "manas.kg"),)
    media_type = forms.ChoiceField(choices=MEDIA_CHOICES)

    class Meta:
        fields = [
            "media_type",
        ]

    def parser_data(self):
        if self.data["media_type"] == "manas.kg":
            manas_parser = parser.parser()
            for i in manas_parser:
                models.ManasFilm.objects.create(**i)
