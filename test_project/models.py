from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, help_text='Category name')

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


class Note(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='notes', related_query_name='node')
    keywords = models.CharField(max_length=400)
    title = models.CharField(max_length=200)
    date = models.DateTimeField()
    content = models.TextField(max_length=50000)

    def __str__(self):
        return self.title
