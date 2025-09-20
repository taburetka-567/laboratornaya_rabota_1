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
