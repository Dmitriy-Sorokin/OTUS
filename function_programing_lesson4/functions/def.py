import inspect


#  Объявление функции
def base_function():
    pass  # Тело функции


def advanced_function(arg) -> str:  # Имя финкции. # Анатация функции
    '''Док стринга функции'''
    return arg  # Возвращение значения


print("=== ФУнция является объектом ===")
print(dir(advanced_function))
print("name:", advanced_function.__name__)
print("code:", advanced_function.__code__)
print("type:", type(advanced_function))

print("=== Использование функции как обект первого класса ===")
# Хранить в структурах данных
my_functions = [base_function, advanced_function, 10, None]
print(my_functions)

#Возвращать функции
result = advanced_function(base_function)
print(result.__name__)


