
team1_num = 5 # Кол-во участников первой команды
team2_num = 6 # Кол-во участников второй команды
score_1 = 45
score_2 = 42 # Кол-во задач решенных командой 2
team1_time = 18015.2 # Время затаченное командой 2 на решение задач
team2_time = 2153.31451
tasks_total = score_1 + score_2
time_avg = (team1_time + team2_time) / tasks_total

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = 'Победа команды Мастера кода'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result = 'Победа команды Волшебники данных'
else:
    challenge_result = 'Ничья'

# Использование %

print('В команде Мастера кода участников %d !' %team1_num)
print('Итого сегодня в командах участников %d и %d !' %(team1_num, team2_num))

# Использование format()

print(f'Команда Волшебники данных решила задач: {score_2}!'.format(score_2))
print(f'Волшебники данных решили задачи за {team1_time} сек!'.format(team1_time))

# Использование f-строк

print(f'Команды решили {score_1} и {score_2} задач')
print(f'Результат битвы: {challenge_result}!')
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg:.2f} секунды за задачу!')



