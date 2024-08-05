def get_matrix(n, m, value):  #объявляем функцию с параметрами
    matrix = []  #создаем пустой список
    for i in range( n ):  #первый (внешний) цикл для строк матрицы
        matrix.append( [] )  #добавляем пустой список в список matrix
        for j in range( m ):  #второй (внутренний)цикл для столбцов
            matrix[i].append( value )#пополнение ранее добавл пустого списка значениями value
    print( matrix )
get_matrix( 2, 2, 10 )
get_matrix( 3, 5, 42 )
get_matrix( 4, 2, 13 )

