from django.db import models

# Create your models here.

class Task(models.Model):
    STATUS =(
        ('doing...','Doing...'),
        ('done!','Done!'),
    )


    title = models.CharField(max_length=50)
    content = models.TextField()
    status =models.CharField(
        max_length=20,
        choices=STATUS,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title