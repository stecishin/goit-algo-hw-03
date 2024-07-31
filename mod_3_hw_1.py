from datetime import datetime

def get_days_from_today(date):
    try:
        return  datetime.today().date().toordinal() - datetime.strptime(date, "%Y-%m-%d").date().toordinal()
    except ValueError:
        return f"Введено некоректно! Дотримуйтесь шаблону 'РРРР-ММ-ДД'"

print(get_days_from_today("2023-08-29"))