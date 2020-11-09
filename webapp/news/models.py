from django.db import models

# Create your models here.
class Headline(models.Model):
    title=model.CharField(max_length=200)
    image=models.UrlField(null=True,blank=True)
    url=models.textField()

    def __str__(self):
        return self.title
