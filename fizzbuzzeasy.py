fizz = int(input('Введите fizz: ', ))
buzz = int(input('Введите buzz: ', ))
n = int(input('Введите n: ', ))
print('')
print('Fizz:', fizz)
print('Buzz: ', buzz)
print('n: ', n)
print('')
for i in range(1, n+1):
  if (i%fizz==0 and i%buzz==0):
    print('FB', end=' ')
  elif (i%fizz==0):
    print('F', end=' ')
  elif (i%buzz==0):
    print('B', end=' ')
  else:
    print(i, end=' ')
