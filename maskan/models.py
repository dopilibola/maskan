from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Profile modelini to'g'rilaymiz
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100, default='Unknown')
    job = models.CharField(max_length=255, default='Unemployed')
    image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    date_modified = models.DateTimeField(auto_now=True)  # fixing typo in field name
    phone = models.CharField(max_length=200, blank=True)
    address1 = models.CharField(max_length=200, blank=True)
    address2 = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=200, blank=True)
    state = models.CharField(max_length=200, blank=True)
    zipcode = models.CharField(max_length=200, blank=True)
    country = models.CharField(max_length=200, blank=True)
    old_cart = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.user.username


# Signal to create Profile when user is created
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

post_save.connect(create_profile, sender=User)



# vil tuman shahar 

class Cemeterys(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    description = models.TextField()
    image = models.URLField()
    total_graves = models.PositiveIntegerField()
    established = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Grave(models.Model):
    cemetery = models.ForeignKey(Cemeterys, on_delete=models.CASCADE, related_name='graves')
    row = models.CharField(max_length=1)  # A, B, C...
    column = models.IntegerField()
    is_occupied = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.row}{self.column} - {self.cemetery.name}"


class Person(models.Model):
    grave = models.OneToOneField(Grave, on_delete=models.CASCADE, related_name='person')
    name = models.CharField(max_length=255)
    birth_date = models.DateField()
    death_date = models.DateField()
    description = models.TextField()
    image = models.URLField()

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.CharField(max_length=200, default='')
    image = models.ImageField(upload_to='uploads/products/')
    # sale staff
    is_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(default=0, decimal_places=2, max_digits=6)

    def __str__(self):
        return self.name
