from django.core.management.base import BaseCommand
from core.models import Author, Book, Tag, Profile, Review
from django.contrib.auth.models import User
from faker import Faker
import random

class Command(BaseCommand):
    help = 'Load a large set of initial data into the database'

    def handle(self, *args, **kwargs):
        fake = Faker('pt_BR')

        # Gerar autores
        authors = [Author(name=fake.name(), bio=fake.text(max_nb_chars=200)) for _ in range(20)]
        Author.objects.bulk_create(authors)

        # Gerar tags
        tag_names = ['Ficção', 'História', 'Biografia', 'Ciência', 'Tecnologia', 'Fantasia', 'Romance', 'Poesia', 'Educação', 'Saúde']
        tags = [Tag(name=name) for name in tag_names]
        Tag.objects.bulk_create(tags)

        # Gerar livros com autores e tags associadas
        for _ in range(50):
            book = Book(
                title=fake.sentence(nb_words=4),
                summary=fake.text(max_nb_chars=500),
                author=random.choice(authors)
            )
            book.save()
            book.tags.set(random.sample(tags, k=random.randint(1, 3)))

        # Gerar usuários e perfis
        for _ in range(10):
            username = fake.user_name()
            user = User.objects.create_user(username, fake.email(), 'password')
            Profile.objects.create(user=user, bio=fake.text(max_nb_chars=200), website=fake.url())

        # Gerar revisões de livros
        all_books = Book.objects.all()
        for book in all_books:
            for _ in range(random.randint(1, 5)):
                Review.objects.create(
                    book=book,
                    review_text=fake.text(max_nb_chars=200),
                    rating=random.randint(1, 5)
                )

        self.stdout.write(self.style.SUCCESS('Dados iniciais carregados com sucesso!'))
