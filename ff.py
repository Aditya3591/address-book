# lst = []

# for i in range(10):
#     lst.append(i)
    
# print(lst)

# lst = [num for num in range(10)]
# print(lst[2:4])

# dct = {i: i**2 for i in range(10)}
# print(dct)
# try:
#     a = int(input())
# except ValueError as e:
#     print('Value error')
# except Exception as e:
#     print(e)
# else:
#     print("try executed successfully")
# finally:
#     print('123')
    

# class MyException(Exception):
    
#     def __init__(self, message, *args: object) -> None:
#         self.message = f'Error: {message}'
        
#     def __str__(self) -> str:
#         return self.message
    
# try:
#     a = input('Enter str:')
#     if a == 'a':
#         raise MyException('Raised my custom exception')
# except MyException as e:
#     print(e)
# finally:
#     print()


# def sum_(a,b,*args, **kwargs):
#     print(args)
#     print(kwargs)
#     return a + b + sum(args) + sum(kwargs.values())
# x = 100
# print(sum_(10, 20, 30, 40, 50, x, y=200))

class User:
    
    def __init__(self, name, value, **kwargs) -> None:
        self.name = name
        self.value =value
        print(kwargs)

data = {'name': 'Nutan', 'value': 'Kumar'}     
obj = User(**data, age=22)


def power_of_two(value):
    return value ** 2

lst = list(map(power_of_two, [1, 2, 3, 4, 5]))
print(tuple(lst))

lst = list(filter(lambda x: x%2==0, lst))
print(lst)   

from functools import reduce

value = reduce(lambda x, y: x+y, lst)
print(value)
