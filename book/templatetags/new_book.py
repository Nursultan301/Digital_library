from django import template

from book.models import Book

register = template.Library()


@register.inclusion_tag('book/tags/new_book.html')
def ger_new_book(cnt=2):
    books = Book.objects.order_by('-create_at')[:cnt]
    return {"books": books}