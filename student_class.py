class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        self.__grades = []

    def __str__(self):
        return '{name} - {age}: {grades}'.format(
            name=self.__name,
            age=self.__age,
            grades=' '.join('(' + str(grade) + ')' for grade in self.__grades)
        )

    def __set_name(self, name):
        if self.__name != name:
            self.__name = name

    def set_age(self, age):
        if 16 <= age < 100:
            self.__age = age

    def add_grades(self, *grades):       # (4, 6, 8, 'SDFDS')  (R=6, Y='TYUTY')
        for grade in grades:
            if 1 <= grade <= 5:
                self.__grades.append(grade)

    def __get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_grades(self):
        return self.__grades

    name = property(__get_name, __set_name)


class Group:
    def __init__(self, name):
        self.__name = name
        self.__students = []

    def add_student(self, student):
        self.__students.append(student)

    def add_students(self, *students):
        for student in students:
            self.__students.append(student)

    def show_group(self):
        for student in self.__students:
            print(student)

    def get_group(self):
        return self.__students

group = Group('New group 1')
cnt = int(input("Amount students: "))
for i in range(cnt):
     name = input("Please enter name: ")
     age = int(input("Please enter age: "))
     tmp = Student(name, age)
     group.add_student(tmp)
