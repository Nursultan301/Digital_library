from django.contrib import admin

from book.models import Book, Author, Illustrator, Translation


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ('title', 'create_at', 'illustrator', 'translation', 'language')


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'date')


@admin.register(Illustrator)
class IllustratorAdmin(admin.ModelAdmin):
    list_display = ('name', 'date')


@admin.register(Translation)
class TranslationAdmin(admin.ModelAdmin):
    list_display = ('name', 'date')