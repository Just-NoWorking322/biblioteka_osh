# from django.utils import timezone
# from django.contrib.auth import get_user_model
# from .models import Stats

# User = get_user_model()

# class StatsUpdateMixin:
#     """
#     Миксин для обновления статистики при каждом запросе.
#     """
#     def update_stats(self):
#         visit, created = Stats.objects.get_or_create(id=1)

#         # Увеличиваем значения
#         visit.views += 1
#         visit.shares += 1
#         visit.users += 1

#         # Проверяем пользователя
#         if self.request.user.is_authenticated:
#             user = self.request.user
#             user.last_activity = timezone.now()
#             user.save()

#         visit.save()
#         return visit
