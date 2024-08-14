# Задание "Раз, два, три, четыре, пять .... Это не всё?".
def calculate_structure_sum(data_structure): #Определение ф-ции
    summa = 0 #Начальное значение искомой суммы
    if isinstance(data_structure, dict): #Проверка наличия во входных данных словарей
        #print('dict', data_structure)
        for key, value in data_structure.items():
            summa += calculate_structure_sum(key)
            summa += calculate_structure_sum(value)
    elif isinstance(data_structure, (list, tuple, set)):
        #print('List, tuple, set', data_structure)
        for item in data_structure:
            summa += calculate_structure_sum(item)
    elif isinstance(data_structure, (int, float)):
        #print('int, float', data_structure)
        summa += data_structure
    elif isinstance(data_structure, str):
        #print('str', data_structure)
        summa += len(data_structure)
    return summa


data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)