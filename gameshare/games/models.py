from django.db import models

# Create your models here.

LABLES1 = (
    ('TABLE', 'Table'),
    ('PC', 'Personal Computer'),
    ('X-BOX', 'X Box'),
    ('PS', 'Play Station')
)


class GamesItem(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField()
    pub_date = models.DateField()
    label = models.CharField(choices=LABLES1, default="TABLE", max_length=7)

    def __str__(self):
        return self.name
