from django.db import models

# Create your models here.
class Author(models.Model):
    id = models.IntegerField(primary_key=True)
    fio = models.CharField(max_length=200)
    email = models.EmailField()
    # password = models.Fie
    def __str__(self):
        return self.fio    

class Blog(models.Model):
    id = models.IntegerField(primary_key=True)
    theme = models.CharField(max_length=200)
    text = models.TextField()
    datetimecreate = models.DateTimeField()
    author = models.ForeignKey('Author', on_delete=models.PROTECT)

    def __str__(self):
        return self.theme + self.id