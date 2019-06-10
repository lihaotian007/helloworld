"""
s = 'Now is better than never.'
s.swapcase() # 逐个字符更替大小写
s.title() 
s.title().swapcase() 
s.upper().swapcase()
"""

# exercise in part.1.E.6.containers
# the purpose is that exercise the different of mutable and immutable
"""
s = 'lt\'s a nice day'
for i in range(len(s)) :
    s[i] = str(i)
"""
# exercise in part.1.E.6.containers
# the purpose is that to determine the rules for collation
"""
a_list = ['100', 78, 83, 88, 78, 83, 88, 'L', 'C', 'A', 78, 'example', 83, 'example', 88]
for i in range(len(a_list)-1):
    if str(a_list[i]) > str(a_list[i+1]):
        print(f'{a_list[i]} > {a_list[i+1]} is True')
    else:
        print(f'{a_list[i]} > {a_list[i+1]} is False')

a_list.sort(key=str, reverse=False)
print(a_list)

import random
a_list = [random.randrange(65, 91) for i in range(10)]
print(a_list)
a_list.reverse()
print(a_list)

import random
a_list = [random.randrange(65, 91) for i in range(10)]
print(a_list)
a_list.pop(2)
print(a_list)
a_list.remove(a_list[2])
print(a_list)
"""

# exercise in1.5.6 - Tuple
'''
a = 2,
print(a)
print(id(a))
a += 3,5
print(a)
print(id(a))
'''

'''
a = "abcdeashfoafnlksadmciosnfoen"
b = {x for x in a if x not in 'abc'}
c = set(a)
print(b)
print(c)
b.remove('h')
print(b)
'''

"""
chars = 'abcdefghijklmnopqrstuvwxyz'
nums = range(1, 25)
for c, n in zip(chars, nums):
    print(f"Let's assume {c} represents {n}.")
"""

"""
def sum_of_word(word):
    sum = 0
    for char in word:
        sum += (ord(char) - 96)
    return sum

i = 0
with open('D:/GitHub - Desktop/helloworld/the-craft-of-selfteaching/file/Result.txt','w') as result:
    with open('D:/GitHub - Desktop/helloworld/the-craft-of-selfteaching/file/Word_English.txt','r') as files:
        for word in files.readlines():
            if sum_of_word(word.strip()) == 100:
                result.writelines(word)
"""

"""
import sys

n = 100
if sys.argv[1:]: # sys.argv是什么？
    n = int(sys.argv[1]) # 为什么不是0

def bottle(n):
    if n == 0: return "no more bottles of beer"
    if n == 1: return "one bottle of beer" # 为什么要增加这句，好像可以去掉
    return str(n) + " bottles of beer"

for i in range(n, 0, -1):
    print(bottle(i), "on the wall,")
    print(bottle(i) + ".")
    print("Take one down, pass it around,")
    print(bottle(i-1), "on the wall.")
"""

"""
words = ['cat', 'window', 'defenestrate']
i = 0
for w in words:  # Loop over a slice copy of the entire list.
    if len(w) > 6:
        words.insert(0, w)
    if i > 10:
        break
    else:
        i += 1
print(words)
"""

"""
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda p: p[1])
print(pairs)
"""

"""
import random

a = []

for i in range(100):
    a.append(not random.randrange(0,10))

print(a)
"""

"""
def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

print(is_leap(4) is True)
print(is_leap(200) is False)
print(is_leap(220) is True)
print(is_leap(400) is True)
"""

"""
import this
print(id(this))
love = this
print(id(love))
"""

"""
with open('D:/GitHub - Desktop/helloworld/the-craft-of-selfteaching/file/exce.txt','w') as f :
    print('123456', file = f, flush = False)
"""

"""
def counter(start, stop):
    while start <= stop:
        yield start
        start += 2
        yield start
        start -= 1
for i in counter(101, 105):
    print(i)
"""

"""
modified_restult = '<strong>'+'original_result'+'</strong>'

print(modified_restult.upper())
"""

"""
n = input(
'You are in the lost Forest\n \
***************************\n \
***************************\n \
   :)                      \n \
***************************\n \
***************************\n \
Go   Left   or   Right  ?  \n')

while n == 'right' or n == 'Right':
    n = input('You are in the lost Forest\n***************************\n***************************\n   :)                      \n***************************\n***************************\nGo   Left   or   Right  ?\n')
print('\nYou got out of the Lost Forest')
"""
"""
def is_prime(n):
  if n < 2:
    return False
  elif n == 2:
    return True
  else:
    for i in range(2,int(n**0.5)+1):
      if n % i == 0:
        return False
    else:
      return True

for i in range(1,100):
  if is_prime(i):
    print(i)
"""
"""
# print(abs(3.5+5.3j))

for i in range(ord('a'),ord('z')+1):
  print(i, end=' ')
print()
for i in range(ord('A'),ord('Z')+1):
  print(i, end=' ')
"""
'''
# The program solve cube root problem by dichotomous method

def dichotomous(cubic_num, precision):
  low = 0.0
  if cubic_num > 1.0:
    high = cubic_num
  else:
    high = 1.0
  cube_root = (low+high)/2
  while abs(cube_root ** 3 - cubic_num) > precision:
    if cube_root ** 3 > cubic_num:
      high = cube_root
    else:
      low = cube_root
    cube_root = (low+high)/2
  return cube_root

cir = 'yes'
while cir == 'yes':
  print('The program solve cube root problem by dichotomous method')
  cubic_num = float(input('please input the cubic number:'))
  precision = float(input('please input the precision:(example:0.01)'))
  if precision == 0:
    precision = 1.0
  print(f'The cube root of {cubic_num} is',dichotomous(cubic_num, precision))
  cir = input('Do you want keep this program?[yes/no]:\n')
    '''