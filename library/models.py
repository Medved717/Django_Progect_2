from django.db import models

class Author(models.Model):

    first_name = models.CharField(max_length=150, verbose_name='Имя автора')
    last_name = models.CharField(max_length=150, verbose_name='Фамилия автора')
    birth_date = models.DateField(verbose_name='Дата рождения автора')

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'
        ordering = ('last_name',)

    def __str__(self):
        return f'{self.first_name}, {self.last_name}'

class Book(models.Model):

    title = models.CharField(max_length=200, verbose_name='Наименование книги')
    publication_data = models.DateField(verbose_name='Дата публикации')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        ordering = ('title',)

    def __str__(self):
        return self.title


