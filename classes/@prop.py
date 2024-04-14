# Требуется реализовать на языке Python класс Student со свойством name с геттером и сеттером.

class Student:

    def __init__(self):
        self.__name = ''

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, set_name):
        if not isinstance(set_name, str) or not all(i.isspace() or i.isalpha() for i in set_name):
            raise ValueError()
        self.__name = set_name

student = Student()
student.name = 'hfihrjeh'
print(student.name)
# print(isinstance(213, str))

# Сеттер свойства name должен позволять присваивать только строки, состоящие из пробелов и букв
# английского алфавита(в любом регистре), в остальных случаях требуется бросать исключение ValueError.