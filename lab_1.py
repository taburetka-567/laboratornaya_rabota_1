
from importlib.resources import read_text
#1
a = 4
b = 2.5
print(a + b, a - b, a * b, a / b)
rad = 5
pi = 3.14159
s = pi * rad ** 2
print(round(s, 2))
print(f'Площадь круга: {round(s, 2)}')

#2
text = " Hello, Python! "
text1 = text.strip().replace('!', '?').upper()
print(text1)
text = text.strip().lower()
assert text == "hello, python!"

#3
num = [7, 2, 5]
num.append(4)
num.insert(1,10)
num.extend([1,1,1])
num.remove(7)
x=num.pop(-1)
num=sorted(num)
num.reverse()
print(num.count(2))
print(num.index(1))
copy=num.copy()
deepcopy=num.copy()
print(copy,deepcopy)
num.clear()

#4
t=(1,2,3)
#t[1]=100#кортежи не поддерживают индексацию(?)
t2=t+(4,5)
print(t2)
print(t2.count(3))
print(t2.index(4))
print(t)

#5
values=[3, 1, 3, 2, 1, 5, 2]
unique_values = set(values)
print(unique_values)
print(len(unique_values))
other = {2, 4, 5}
print(unique_values&other)
print(unique_values|other)
print(unique_values-other)
print(other-unique_values)

#7

k=0
text = """
     Python is a powerful programming language.
     It is used in data science, web development, automation, and many other fields!
    PYTHON is easy to learn, yet very versatile.
"""

text = text.strip().lower()
text = text.replace('!',".")
s = [s.strip() for s in text.split('.') if s.strip()]
print(s)

s1 = s[0].split()
print(s1)
for x in s1:
    if x == 'python':
        k+=1
print(k)
s1 = ' '.join(s1)
print(s1)
print(str(s1).startswith('python'), str(s1).endswith('language'))

ts = text.split()
n=0
print(len(ts), text.count('a'))
for i in range(len(ts)):
    n+=1
    if ts[i] == 'data':
        print(n)

ts1 = '-'.join(ts)
print(ts1)

text_list = [
    'python is a powerful programming language',
    'it is used in data science, web development, automation, and many other fields',
    'python is easy to learn, yet very versatile'
]

import string
all_text = " ".join(text_list).lower().translate(str.maketrans('', '', string.punctuation))
words = all_text.split()

word_counts = {}

for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

print(word_counts)

def clean_text(text):
     text = text.replace(',','')
     text = text.replace('.', '')
     text = text.replace('!', '')
     return text.lower()
print(clean_text(text))


# 6
scores = {"Alice": 85, "Bob": 90}
scores["Charlie"] = 78
scores["Bob"] = 95
print(scores)
dave_score = scores.get("Dave", "не найден")
bob_score = scores.get("Bob", "не найден")

print( {dave_score})
print( {bob_score})

alice_score = scores.pop("Alice")
print(scores)


expected_count = 2 # боб и чарли
print( expected_count)
print( len(scores))
if expected_count == len(scores):
    print('всё совпадает')


print(scores.keys())


print(scores.values())