from django.db import models
from django.contrib.auth.models import User

from django.core.urlresolvers import reverse

# Create your models here.

class Topic(models.Model):
    top_name = models.CharField(max_length=264,unique=True)

    def __str__(self):
        return self.top_name

    def get_absolute_url(self):
        return reverse("first_app:detail",kwargs={'pk':self.pk})



class Webpage(models.Model):
    topic = models.ForeignKey(Topic,related_name='webpages')
    name = models.CharField(max_length=264,unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name

class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage)
    date = models.DateField()

    def __str__(self):
        return str(self.date)


class UserProfileInfo(models.Model):

    user = models.OneToOneField(User) # do not inherit from User here !!!!

    # additional
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        return self.user.username
