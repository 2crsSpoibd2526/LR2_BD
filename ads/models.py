from django.db import models

class Rubric(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Bb(models.Model):
    rubric = models.ForeignKey(Rubric, on_delete=models.PROTECT, null=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    price = models.IntegerField(null=True, blank=True)
    published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
