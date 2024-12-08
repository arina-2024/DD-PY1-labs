# TODO Напишите функцию find_common_participants
def find_common_participants(group_1, group_2, arg=","):
    participants_1 = set(group_1.split(arg))
    participants_2 = set(group_2.split(arg))

    common_participants = list(set(participants_1).intersection(participants_2))
    common_participants.sort()

    return common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, "|"))
# TODO Провеьте работу функции с разделителем отличным от запятой

