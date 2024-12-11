from django.db import models
class Contact (models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name

class Otherchefs(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.title

class GalleryPage(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.title




class Book(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    room=models.CharField(max_length=100)
    menu=models.CharField(max_length=100 )
    arrival=models.DateTimeField()
    departure=models.DateTimeField()
    message=models.CharField(max_length=100)


    def __str__(self):
        return self.name
class Order(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    menu=models.CharField(max_length=100)
    guests=models.IntegerField()
    conference=models.CharField(max_length=100)
    arrival=models.DateTimeField()


    def __str__(self):
        return self.name


