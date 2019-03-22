from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    details = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now) # Gets timestamp from users timezone settings
    author = models.ForeignKey(User, on_delete=models.CASCADE) #if user deletes account, cascade deltes all of his posts as well

    def __str__(self):
        return self.title
 
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
