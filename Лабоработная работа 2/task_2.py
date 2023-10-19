salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

safe_capital = 0
current_month_spend = spend
for _ in range(months):
    safe_capital -= salary - current_month_spend
    current_month_spend *= 1 + increase
safe_capital = int(safe_capital)

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", safe_capital)
