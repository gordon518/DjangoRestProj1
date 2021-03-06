from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=20,null=False)
    password = models.CharField(max_length=20,null=False)
    name = models.CharField(max_length=10,null=False) #name

    class Meta:
        ordering = ['username']

class Blog(models.Model):
    title = models.CharField(max_length=50,null=False)
    body = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE) #creator of blog
    create_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-create_date']