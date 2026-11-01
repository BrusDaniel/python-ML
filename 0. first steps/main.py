#ZJAZD 2


#1 MAIN TASKS




'''from random import random

def points_to_grade (points):
    if points<=50:
        return 2
    elif points<=70:
        return 3
    elif points<=85:
        return 4
    else:
        return 5

my_points = [int(random()*100) for i in range(10)]
print(my_points)
points_and_grades = {point: points_to_grade(point) for point in my_points}
print(points_and_grades)
print("srednia: ", sum(my_points)/len(my_points), sum(points_and_grades.values())/len(points_and_grades))
count_of_positive = 0
print(len([x for x in my_points if x>50]))
print("maxes:", end=' ')
for i in range(3):
    print(max(my_points), end=' ')
    my_points[:].remove(max(my_points))
    print('\n')
from random import random

systems_num = int(random()*100)
users_num = int(input())
count = 1
numbers =[]
numbers.append(users_num)
while users_num != systems_num:
    if users_num < systems_num:
        print("increase your number")
    else:
        print("decrease your number")
    users_num = int(input())
    count += 1
    numbers.append(users_num)
else:
    print("win!")
    print(numbers)
    print(
        count
    )
    print(numbers[-3:])



from random import random

random_L = [int(random()*10) for i in range(10)]
print(random_L)
random_S = set(random_L)
print(random_S)
print(max(random_S), min(random_S))
print(sum(random_L)/len(random_L))
print(len([x for x in random_L if x>sum(random_L)/len(random_L)]))
print(sorted(random_S)[-2])

i = ""
products_and_prices = {}
while True:
    i = input("put product[space]price:\n")
    if i == "stop": break
    a, b = i.split()
    if a.isdigit():
        products_and_prices[b] = int(a)
    else:
        products_and_prices[a] = int(b)
print(products_and_prices)
print("overall cost: ", sum(products_and_prices.values()))
print("most expensive: ", int(max(products_and_prices.values())))
print(sum(products_and_prices.values())/len(products_and_prices.values()))

users_list = {'k': 4, 'a': 3}
def add_user (**kwargs):
    for name, score in kwargs.items():
        users_list[name] = score
def is_exist (name):
    if name in users_list: return True
    else: return False
users_list = {name : users_list[name] for name in sorted(users_list)}
print(users_list)
name = input()
print(users_list.get(name, "not exist"))
max_user = ("",)
for name in users_list:
    if len(name)>len(max_user[0]):
        max_user = (name,users_list[name])
print(max_user)

from random import choice

choices = []
user_wins = 0
user_fails = 0
user_remises = 0
rounds = input('how many rounds?')
choices_dict = {1: 'rock', 2: 'scissors', 3: 'paper'}
for i in range(int(rounds)):
    user_choice = 0
    while int(user_choice) not in list(range(1,4)):
        user_choice = int(input('enter 1 if rock, 2 if scissors, 3 if paper'))
    computer_choice = int(choice(list(range(1,4))))
    choices.append(f"computer={choices_dict[computer_choice]} vs. user={choices_dict[user_choice]}")
    if user_choice == 1 and computer_choice == 2:
        user_wins += 1
        print("win")
    elif user_choice == 2 and computer_choice == 1:
        user_fails += 1
        print("fail")
    elif user_choice == 2 and computer_choice == 3:
        user_wins += 1
        print("win")
    elif user_choice == 3 and computer_choice == 2:
        user_fails += 1
        print("fail")
    elif user_choice == 3 and computer_choice == 1:
        user_wins += 1
        print("win")
    elif user_choice == 1 and computer_choice == 3:
        user_fails += 1
        print("fail")
    else:
        user_remises+=1
        print("remise")
print(choices)
print(f"your_wins: {user_wins}, your_fails: {user_fails}, your_remises: {user_remises}")
if user_wins>user_fails:
    print("YOU WIN!")
elif user_wins<user_fails:
    print("YOU LOSE!")
else:
    print("REMIS!")


N = int(input("enter number:\n"))
lst = list(range(1, N+1))
def is_even (num):
    if num % 2 == 0:
        return True
    else:
        return False
def my_filter (func, lst):
    return [x for x in lst if func(x)]
print(my_filter(is_even, lst))



names = [
    "John", "Mary", "Kitty", "Alice", "John",
    "Mary", "Al", "Bill", "John", "Alice", "Al"
]
names_len = [len(name) for name in names]
print(names_len)
names_len_dict = {}
for name in names:
    if names_len_dict.get(len(name), 0):
        names_len_dict[len(name)].append(name)
    else:
        names_len_dict[len(name)] = [name]
print(names_len_dict)
for amount in names_len_dict:
    names_len_dict[amount] = set(names_len_dict[amount])
print(names_len_dict)
last_dict = {}
for name in names:
    if last_dict.get(name, 0):
        last_dict[name]+=1
    else:
        last_dict[name] = 1
print(last_dict)



N = int(input("enter numbers amount:\n"))
my_set = set()
more_than_one_time = []
while True:
    old_len = len(my_set)
    i = int(input("enter number:\n"))
    my_set.add(i)
    new_len = len(my_set)
    if old_len == new_len:
        more_than_one_time.append(i)
    if len(my_set) == N:
        break
print(my_set)
print(more_than_one_time)



def reverse_winners_list (winners_dict: dict):
    #name, wins_amount = winners_dict.items()
    reversed_winners_dict = {}
    for name in winners_dict:
        if reversed_winners_dict.get(winners_dict[name], 0):
            reversed_winners_dict[winners_dict[name]].append(name)
        else:
            reversed_winners_dict[winners_dict[name]] = [name]
    print(reversed_winners_dict)
    print(sorted(list(zip(
        reversed_winners_dict, reversed_winners_dict.values())),
        reverse=True))

dct = {'John': 3, 'Bill': 4, 'Jane': 4, 'Kim': 2,
       'Mary': 3, 'Joe': 0, 'Sue': 5, 'Ada': 2, 'Ray': 2}

reverse_winners_list(dct)


import time
import timeit
from curses import wrapper
from itertools import count
from random import random
from textwrap import dedent

#2 FOR
'''
"""

for i in range(1, 10):
    print(i, end=' ')
print()

for i in list(range(1, 10))[::-1]:
    print(i, end=' ')
print()


for i in range(1, 20):
    if i % 2 == 0:
        print(i, end=' ')
print()

summ = 0
for i in range(1, 10):
    summ += i
print(summ)

for s in "Python":
    print(s)

text = "dlf,e  v\tledl,elw95\n   93nmmf\ap2[ ;epe"
count = 0
for s in text:
    count += 1
print(count)

digit_count = 0
for s in text:
    if s.isdigit():
        digit_count += 1
print(digit_count)

digit_sum = 0
for s in text:
    if s.isdigit():
        digit_sum += int(s)
print(digit_sum)

for num in range(1, 50):
    if num % 3 == 0:
        print(num, "<-(Divisible by 3)", end=' ', sep='')
    elif num % 5 == 0:
        print(num, "<-(Divisible by 5)", end=' ', sep='')
    else:
        print(num, end=' ')
print()

for num in range(1, 100):
    if num % 7 != 0:
        print(num, end=' ')
print()

maxx=0
for num in [3, 7, 2, 9, 4, 5]:
    if num > maxx:
        maxx = num
print(maxx)

for num in [5, 12, 7, 18, 3, 21]:
    if num > 10:
        count += 1
print(count)

for a in range(1, 11):
    for b in range(1, 6):
        print(a, "*", b, "=", a*b, end='\t'*3)
    print()

for a in range(1, 6):
    print("*  "*5,)

n = 4657
czy_pierwsza = False
for a in range(2, n):
    if n % a == 0:
        czy_pierwsza = True
if czy_pierwsza: print(n, "pierwsza")
else: print(n, "nie pierwsza")


for a in range(1, 100):
    if a % 3 == 0 and a % 5 == 0:
        print(a, end=' ')
print()

count=0
for a in text:
    if a in "eyuioa":
        count += 1
print("amount of vowels:", count)

for s in text:
    if not s.isspace():
        print(s, end='')
print()

for s in text[::-1]:
    print(s, end='')
print()

letters_amount = {}
for s in text:
    letters_amount[s] = letters_amount.get(s, 0) + 1
print(letters_amount)

minn = 1000
for num in [8, 3, 15, 2, 9, 11]:
    if num < minn:
        minn = num
print(minn)

mull = 1
for num in [1, 2, 3, 4, 5]:
    mull *= num
print(mull)

for num in range(2, 100):
    czy_pierwsza = True
    for num2 in range(2, num):
        if num % num2 == 0:
            czy_pierwsza = False
            break
    if czy_pierwsza:
        print(num, end=' ')
print()



for i in range(1, 6):
    print("*"*i)

for i in list(range(1, 6))[::-1]:
    print("*"*i)

for i in [1, 2, 3, 4]:
    for j in [1, 2, 3, 4]:
        print((i,j), end=' ')
print()

maxx = 0
almost_max = 0
for num in [10, 5, 8, 20, 3, 15]:
    if num > maxx:
        almost_max, maxx = maxx, num
print(almost_max)

for s in "hHkCMLDMkKkdo":
    if s.islower() and s.isalpha():
        print(chr(ord(s)-32), end='')
        continue
    print(s, end='')
print()


for s in "hHkCMLD7879548774Mk55Kkdo":
    if not s.isdigit():
        print(s, end='')
print()


count = 0
summ = 0
for num in [4, 8, 15, 16, 23, 42]:
    count += 1
    summ += num
print(summ/count)
"""

'''
#3 WHILE

summ = 0
while True:
    i = int(input())
    if i == 0:
        break
    summ+=i
print(summ)


count = 0
while True:
    i = int(input())
    if i < 0:
        break
    count+=1
print(count)


i = 1
while i!=0:
    i = int(input())
else:
    print("End of data input")


summ = 0
while True:
    i = int(input())
    if i < 0:
        break
    summ+=i
print(summ)



while (x:=10) in [3, 7, 4, 8, 2]:
    break
else:
    print("Number not found")


while (word:=input()) !="python":
    pass
else:
    print('Logged in')


i = 0
text = 'jhksla84hkkmv'

while i < len(text):
    if text[i].isdigit():
        break
else:
    print("No digits")


while (x:=int(input())) != 0:
    if x > 100:
        break
else:  
    print("All numbers less than 100")




#4 LISTS

from random import randint as random
def createList(min_len, max_len):
    my_list = []
    real_len = random(min_len, max_len)
    i = 0
    while i < real_len:
        my_list.append(random(1, 100))
        i=+1
    return my_list

lst1 = [x for x in range(1, 10)]
print([5, 8, 2, 9, 1][0], [5, 8, 2, 9, 1][-1])

count=0
for num in  [3, 7, 2, 9, 4, 5]:
    count += 1
print(count)

lst2 = [1, 2, 3]
lst2.append(4)
lst2.insert(0, 0)
print(lst2)


lst3 =  [1, 2, 3, 4, 5]
lst3.pop(2)
lst3.remove(4)
print(lst3)

print(sum([5, 8, 2, 9, 1]))
print(min([1, 2, 3]), max([1, 2, 3]))
lst4 = [1, 2, 3, 4, 5]
lst4.reverse()
print(lst4)

lst5 =  [4, 1, 7, 3, 9]
lst5.sort()
print(lst5)
lst5.sort(reverse=True)
print(lst5)

print([x for x in [1, 2, 3, 4, 5, 6] if x % 2 == 0])
print([x**2 for x in  [1, 2, 3, 4, 5]])
lst6 = [1, 2, 3]
lst6.extend([4, 5, 6])
print(lst6)

print(set([1, 2, 2, 3, 4, 4, 5]))
print( [1, 2, 3, 4, 5][::-1])
if 7 in [3, 5, 7, 9]: print('7 in list')

summ=0
for x in [2, 7, 4, 10, 5]:
    if x > 5: summ += x
print(summ)


print([x.upper() for x in ['a','b','c']])
for x in ['Python','Java','C++']:
    print(x)

count=0
for s in [1,3,2,3,4,3]:
    if s == 3: count += 1
print(count)


print(''.join(['A', 'B', 'C']))



from random import randint
print([randint(1, 20) for _ in range(randint(8, 15))][1::2])
print([randint(0, 50) for _ in range(randint(10, 20))][3:8])
print([chr(randint(0, 10000)) for _ in range(randint(6, 12))][::-1])
print([randint(0, 50) for _ in range(randint(9, 15))][::3])
lst7 = [randint(0, 50) for _ in range(randint(6, 12))]
print(lst7[:3], lst7[-3:])
print([randint(0, 50) for _ in range(randint(10, 20))][2:8:2])
print([randint(0, 50) for _ in range(randint(10, 20))][1:-1])
lst8=[randint(0, 50) for _ in range(randint(8, 12))]
print(lst8)
print(lst8[::-3])
lst9=[randint(0, 50) for _ in range(randint(10, 15))]
print(lst9)
lst9[2:5] = [47,84,49,45]
print(lst9)
lst10=[randint(0, 50) for _ in range(randint(10, 20))]
print(lst10)
print([x for i, x in enumerate(lst10) if i % 2 == 0])

'''


#ZJAZD 3
#EX1
'''
tuples_list = []
while line:=input("Enter up to 3 numbers separated by space: "):
    future_tuple = []
    lst = [int(x) for x in line.split()]
    if len(lst) == 1:
        future_tuple.append('S')
        future_tuple.append(lst[0]**2)
    elif len(lst) == 2:
        future_tuple.append('R')
        future_tuple.append(lst[0]*lst[1])
    elif len(lst) == 3:
        future_tuple.append('C')
        future_tuple.append(lst[0]*lst[1]*lst[2])
    future_tuple.insert(1,tuple(lst))
    tuples_list.append(future_tuple)
print(tuples_list)

#EX2

def reverse_dict (films_actors):
    reversed_dict = {}
    for film, actors in films_actors.items():
        for actor in actors:
            reversed_dict[actor]=reversed_dict.get(actor, []) + [film]
    reversed_dict = dict(sorted(reversed_dict.items(), key=lambda x:x[0]))
    reversed_dict = dict(sorted(reversed_dict.items(), key=lambda x:len(x[1]), reverse=True))
    return reversed_dict

films = dict(
a=[1, 3, 5], b=[2, 1, 4], c=[5, 2], d=[3, 4, 6],
e=[1], f=[3, 4, 5], g=[1, 7], h=[7, 6]
)
print(reverse_dict(films))


#EX3
def create_tuple(lst):
    D = {}
    for num in lst:
        D[num] = D.get(num, 0) + 1
    return sorted(D.items(), key=lambda x:x[1])[-1]
lst = [-4, 0, 3, 2, -4, -3, 3, 2, -4]
print(create_tuple(lst))
lst = 'to be or not to be'.split()
print(create_tuple(lst))




#EX4
from functools import reduce
from copy import deepcopy
def library(dct):
    new_dct = {}
    dct = deepcopy(dct)
    for person1, books1 in dct.items():
        max_books_amount = 0
        for person2, books2 in dct.items():
            if person1 == person2: continue
            if len(books1 & books2) > max_books_amount:
                max_books_amount = len(books1 & books2)
                new_dct[person1] = [person2, max_books_amount, books2 - books1]
    return new_dct

def library_reverse_dict(dct):
    reversed_dict = {}
    dct = deepcopy(dct)
    for person, books in dct.items():
        for book in books:
            reversed_dict[book] = reversed_dict.get(book, []) + [person]
    return reversed_dict

def library2(dct):
    reversed_dict = dict(sorted(library_reverse_dict(dct).items(), key=lambda x: len(x[1]), reverse=True))
    new_dct = {}
    for book, persons in reversed_dict.items():
        for person in persons:
            if person in new_dct: continue
            else: new_dct[person] = book, len(persons)-1
    return new_dct

def library3(dct):
    reversed_dict = dict(sorted(library_reverse_dict(dct).items(), key=lambda x: len(x[1]), reverse=True))
    new_dct = {}
    for book, persons in reversed_dict.items():
            for name in dct:
                if name in new_dct: continue
                if not name in persons: new_dct[name] = book, len(persons)
    return new_dct



bibliophiles = {
'John': {1, 2, 7, 11, 29},
'Mary': {7, 9, 11, 5},
'Jane': {1, 4, 5},
'Bill': {7, 11, 1, 2, 9},
'Kate': {4, 5, 9, 11}
}

print(library(bibliophiles))
print(library2(bibliophiles))
print(library3(bibliophiles))


'''
#GENERATORS
#EX6
'''

def gen_range(num):
    G = (x for x in range(1, num))
    for x in G:
        if x%3==0 and x%5==0:
            yield "FizzBuzz"
        elif x%3==0:
            yield "Fizz"
        elif x%5==0:
            yield "Buzz"
        else:
            yield x

func = gen_range(16)
print(next(func))
print(next(func))
print(next(func))
print(next(func))
print(next(func))
print(next(func))
print(next(func))
print(next(func))
print(next(func))
print(next(func))
print(next(func))
print(next(func))
print(next(func))
print(next(func))
print(next(func))
print(next(func))
print(next(func))
print(next(func))
print(next(func))
print(next(func))
print(next(func))



#EX7
def pairs_from_list(lst):
    x=0
    while x < len(lst):
        yield tuple(lst[x: x + 2])
        x+=2

lst = [1,2,3,4,5,6,7,8,9]
g = pairs_from_list(lst)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))



#EX8
def fibonacci(n):
        x, y = 0, 1
        while x < n:
            yield x
            x, y = y, x + y


func = fibonacci(25)
print(next(func))
print(next(func))
print(next(func))
print(next(func))
print(next(func))
print(next(func))
print(next(func))
print(next(func))
print(next(func))
print(next(func))
print(next(func))

#EX9
def gen_vowels(word):
    for c in word:
        if c in 'aeiou':
            yield c

gen = gen_vowels('hello')
print(next(gen))
print(next(gen))
print(next(gen))

#EX9


def gen_more_than_mid(lst):
    mid = len(lst) / 2
    for x in lst:
        if x > mid:
            yield x

gen = gen_more_than_mid([1,2,3,4,5,6,7,8,9,10,11])
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))



#EX11
def gen_pow_2():
    x = 0
    while True:
        y = 2**x
        yield y
        x+=1
        if y>1000:
            break


gen = gen_pow_2()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))



#EX12
def gen_last_element(lst):
    index = len(lst)-1
    while index>=0:
        yield lst[index]
        index-=1

lst = [1,2,3,4,5,6,7,8,9,10,11]
gen = gen_last_element(lst)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))


from random import choice
#EX14
def gen_dice():
    dice_values = [1,2,3,4,5,6]
    while (dice_value:=choice(dice_values))!=6:
        yield dice_value

gen = gen_dice()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

#P4
#EX1

def uppercase (fun):
    print("dec")
    def wrapper(*args, **kwargs):
        print("wrapper")
        return fun(*args, **kwargs).upper()
    return wrapper


@uppercase
def take_str(stri):
    print("taker")
    return stri


print(take_str("hello"))
take_str("hello")
take_str("hello")




import timeit

def timer (func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        finish = time.perf_counter()
        print("function execution time:", finish - start)
        return result
    return wrapper

@timer
def slow_add ( a , b ) :
    import time
    time . sleep ( 1 )
    return a + b

print(slow_add(8,12))



def repeat(fun):
    print("repeat")
    def wrapper(n, *args, **kwargs):
        print("wrapper")
        for i in range(n):
            fun(*args, **kwargs)
    return wrapper


@repeat
def greet ( name ) :
    print ( f"Hello {name}" )

p = greet
p(8, "Daniel")




import time
def delay(seconds):
    print("delay")
    def decorator(fun):
        def wrapper(*args, **kwargs):
           print("wrapper")
           time.sleep(seconds)
           return fun(*args, **kwargs)
        return wrapper
    return decorator

def timer(fun):
    print("timer")
    def wrapper(*args, **kwargs):
        print("wrapper2")
        start = time.perf_counter()
        fun(*args, **kwargs)
        finish = time.perf_counter()
        print("function execution time:", finish - start)
    return wrapper


@timer
@delay(5)
def fetch_data ( ) :
    return "data"


fetch_data()






def call_counter(func):
    print("decorator")
    called = 0
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        nonlocal called
        called += 1
        print(func.__name__, "called: ", called, "times")
    return wrapper

@call_counter
def F ():
    pass

@call_counter
def D ():
    pass

F()
F()
D()
F()
D()

'''

