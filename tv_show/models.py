from django.db import models

class Films(models.Model):
    GENRE = (
        ('Комедия', 'Комедия'),
        ('Хоррор', 'Хоррор'),
        ('Мелодрамма', 'Мелодрамма'),
        ('Аниме', 'Аниме')
    )
    title = models.CharField('Укажите название фильма', max_length=100)
    description = models.TextField('Укажите описание фильма', blank=True, null=True)
    image = models.ImageField('Добавьте фото', upload_to='images/')
    genre = models.CharField('Укажите жанр фильма', max_length=100, choices=GENRE)
    trailer = models.URLField('Укажите ссылку')
    cost = models.PositiveIntegerField('Укажите цену')
    director = models.CharField('Укажите директора', max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Премьеру'
        verbose_name_plural = 'Премьеры'
