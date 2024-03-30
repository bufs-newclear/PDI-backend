# models.py

from django.db import models

class DailyMenu(models.Model):
    date = models.DateField(unique=True)  # 날짜 필드를 고유하게 설정하여 하루에 한 번만 메뉴를 등록할 수 있도록 함
    breakfast_menu = models.CharField(max_length=100)
    lunch_menu_1 = models.CharField(max_length=100)
    lunch_menu_2 = models.CharField(max_length=100)
    lunch_menu_3 = models.CharField(max_length=100)

    def __str__(self):
        return str(self.date)