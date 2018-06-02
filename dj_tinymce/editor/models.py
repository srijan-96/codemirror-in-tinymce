from django.db import models

# Create your models here.

class EditorData(models.Model):
    htmlContent = models.TextField()
    showHTML = models.TextField()
    lastModified = models.CharField(max_length=50, default="1 Jan 1970")
    # The following is just for database filtering purpose
    name = models.CharField(max_length=10, default="Jeff")

    def __str__(self):
        return self.name
        