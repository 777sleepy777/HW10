from django.db import models

class Author(models.Model):
    fullname = models.CharField(max_length=50)
    born_date = models.CharField()
    born_location = models.CharField(max_length=150)
    description = models.TextField()
    #created_at = models.DateTimeField()

    def __str__(self):
        return f"{self.fullname}"

class Tag(models.Model):
    name = models.CharField(max_length=30, null=False, unique=True)



class Quotes(models.Model):
    tags = models.ManyToManyField(Tag)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, default=None, null=True)
    quote = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.quote}"



