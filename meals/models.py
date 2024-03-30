from django.db import models

# class DailyMenu(models.Model):
#     # 날짜 필드를 고유하게 설정하여 하루에 한 번만 메뉴를 등록할 수 있도록 함
#     date = models.DateField(unique=True)
#     breakfast_menu = models.CharField(max_length=100)
#     lunch_menu_1 = models.CharField(max_length=100)
#     lunch_menu_2 = models.CharField(max_length=100)
#     lunch_menu_3 = models.CharField(max_length=100)

#     def __str__(self):
#         return str(self.date)


class UnitMenu(models.Model):
    Meal_types = models.TextChoices('Meal_types', 'morning lunch employee')
    # Permissions = (
    #     ("can_edit", "Can edit the content"),
    # )
    date = models.DateField()
    name = models.CharField(max_length=100)
    meal_type = models.CharField(choices=Meal_types.choices, max_length=32)

    def __str__(self):
        return str(f"[{self.date}]({self.meal_type}): {self.name}")
