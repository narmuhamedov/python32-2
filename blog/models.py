from django.db import models


class ProgramLang(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to="")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
