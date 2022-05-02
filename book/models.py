from django.db import models


class Book(models.Model):
    """Книга"""
    LANGUAGE = (
        ('kg', 'Кыргызкий'),
        ('ru', 'Русский'),
        ('en', 'Английский'),
    )

    title = models.CharField("Называние", max_length=50)
    descriptions = models.TextField("Описание")
    img = models.ImageField("Фото", upload_to='media/book')
    created_at = models.DateTimeField("Дата", auto_now_add=True)
    author = models.ForeignKey("Author", on_delete=models.SET_NULL, null=True, verbose_name='Автор',
                               related_name='author')
    illustrator = models.ForeignKey("Illustrator", on_delete=models.SET_NULL, null=True, verbose_name="Иллюстратор",
                                    related_name='illustrator')
    translation = models.ForeignKey("Translation", on_delete=models.SET_NULL, null=True, verbose_name="Иллюстратор",
                                    related_name='translation')
    language = models.CharField("Язык", max_length=50, choices=LANGUAGE, default='ru')

    def __str__(self):
        return self.title

    def language_v(self):
        return dict(self.LANGUAGE)[self.language]

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'


class Author(models.Model):
    """ Автор """
    name = models.CharField("Имя", max_length=50)
    data = models.CharField("Созданно", max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Автор'


class Illustrator(models.Model):
    """ Иллюстратор """
    name = models.CharField("Имя", max_length=50)
    data = models.CharField("Созданно", max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Иллюстратор'
        verbose_name_plural = 'Иллюстратор'


class Translation(models.Model):
    """ Перевод и адаптация """
    name = models.CharField("Имя", max_length=50)
    data = models.CharField("Созданно", max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Перевод и адаптация'
        verbose_name_plural = 'Перевод и адаптация'


