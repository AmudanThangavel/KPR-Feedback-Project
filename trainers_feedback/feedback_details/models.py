from django.db import models

# Create your models here.

class trainer_data(models.Model):
    id = models.CharField(max_length=10)
    name = models.CharField(max_length=30)
    destination  = models.CharField(max_length=30)
    phone_no = models.IntegerField()

    def __str__(self):
        return self.id

# class trainer_feedback(models.Model):
#     id = models.OneToOneField(
#         trainer_data,
#         on_delete=models.CASCADE,
#         primary_key=True,
#         )
#     communicatin_skill = models.IntegerField()
#     content_delivered = models.IntegerField()
#     doubt_clarification = models.IntegerField()
#     technical_skill = models.IntegerField()
#     feedback = models.CharField(max_length = 500)