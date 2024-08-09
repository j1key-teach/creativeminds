from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    JUNIOR = 'junior'
    MIDDLE = 'middle'
    SENIOR = 'senior'

    STAGE_CHOICES = [
        (JUNIOR, 'Junior'),
        (MIDDLE, 'Middle'),
        (SENIOR, 'Senior'),
    ]

    stage = models.CharField(max_length=10, choices=STAGE_CHOICES, default=JUNIOR)

    def upgrade_stage(self):
        if self.stage == self.JUNIOR:
            self.stage = self.MIDDLE
        elif self.stage == self.MIDDLE:
            self.stage = self.SENIOR
        self.save()
