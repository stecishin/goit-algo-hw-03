import re


phone_number = [
    "    +38(050)123-32-34", "     0503451234", "(050)8889900",
    "38050-111-22-22", "38050 111 22 11   ", "067\\t123 4567",
    "(095) 234-5678\\n", "+380 44 123 4567", "380501234567",
    "    +38(050)123-32-34", "     0503451234", "(050)8889900",
    "38050-111-22-22", "38050 111 22 11   "
]



def normalize_phone(phone_number):
    phone_well = []
    phone_number_only = []
    for phone in phone_number:
        phone_number_only.append(re.sub(r"\D+", "", phone))

    for phone_full_num in phone_number_only:
        if len(phone_full_num) == 10:
            phone_well.append("+38" + phone_full_num)
        elif len(phone_full_num) == 12:
            phone_well.append("+" + phone_full_num)
              
    return phone_well


print(normalize_phone(phone_number))