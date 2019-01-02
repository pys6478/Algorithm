import sys

a, b = input().split()
a = int(a)
b = int(b)

month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day = {0:'SUN', 1:'MON', 2:'TUE', 3:'WED', 4:'THU', 5:'FRI', 6:'SAT'}

print(day[(sum(month[:(a)]) + b)%7])