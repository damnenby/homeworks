
from random import randrange
import sys

n = int(input('Введите количество строк: '))
min = int(input('Введите минимальное значение для случайного числа: '))
max = int(input('Введите максимальное значение для случайного числа: '))

def createRandomArr(n, min, max):
  arr2d = []
  for i in range(1,n+1):
    arr2d.append([randrange(min, max),randrange(min, max),randrange(min, max)])
  return arr2d

arr = createRandomArr(n, min, max)

def createStr(arr):
  string = ''
  for item in arr:
    temp = ' '.join(map(str, item))
    string = string + temp + '\n'
  return string

w = open('fizzbuzzes.txt', 'w')
w.write(createStr(arr))

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


f = open('fizzbuzzes.txt', 'r')
w = open('results.txt', 'w')
for line in f:
  arr = line.split(' ')
  intarr = []
  for item in arr:
    intarr.append(int(item))
  print(fizzbuzz(intarr[0], intarr[1], intarr[2]))
  w.write(fizzbuzz(intarr[0], intarr[1], intarr[2]) + '\n')
