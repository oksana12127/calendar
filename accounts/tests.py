import datetime

from django.test import TestCase

# Create your tests here.
# def fibonacci(n):
#     a = 0
#     b = 1
#     if n <= 0:
#         print("Incorrect input")
#     elif n == 1:
#         return b
#     else:
#         for i in range(2, n):
#             c = a + b
#             a = b
#             b = c
#         return b
#
#
# print(fibonacci(12))


# def fibonacci(n):
#     if n in (1, 2):
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
#
# print(fibonacci(4))



# def palindrom(word):
#     if word == "".join(reversed(word)):
#         return print(True)
#     else:
#         return print(False)
#
# palindrom('okko')


# def Fizz_Buzz(x):
#     for x in range(1, x+1):
#         if x % 3 == 0 and x % 5 == 0:
#             print('FizzBuzz')
#         elif x % 3 == 0:
#             print('Fizz')
#         elif x % 5 == 0:
#             print('Buzz')
#         else:
#             print(x)
#
# Fizz_Buzz(20)


# def vowel(s):
#     vowels = 'aeiou'
#     count = 0
#     for letter in s.lower():
#         if letter in vowels:
#             count = 1 + count
#     print(count)
#
# vowel('omohouruyuy')




# def anagram(s1, s2):
#     s1 = "".join(sorted(s1))
#     s2 = "".join(sorted(s2))
#     if s1 == s2:
#         print('anagram')
#     else:
#         print(False)
#
# anagram('kot', 'tok')


#
# def fibonacci(n):
#     a = 0
#     b = 1
#
#     if n <= 0:
#         print("Incorrect input")
#     elif n == 1:
#         print(b, end=' ')
#         return b
#     else:
#         print(1, end=' ')
#         for i in range(1, n):
#             c = a + b
#             a = b
#             b = c
#             print(b, end=' ')
#         return b
#
# (fibonacci(7))
# print('')
#
#
# def list_sum(a):
#     i = 0
#     sum = 0
#     while i < len(a):
#         sum = sum + a[i]
#         i += 1
#     return print(sum)
#
#
# list_sum([1, 3, 5, 8, -3, 10])
#
#
#
#
# def more_them_a(a):
#     n = 2
#     b = 1 + 1 / n
#     while b > a:
#         print(b, end=' ')
#         n = n + 1
#         b = 1 + 1 / n
#
#
# more_them_a(1.3)
#
#
# print('')


# print(datetime.datetime(int(input('Год: ')), 1, 1) + datetime.timedelta(int(input('Номер дня: ')) - 1))

t = (input('Номер дня: '))
year = datetime.datetime(int(input('Год: ')), 1, 1)

print(year + datetime.timedelta(int(t) - 1))

def date_of_year(t):
    start_year_day_week = year.weekday()
    date_year = 1
    week = ["пн", "вт", "ср", "чт", "пт", "сб", "вс"]
    while date_year < (int(t)):
        date_year += date_year
        start_year_day_week += start_year_day_week
        if start_year_day_week > 7:
            start_year_day_week = 1

    print(week[start_year_day_week])


date_of_year(t)
