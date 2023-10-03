# #task 1
# try:
#    num = int(input())
#    first_num = num // 1000
#    second_num = (num // 100) % 10
#    third_num = (num // 10) % 10
#    last_num = num % 10
#    if ((first_num + last_num) == (second_num - third_num)):
#       print('yes')
#    else:
#       print('no')
# except ValueError:
#    print('error')

# #task 2
# try:
#    age = int(input())
#    if (age >= 18 <= 110):
#       print('access allowed')
#    else:
#       print('access denied')
# except ValueError:
#    print('error')

# # task 3
# try:
#    num1 = int(input())
#    num2 = int(input())
#    num3 = int(input())
#    if num2 - num1 == num3 - num2:
#       print("YES")
#    else:
#       print("NO")
# except ValueError:
#    print('error')

# # task 4
# try:
#    r1 = int(input())
#    l1 = int(input())
#    r2 = int(input())
#    l2 = int(input())
#    if( 0 < r1 and r2 and l1 and l2 <= 8):
#       if (l1 == l2):
#          print('YES')
#       elif (r1 == r2):
#          print('YES')
#       else:
#          print('NO')
#    else:
#       print('NO')
# except ValueError:
#    print('error')

# # task 5
# try:
#    r1 = int(input())
#    l1 = int(input())
#    r2 = int(input())
#    l2 = int(input())

#    if( 0 < r1 <= 8 and 0 < l1 <= 8 and 0 < r2 <= 8 and 0 < l2 <= 8):
#       if (abs(l1 - l2) <= 1 & abs(r1 - r2) <= 1):
#          print('YES')
#       else:
#          print('NO')
#    else:
#       print('NO')
# except ValueError:
#    print('error')

# # task 6
# try:
#    num1 = int(input())
#    num2 = int(input())
#    num3 = int(input())
#    max_num = max(num1, num2, num3)
#    min_num = min(num1, num2, num3)
#    average = num1 + num2 + num3 - max_num - min_num
#    print(average)
# except ValueError:
#    print('error')

# # task 7 
# try:
#    month = int(input())
#    if (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 12):
#       print(31)
#    elif (month == 4 or month == 6 or month == 9 or month == 11):
#       print(30)
#    elif (month == 2):
#       print(28)
#    elif (month > 12 or month == 0):
#       print('you serious?')
# except ValueError:
#    print('error')

# # task 8
# try:
#    weight = int(input())
#    if ( 30 < weight <= 60 ):
#       print('Light weight ')
#    elif ( 61 < weight <= 64 ):
#       print('First welterweigh')
#    elif ( 65 < weight <= 69 ):
#       print('Welterweight ')
#    elif (weight > 69 or weight < 30):
#       print('I never thought about it')
# except ValueError:
#    print('error')

# # task 9 
# try:
#    password1 = str(input())
#    password2 = str(input())
#    if (password1 == password2):
#       print('Password accepted ')
#    else:
#       print('Password not accepted ')
# except ValueError:
#    print('error')

# # task 10
# try:
#    number = int(input())
#    if ( number % 2 != 0 ):
#       print('Odd number ')
#    else:
#       print('Even value ')
# except ValueError:
#    print('error')

# # task 11
# try:
#    num1 = int(input())
#    num2 = int(input())
#    min_number = min(num1, num2)
#    print(min_number)
# except ValueError:
#    print('error')

# # task 12
# try:
#    age = int(input())
#    if (age <= 13):
#       print('inclusive-childhood')
#    elif (14 <= age <= 24):
#       print('youth')
#    elif (25 <= age <= 59):
#       print('maturity')
#    elif (age >= 60):
#       print('old age')
# except ValueError:
#    print('error')

# # task 13
# try:
#    k1 = int(input())
#    k2 = int(input())
#    g = int(input())
#    if (k1 == k2 and k1 != g) :
#       print('Isosceles')
#    elif (k1 == g and k2 == g):
#       print('Equilatera')
#    else:
#       print('Versatile')
# except ValueError:
#    print('error')