from django.db import models

# Modelo para representar um autor, relacionamento "um-para-muitos" será demonstrado com livros
class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return self.name

# Modelo para representar um livro, relacionamento "um-para-muitos" com o autor
class Book(models.Model):
    title = models.CharField(max_length=200)
    summary = models.TextField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
    # Relacionamento "muitos-para-muitos" será demonstrado com tags
    tags = models.ManyToManyField('Tag', related_name='books')

    def __str__(self):
        return self.title

# Modelo para representar uma etiqueta (Tag), relacionamento "muitos-para-muitos" com livros
class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Modelo para representar um perfil de usuário, relacionamento "um-para-um" com o usuário
class Profile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    bio = models.TextField()
    website = models.URLField(blank=True)

    def __str__(self):
        return self.user.username

# Modelo para representar uma revisão de um livro, relacionamento "um-para-muitos" com o livro
class Review(models.Model):
    book = models.ForeignKey(Book, related_name='reviews', on_delete=models.CASCADE)
    review_text = models.TextField()
    rating = models.IntegerField()

    def __str__(self):
        return f"Review of {self.book.title}"
