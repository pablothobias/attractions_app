from django.db import models
from django.contrib.auth.models import User

class Review(models.Model):
    STARS = (
        (1, 'Very Bad'),
        (2, 'Bad'),
        (3, 'Medium'),
        (4, 'Good'),
        (5, 'Excellent'),
    )

    review = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=True)
    stars = models.IntegerField(default=5, choices=STARS)
    author_review = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.author_review.first_name} - {self.date}"