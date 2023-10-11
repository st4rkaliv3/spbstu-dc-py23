list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# Разделите участников на две команды
half_players = int(len(list_players) // 2)
teamA = list_players[:half_players]
teamB = list_players[half_players:]
print(teamA)
print(teamB)
