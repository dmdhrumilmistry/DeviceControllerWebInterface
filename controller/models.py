from django.db import models

# Create your models here.
class Device(models.Model):
    name = models.CharField(max_length=20, default="Not Changed Yet")
    state = models.BooleanField(default=False)
    pin_type = models.BooleanField(default=False) # 0->Digital, 1->Analog
    pin = models.IntegerField()

    def __str__(self) -> str:
        return f'{self.name}:{self.pin}:{self.state}'
