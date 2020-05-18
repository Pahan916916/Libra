from django.db import models
from django.contrib.auth.models import User
import uuid, datetime, os

def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join(filename)

class table_pass(models.Model):
    password = models.TextField()

    def __str__(self):
        return "%s" % (self.password)


class category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(default="")

    def get_id(self):
        return "%s" % (self.id)

    def __str__(self):
        return "%s" % (self.name)

class author(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(default="")

    def get_id(self):
        return "%s" % (self.id)

    def __str__(self):
        return "%s" % (self.name)
      

class book(models.Model):
    name = models.CharField(max_length=50)
    author = models.ForeignKey(author, on_delete=models.CASCADE)
    description = models.TextField(default="")
    release_date = models.DateField(auto_now=False, auto_now_add=False, default=datetime.date.today)
    category = models.ForeignKey(category, on_delete=models.CASCADE)
    cover = models.ImageField(default=None)
    book_file = models.FileField(default=None, upload_to=get_file_path)
    blocked = models.BooleanField(default=False)

    def get_id(self):
        return "%s" % (self.id)

    def __str__(self):
        return "%s" % (self.name)

# Create your models here.
