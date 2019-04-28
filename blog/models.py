from django.db import models
from django.utils import timezone

#define modelo objeto que é salvo em models
class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE) #link para outro modelo
    title = models.CharField(max_length=200) #limitado
    text = models.TextField()#quantidade ilimitado de caracter
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    #metodos
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title