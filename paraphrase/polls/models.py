from django.db import models

# Create your models here.

class Grammercheck(models.Model):
    title = models.TextField()

    def __str__(self):
        return self.title
    
    def delete(self, *args, **kwargs):
        if self.title:
            self.title.delete()
            super().delete(*args, **kwargs)

class Paracheck(models.Model):
    description = models.TextField()
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description
    
    def delete(self, *args, **kwargs):
        if self.description:
            self.description.delete()
            super().delete(*args, **kwargs)

class Spellcheck(models.Model):
    description = models.TextField()
    #document = models.FileField(upload_to='documents/')
    #uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description
    
    def delete(self, *args, **kwargs):
        if self.description:
            self.description.delete()
            super().delete(*args, **kwargs)

class Filespellcheck(models.Model):
    description = models.TextField()
    document = models.FileField(upload_to='textdocuments/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description
    
    def delete(self, *args, **kwargs):
        if self.description:
            self.description.delete()
            super().delete(*args, **kwargs)