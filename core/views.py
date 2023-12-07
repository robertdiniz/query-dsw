from django.shortcuts import render
from .models import Book, Author, Tag, Review, Profile

def query_examples(request):
    # Consulta simples com filter
    books_by_title = Book.objects.filter(title__icontains='a')

    # Consulta com lookup para buscar autores por nome
    authors_by_name = Author.objects.filter(name__icontains='Paulo')

    # Consulta many-to-many (livros com uma determinada tag)
    books_with_tag = Book.objects.filter(tags__name='Romance')

    # Consulta com relacionamento reverso (todos os livros de um autor)
    books_of_author = Book.objects.filter(author__name='Paulo')

    # Consulta agregada (por exemplo, número de livros de um autor)
    num_books_of_author = Book.objects.filter(author__name='Paulo').count()

    # Envie todas as consultas para o template
    context = {
        'books_by_title': books_by_title,
        'authors_by_name': authors_by_name,
        'books_with_tag': books_with_tag,
        'books_of_author': books_of_author,
        'num_books_of_author': num_books_of_author,
    }

    return render(request, 'core/teste1.html', context)


def query_exercise1(request):

    books_of_author = Book.objects.filter(author__name='Lucas Moreira')

    books_with_tag = Book.objects.filter(tags__name='Romance')

    authors_specific_bio = Author.objects.filter(bio__icontains="odio")

    highly_rated_books = Review.objects.filter(rating__gte=4).order_by('-rating')

    specific_websites_users = Profile.objects.filter(website__icontains='oliveira')

    books_without_review = Book.objects.filter(reviews__isnull=True)

    books_long_summaries = Book.objects.annotate(comprimento_resumo=len('resumo')).filter(comprimento_resumo__gt=150)

    print(books_long_summaries)

    context = {
        'books_of_author': books_of_author,
        'books_with_tag': books_with_tag,
        'authors_specific_bio': authors_specific_bio,
        'highly_rated_books': highly_rated_books,
        'specific_websites_users': specific_websites_users,
        'books_without_review': books_without_review
    }

    return render(request, 'core/teste2.html', context)
