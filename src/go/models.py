from django.db import models


class Publication(models.Model):
    title = models.CharField(max_length=30)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class Article(models.Model):
    headline = models.CharField(max_length=100)

    class Meta:
        ordering = ['headline']

    def __str__(self):
        return self.headline


class Purchase(models.Model):
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    quantity = models.IntegerField()