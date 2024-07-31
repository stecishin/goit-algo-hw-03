import random

def get_numbers_ticket(min=1, max=1000, quantity=4):
    try:
        if 0 < min <= 1000 and 0 < max <= 1000 and 0 < quantity <= 1000:
            win_num = random.sample(range(min, max + 1), quantity)
            win_num.sort()
            return win_num
        else:
            return f"Потрібно вводити числа від 1 до 1000 включно!"
    except ValueError:
        return f"Некоректні дані! Правила вводу: (max - min) >= quantity < max > min "

print(get_numbers_ticket(11, 20, 5))
