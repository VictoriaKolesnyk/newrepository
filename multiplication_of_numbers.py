def multiplication_of_number(number):
    s = str(number)
    res = sum([int(el) * idx for idx, el in enumerate(s, 1)])
    return( res )

number =int(input('please enter a number  '))
print(multiplication_of_number(number))