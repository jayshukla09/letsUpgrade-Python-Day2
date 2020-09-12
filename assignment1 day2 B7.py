Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:37:02) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> lst = [1,3,4]
>>> print(lst)
[1, 3, 4]
>>> lst.append(6)
>>> print(lst)
[1, 3, 4, 6]
>>> lst.extend([7, 8])
>>> print(lst)
[1, 3, 4, 6, 7, 8]
>>> lst.insert(2, 2)
>>> print(lst)
[1, 3, 2, 4, 6, 7, 8]
>>> lst.remove(7)
>>> print(lst)
[1, 3, 2, 4, 6, 8]
>>> lst.pop(3)
4
>>> #dictionary
>>> d = {1:2, 2:3, 3:5}
>>> print(d)
{1: 2, 2: 3, 3: 5}
>>> d.clear()
>>> print(d)
{}
>>> d = {1:2, 2:5, 3:8}
>>> print(d)
{1: 2, 2: 5, 3: 8}
>>> print(d.items())
dict_items([(1, 2), (2, 5), (3, 8)])
>>> d.popitem()
(3, 8)
>>> print(d)
{1: 2, 2: 5}
>>> print(d.keys())
dict_keys([1, 2])
>>> print(d.keys())
dict_keys([1, 2])
>>> print(d.values())
dict_values([2, 5])
>>> #sets
>>> s = {2, 5, 6, 7}
>>> print(s)
{2, 5, 6, 7}
>>> s.add(4)
>>> print(s)
{2, 4, 5, 6, 7}
>>> s.clear()
>>> print(s)
set()
>>> s = {1, 3, 4, 6}
>>> print(s.pop())
1
>>> s.update([7, 8], [2, 5])
>>> print(s)
{2, 3, 4, 5, 6, 7, 8}
>>> s.remove(6)
>>> print(s)
{2, 3, 4, 5, 7, 8}
>>> #tuple
>>> tup = (3, 5, 8)
>>> tup.index(2)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    tup.index(2)
ValueError: tuple.index(x): x not in tuple
>>> tup.index(3)
0
>>> tup.count(8)
1
>>> #string
>>> st = "Hello People"
>>> print(st)
Hello People
>>> st.lower()
'hello people'
>>> st.upper()
'HELLO PEOPLE'
>>> st.capitalize()
'Hello people'
>>> st.count()
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    st.count()
TypeError: count() takes at least 1 argument (0 given)
>>> st.count(l)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    st.count(l)
NameError: name 'l' is not defined
>>> st.count('l')
3
>>> st.find('e')
1
>>> st.rfind('l')
10
>>> 