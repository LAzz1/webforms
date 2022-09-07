from django.db import models

class owasp(models.Model):
    code = models.CharField(max_length=10)
    year = models.CharField(max_length=4)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=2000)

    def __str__(self):
        return self.code+' - '+self.title