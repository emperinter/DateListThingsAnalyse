from django.db import models

class User(models.Model):
    # 非自增ID
    # user_id = models.IntegerField(primary_key=True,auto_created=True,unique=True)
    user_id = models.AutoField(primary_key=True)
    user_name = models.TextField(max_length=32,unique=True)
    user_passwd = models.TextField(max_length=32)

class ListThings(models.Model):
    # things_id = models.IntegerField(primary_key=True,auto_created=True)
    # userid = models.ForeignKey(User,to_field='user_id',on_delete=models.CASCADE,default="-1")
    things_id = models.AutoField(primary_key=True)
    userid = models.IntegerField()
    date = models.DateField(unique=True)
    process = models.IntegerField()
    emotion = models.IntegerField()
    energy = models.IntegerField()
    key = models.TextField()
