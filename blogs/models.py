from django.db import models
from django.contrib.auth.models import User

class BlogPost(models.Model):
    """Модель для постов."""
    title = models.CharField(max_length=100)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        if len(self.text) > 30:
            return f"{self.title} - {self.text[:30]}..."
        return f"{self.title} - {self.text}"