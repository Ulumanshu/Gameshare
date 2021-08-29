from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

LABLES1 = (
    ('TABLE', 'Table'),
    ('PC', 'Personal Computer'),
    ('X-BOX', 'X Box'),
    ('PS', 'Play Station')
)

STATUS = (
    ('NEW', 'New'),
    ('AVAILABLE', 'Available'),
    ('BUSY', 'Busy'),
    ('INACTIVE', 'Inactive')
)


class Games(models.Model):
    name = models.CharField(max_length=200, default="")
    photo = models.ImageField(upload_to='img', default=False)
    author = models.CharField(max_length=200)
    description = models.TextField()
    pub_date = models.DateField()
    label = models.CharField(choices=LABLES1, default="TABLE", max_length=9)

    def __str__(self):
        return self.name


class Items(models.Model):
    name = models.CharField(max_length=200, default="")
    game_id = models.ForeignKey(Games, related_name='game_item_ids', on_delete=models.CASCADE)
    owner_id = models.ForeignKey(User, related_name='item_ids', on_delete=models.CASCADE)
    rentee_id = models.ForeignKey(
        User,
        related_name='rented_item_ids',
        on_delete=models.SET_NULL,
        null=True,
    )
    status = models.CharField(choices=STATUS, default="NEW", max_length=9)
    rent_price = models.IntegerField()
    date_rent_start = models.DateField()
    date_rent_end = models.DateField()

    def __str__(self):
        return self.name
