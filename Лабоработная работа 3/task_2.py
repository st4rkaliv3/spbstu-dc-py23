def find_common_participants(participants1, participants2, delimiter=','):
    commons = list(set(participants1.split(delimiter)).intersection(participants2.split(delimiter)))
    commons.sort()
    return commons

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
print(find_common_participants(participants_first_group, participants_second_group, delimiter='|'))
