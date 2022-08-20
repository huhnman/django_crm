from django.db import models

# Create your models here.
class PlateNum(models.Model):
    market_num = models.CharField(max_length=100, blank=True)
    num = models.CharField(max_length=100, blank=True)
    car_owner_name = models.CharField(max_length=100, blank=True)
    telephone_num = models.CharField(max_length=100, blank=True)
    trader_status = models.CharField(max_length=100, blank=True)
    move_ability = models.CharField(max_length=1, blank=True)
    exit_is_unrestricted = models.CharField(max_length=1, blank=True)
    country = models.CharField(max_length=100)
    comment = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    time = models.TimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.num

    # #JSON
    # def get_data(self):
    #     return {
    #         'id': self.id,
    #         'num': self.num,
    #         'country': self.country,
    #         'comment': self.comment,
    #         'author': self.author,
    #         'time': self.time
    #     }
    
    #JSON
    def get_data(self):
        return {
            'market_num': self.market_num,
            'num': self.num,
            'car_owner_name': self.car_owner_name,
            'telephone_num': self.telephone_num,
            'trader_status': self.trader_status,
            'move_ability': self.move_ability,
            'exit_is_unrestricted': self.exit_is_unrestricted,
            'comment': self.comment,
            'author': self.author,
            'time': self.time
        }