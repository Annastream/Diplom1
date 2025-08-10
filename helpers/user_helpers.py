import random
import string

def generate_random_string(length):
   #Генерирует случайную строку из букв нижнего регистра
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

def generate_user_data(email_suffix="@example.com"):
    #Генерирует данные пользователя
    email = f"{generate_random_string(10)}{email_suffix}"
    password = generate_random_string(12)
    name = generate_random_string(8)
    return {
        "email": email,
        "password": password,
        "name": name
    }

