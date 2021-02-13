from django.db import models
from django.utils import timezone
from django.core.validators import FileExtensionValidator

class Post(models.Model):
    author = models.ForeignKey('account.MyUser',on_delete=models.CASCADE)
    title = models.CharField(max_length=25, verbose_name="Название файла")
    url = 'calculation/'
    file = models.FileField(upload_to=url, verbose_name="Файл",blank=True, validators=([FileExtensionValidator(['xlsx','xlsm','xltx','xltm'])]))
    file_name = models.CharField(max_length=50, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    csi = models.FloatField(default=0)
    loyalty = models.FloatField(default=0)
    regressa = models.FloatField(default=0)
    one = models.FloatField(default=0)
    two = models.FloatField(default=0)
    three = models.FloatField(default=0)
    four = models.FloatField(default=0)
    five = models.FloatField(default=0)
    nps = models.FloatField(default=0)
    barrier = models.FloatField(default=0)


    def __str__(self):
        return self.title
