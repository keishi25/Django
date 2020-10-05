from django.db import models


class Club(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Person(models.Model):
    """
    1対多モデルを構築したい時は、
    子モデルに、ForeignKey設定をするだけでよい
    """
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    club = models.ForeignKey(Club, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + ' ' + self.club.name
