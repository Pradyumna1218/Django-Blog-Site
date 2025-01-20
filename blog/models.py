from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
class Post(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    date_posted = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.title


'''
DATETIMEFIELD
auto_now = True 
    update the date time everytime the post was updated

auto_now_add = True 
    update the date time only when the object is created but you can't update the date

user delete what do
cascade post delete then user no delete but user delete post also delete

MIGRATIONS
make changes to database even after it created and has data in database
We would have to run a complicated sql but migrations makes changes for us
'''