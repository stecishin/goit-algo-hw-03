import re

def normalize_phone(phone_number):
    num = "".join(re.findall(r"\d+", phone_number))

    if len(num) == 10:
        return "+38" + num
    elif len(num) == 12:
        return "+" + num
              
print(normalize_phone("067\\t123 4567"))