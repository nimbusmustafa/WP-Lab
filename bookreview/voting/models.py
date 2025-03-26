from django.db import models

class BookVote(models.Model):
    GOOD = 'good'
    SATISFACTORY = 'satisfactory'
    BAD = 'bad'
    
    VOTE_CHOICES = [
        (GOOD, 'Good'),
        (SATISFACTORY, 'Satisfactory'),
        (BAD, 'Bad'),
    ]
    
    vote = models.CharField(max_length=20, choices=VOTE_CHOICES)

    def __str__(self):
        return self.vote
