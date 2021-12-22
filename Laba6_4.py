List1 = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
List2 = [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]
print("Перший массив має вкладені список: ",any(isinstance(a, list) for a in List1))
print("Другий массив має вкладені списки:  ",any(isinstance(a, list) for a in List2))