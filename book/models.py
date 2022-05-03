from django.db import models


class Author(models.Model):
    """ Автор """
    name = models.CharField("Имя", max_length=50, unique=True)
    date = models.DateField("Созданно", auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Автор'


class Illustrator(models.Model):
    """ Иллюстратор """
    name = models.CharField("Имя", max_length=50, unique=True)
    date = models.DateField("Созданно", auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Иллюстратор'
        verbose_name_plural = 'Иллюстратор'


class Translation(models.Model):
    """ Перевод и адаптация """
    name = models.CharField("Имя", max_length=50, unique=True)
    date = models.DateField("Созданно", auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Перевод и адаптация'
        verbose_name_plural = 'Перевод и адаптация'


class Book(models.Model):
    """Книга"""
    LANGUAGE = (
        ('kg', 'Кыргызкий'),
        ('ru', 'Русский'),
        ('en', 'Английский'),
    )

    title = models.CharField("Называние", max_length=50)
    descriptions = models.TextField("Описание", blank=True)
    img = models.ImageField("Фото", upload_to='media/book')
    create_at = models.DateField("Дата", auto_now_add=True)
    author = models.ManyToManyField(Author, verbose_name='Автор', related_name='set_author')
    illustrator = models.ForeignKey(Illustrator, on_delete=models.SET_NULL, null=True, blank=True,
                                    verbose_name="Иллюстратор",
                                    related_name='illustrator')
    translation = models.ForeignKey(Translation, on_delete=models.SET_NULL, null=True, blank=True,
                                    verbose_name="Перевод и адаптация",
                                    related_name='translation')
    language = models.CharField("Язык", max_length=50, choices=LANGUAGE, default='ru')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title

    def language_v(self):
        return dict(self.LANGUAGE)[self.language]

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'


class Comment(models.Model):
    """ Комментария """
    name = models.CharField("Имя", max_length=50)
    email = models.EmailField("E-mail")
    messages = models.TextField("Сообшения")
    date = models.DateField(auto_now_add=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name="Книга")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Комментария'
        verbose_name_plural = 'Комментарии'
