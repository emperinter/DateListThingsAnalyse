from django.db import models

#事件日期
class Things_Date(models.Model):
    date_id = models.IntegerField()
    date_time = models.DateField()

    def __str__(self):
        return self.date_id

class User(models.Model):
    user_id = models.IntegerField(primary_key=True)
    user_name = models.TextField(max_length=32,unique=True)
    user_passwd = models.TextField(max_length=32)

# 事项进度
# class Processing(models.Model):
#     process_id = models.IntegerField()
#     process = models.IntegerField()
#     emotion = models.IntegerField()
#     energy = models.IntegerField()
#     key = models.TextField(max_length=100) # 关键字
#     things_date = models.ForeignKey(Things_Date,on_delete=models.CASCADE,default="") # 外键，和事件日期相匹配
#
#     def __str__(self):
#         return self.process_id
#
#     def get_process(self):
#         return self.process
#
#     def get_emotion(self):
#         return self.emotion
#
#     def get_energy(self):
#         return self.energy
#
#     def get_key(self):
#         return self.key


class process(models.Model):
    process = models.IntegerField()
    things_date = models.ForeignKey(Things_Date, on_delete=models.CASCADE, default="")  # 外键，和事件日期相匹配
    def __str__(self):
        return self.process


class emotion(models.Model):
    emotion = models.IntegerField()
    things_date = models.ForeignKey(Things_Date, on_delete=models.CASCADE, default="")  # 外键，和事件日期相匹配

    def __str__(self):
        return self.emotion

class energy(models.Model):
    energy = models.IntegerField()
    things_date = models.ForeignKey(Things_Date, on_delete=models.CASCADE, default="")  # 外键，和事件日期相匹配

    def __str__(self):
        return self.energy

class energy(models.Model):
    energy = models.IntegerField()
    things_date = models.ForeignKey(Things_Date, on_delete=models.CASCADE, default="")  # 外键，和事件日期相匹配

    def __str__(self):
        return self.energy