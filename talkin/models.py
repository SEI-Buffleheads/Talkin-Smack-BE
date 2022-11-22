from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    username = models.CharField(max_length=128)
    email = models.EmailField(max_length=128)
    avatar = models.CharField(max_length=500)
    password = models.CharField(max_length=128)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
      return f'{self.first_name} - {self.username}'

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    text = models.CharField(max_length=500)
    creation_date = models.DateTimeField(auto_now_add=True)
    # reply_to = models.ForeignKey(Reply, on_delete=models.CASCADE, related_name='post', blank=True)
    
class Reply(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='replies')
    smack = models.ForeignKey(Post,related_name="replies",on_delete=models.CASCADE)
    text = models.CharField(max_length=500)
    creation_date = models.DateTimeField(auto_now_add=True)

    
    
