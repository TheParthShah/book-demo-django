from django.db import models


# Create your models here.


# Model for book details
class Book(models.Model):
    title = models.CharField(max_length=36, null=True, blank=False, unique=True, default='')
    description = models.TextField(max_length=256, blank=True, null=True)
    price = models.DecimalField(default=0.00, decimal_places=2, max_digits=16)
    publishedOn = models.DateField(blank=True, default=None, null=True)
    coverImage = models.ImageField(upload_to='coverImage/', blank=True)
    onSale = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    # number = models.OneToOneField(BookNumber, null=True, blank=True, on_delete=models.CASCADE)


# Model for book number
class BookNumber(models.Model):
    isbn_10 = models.CharField(max_length=10, blank=True)
    isbn_13 = models.CharField(max_length=13, blank=True)
