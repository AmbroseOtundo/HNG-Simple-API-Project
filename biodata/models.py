from django.db import models

# Create your models here.
class Profile(models.Model):
    slackUsername= models.CharField(max_length=30)
    backend = models.BooleanField(True)
    age = models.IntegerField()
    bio = models.TextField(max_length=255)

    class Meta:
        ordering = ['slackUsername']

    def __str__(self) -> str:
        return Profile.slackUsername
    