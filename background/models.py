from django.db import models

class User(models.Model):
    # 非自增ID
    # user_id = models.IntegerField(primary_key=True,auto_created=True,unique=True)

    # 自增user_id
    user_id = models.AutoField(primary_key=True)
    user_name = models.TextField(max_length=32,unique=True)
    user_passwd = models.TextField(max_length=32)

    def __str__(self):
        return self.user_name

class ListThings(models.Model):
    # things_id = models.IntegerField(primary_key=True,auto_created=True)
    # userid = models.ForeignKey(User,to_field='user_id',on_delete=models.CASCADE,default="-1")

    # 自增things_id
    things_id = models.AutoField(primary_key=True)
    # userid = models.IntegerField()
    userid = models.ForeignKey(User,to_field='user_id',on_delete=models.CASCADE,default="-1")
    date = models.DateField(unique=True)
    process = models.IntegerField()
    emotion = models.IntegerField()
    energy = models.IntegerField()
    key = models.TextField()

    def __str__(self):
        return str(self.things_id)