from django.db import models

class Viloyat(models.Model):
    title = models.CharField(max_length=50)
    context = models.TextField(blank=True)
    def __str__(self):
        return self.title
class Tuman(models.Model):
    title = models.CharField(max_length=50)
    context = models.TextField(blank=True)
    created_ed = models.DateTimeField(auto_now_add=True)
    update_ed = models.DateTimeField(auto_now=True)
    viloyat = models.ForeignKey(Viloyat,on_delete=models.CASCADE)
    def __str__(self):
        return self.title
class Mahalla(models.Model):
    title = models.CharField(max_length=50)
    context = models.TextField(blank=True)
    created_ed = models.DateTimeField(auto_now_add=True)
    update_ed = models.DateTimeField(auto_now=True)
    tuman = models.ForeignKey(Tuman,on_delete=models.CASCADE)
    def __str__(self):
        return self.title






