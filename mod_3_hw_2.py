import random

def get_numbers_ticket(min=1, max=1000, quantity=4):
    try:
        if 0 < min <= 1000 and 0 < max <= 1000 and 0 < quantity <= 1000:
            win_num = random.sample(range(min, max + 1), quantity)
            win_num.sort()
            return win_num
        else:
            return
    except ValueError:
        return

print(get_numbers_ticket(2, 2000, 5))
