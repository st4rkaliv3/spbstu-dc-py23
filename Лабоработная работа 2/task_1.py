money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

months = 0
current_month_spend = spend
while True:
    money_capital += salary - current_month_spend
    if money_capital < 0:
        break
    current_month_spend *= 1 + increase
    months += 1

print("Количество месяцев, которое можно протянуть без долгов:", months)
