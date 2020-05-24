from django.db import models
from django.contrib.auth.models import User

class PageContent(models.Model):
    title = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='pictures/%Y/%m/%d/', max_length=255, null=True, blank=True)
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{0} {1}".format(self.title, self.image)