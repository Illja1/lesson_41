from django.db import models


class Categories(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Note(models.Model):
    title = models.CharField(max_length=150)
    text =models.TextField(max_length=150)
    reminder = models.DateTimeField()
    category = models.ForeignKey(Categories,on_delete=models.CASCADE)


    def __str__(self):
        return self.title
    

