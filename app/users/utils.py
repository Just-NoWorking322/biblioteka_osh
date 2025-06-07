import random
from django.core.cache import cache

def generate_email_code(user):
    code = f"{random.randint(100000, 999999)}"
    cache.set(f'email_code_{user.id}', code, timeout=60*10)  # 10 минут хранения
    return code

def verify_email_code(user, input_code):
    real_code = cache.get(f'email_code_{user.id}')
    return input_code == real_code

def generate_reset_code():
    return str(random.randint(100000, 999999))
