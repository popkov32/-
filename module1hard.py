grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3],
          [5, 5, 5, 4, 5]]  # вх данные оценки студентов типа list "список"
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}  # вх данные перечень студентов типа set "множество"
students = sorted( students )  # перевод students типа set в сортированный тип list
new_grades = [(sum( grades[0] ) / len( grades[0] )), (sum( grades[1] ) / len( grades[1] )),
              (sum( grades[2] ) / len( grades[2] )), (sum( grades[3] ) / len( grades[3] )),
              (sum( grades[4] ) / len( grades[4] ))]
# создание списка new_grades путем расчета средних оценок студентов: сумма оценок из списка grades деленая на кол-во оценок с соотв индексом студента
book = dict( zip( students, new_grades ) ) # создание словаря book путем объединения списков students и new_grades
print( book )  # вывод словаря book
