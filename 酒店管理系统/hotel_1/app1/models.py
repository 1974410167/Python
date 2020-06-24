from django.db import models

# Create your models here.

class House(models.Model):

    HOUSE_TYPE = [
        ('Standard_room','标间'),
        ('Double_room','大床房'),
        ('Couples_room','情侣房'),
        ('Suite','套房'),
    ]

    house_type = models.CharField(max_length=128,choices=HOUSE_TYPE,default=HOUSE_TYPE[0][0])  # 房间类型，默认为标间
    is_check_in = models.BooleanField(default=False)       # 是否入住，默认为否
    price = models.IntegerField(null=False)                # 价格

    def __str__(self):
        return self.house_type

class Customer(models.Model):

    GENDER = [
        ('man','男'),
        ('woman','女'),
    ]

    name = models.CharField(max_length=128,null=False,blank=False)      # 姓名
    gender = models.CharField(max_length=10,choices=GENDER,default=GENDER[0][0])   # 性别，默认为男
    phone = models.CharField(max_length=11)                 # 手机号
    id_card =models.CharField(max_length=18)                  # 身份证
    House_id = models.ForeignKey(House,on_delete=models.CASCADE)    # 外键

    # def set_is_check_in(self):
    #     self.House_id.is_chcek_in


    def __str__(self):
        return self.name