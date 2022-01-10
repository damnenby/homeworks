import sys
from random import randrange


def createRandomArr(n, min, max):
    arr2d = []
    for i in range(1, n + 1):
        arr2d.append([randrange(min, max), randrange(min, max), randrange(min, max)])
    return arr2d


def fizzbuzz(fizz, buzz, n):
    result = ''
    for i in range(1, n + 1):
        if (i % fizz == 0 and i % buzz == 0):
            result += 'FB '
        elif (i % fizz == 0):
            result += 'F '
        elif (i % buzz == 0):
            result += 'B '
        else:
            result += str(i) + ' '
    return result


f = open('fizzbuzz.txt', 'r')
w = open('results.txt', 'w')
for line in f:
    arr = line.split(' ')
    intarr = []
    for item in arr:
        intarr.append(int(item))
    print(fizzbuzz(intarr[0], intarr[1], intarr[2]))
    w.write(fizzbuzz(intarr[0], intarr[1], intarr[2]) + '\n')







