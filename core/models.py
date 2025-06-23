from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    image_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name



class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    price = models.FloatField()
    old_price = models.FloatField(null=True, blank=True)
    description = models.TextField()
    image_url = models.URLField()
    affiliate_link = models.URLField()

    # ✅ Nouveaux champs
    rating = models.FloatField(default=4.0)  # Note sur 5
    review_count = models.IntegerField(default=1000)  # Nombre d'avis

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=200)
    summary = models.TextField()
    content = models.TextField()
    published_at = models.DateField(auto_now_add=True)
    image_url = models.URLField(blank=True, null=True)  # ✅ image ajoutée

    def __str__(self):
        return self.title







class MessageContact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"
