from django.db import models


#model for Creator registraion


class CreatorUserProfile(models.Model):
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    nickname = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    date_of_birth = models.DateField(null=True)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    profession = models.CharField(max_length=50)
    experience = models.IntegerField(null=True)


    def __str__(self):
        return self.nickname
    