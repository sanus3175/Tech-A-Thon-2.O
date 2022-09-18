# from django.db import models
# Create your models here.
import email
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator
'''
STATE_CHOICS = (
    ('Assam','Assam'),
    ('Bihar','Bihar'),
    ('Delhi','Delhi'),
    ('Goa','Goa'),
    ('Jammu & Kashmir','Jammu & Kashmir'),
)
'''
class Bloger(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pincode = models.IntegerField()
    contact_no = models.CharField(max_length=10)
    email = models.EmailField()


def _str_(self):
 return str(self.id)

 

BLOG_CHOICES = (
    ('CS','Computer Science'),
    ('SC','Social Media'),
    ('PL','Politics'),
    ('AL','All'),
)

class Blog(models.Model):
   title = models.CharField(max_length=100)
   description = models.CharField(max_length=5000)
   category = models.CharField(choices=BLOG_CHOICES,max_length=2)
   blog_image = models.ImageField(upload_to='productimg')

def _str_(self):
  return str(self.id)
