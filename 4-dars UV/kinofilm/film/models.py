from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Kategoriya nomi')
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Movie(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Kategoriyasi')
    name = models.CharField(max_length=50, verbose_name='Film nomi')
    description = models.TextField()
    release_date = models.DateTimeField(verbose_name='Chiqgan sana')
    made = models.CharField(max_length=50, verbose_name='Film qayerda chiqgan')
    language = models.CharField(max_length=50, verbose_name='Film Tili')


    def __str__(self):
        return self.name

class Comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    author_name = models.CharField(max_length=50, verbose_name='Kommentator ismi')
    description = models.TextField()

    def __str__(self):
        return self.author_name


