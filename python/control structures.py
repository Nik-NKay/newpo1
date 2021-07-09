my_boolean = True
print(my_boolean)


print(2 == 3)

print('hello' == 'hello')

print(1 != 1)

if 10 > 5:
    print('10 greater than 5')

    num = 12
    if num > 5:
        print('bigger than 5')
        if num <= 47:
            print('between 5 and 47')

            num_1 = 7
            if num_1 > 3:
                print('3')
                if num_1 < 5:
                    print('5')
                    if num_1 == 7:
                        print('7')


x = 4
if x == 5:
    print('yes')
else:
    print('no')


y = 3
if y == 1:
    print('one')
else:
    if y == 2:
        print('two')
    else:
        if y == 3:
            print('three')
        else:
            print('something else')


b = 4
if b == 1:
    print('one')
elif b == 2:
    print('two')
elif b == 3:
    print('three')
else:
    print('something else')

    # boolen logic class (and, or, not)

    if (1 == 1) and (2+2 > 3):
        print('true')
    else:
        print('false')

print(1 == 1 or 2 == 2)
print(1 == 1 or 2 == 3)
print(1 != 1 or 2 == 2)
print(2 < 1 or 3 > 6)


age = 15
money = 500
if age > 18 or money > 100:
    print('welcome')


print(not 1 == 1)
print(not 1 > 7)


if not True:
    print('1')
elif not (1+1 == 3):
    print('2')
else:
    print('3')

    # operator precedence

    print(False == False or True)

    if 1+1*3 == 6:
        print('yes')
    else:
        print('no')


grade = 88
if (grade >= 70 and grade <= 100):
    print('Passed!')

    g = 4
    o = 2
    if not 1+1 == o or g == 4 and 7 == 8:
        print('yes')
    elif g > o:
        print('No')
