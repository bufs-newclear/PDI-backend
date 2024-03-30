from django.db import models
from django.contrib.auth.models import User

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
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    name = models.CharField(max_length=100)
    meal_type = models.CharField(choices=Meal_types.choices, max_length=32)
    like_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return str(f"[{self.date}]({self.meal_type}): {self.name}")


class UserMealLike(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    meal = models.ForeignKey(UnitMenu, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        unique_together = ('user', 'meal')

    def __str__(self):
        return f"{self.user.username} likes {self.meal.name}"
