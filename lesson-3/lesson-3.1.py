>>> def my_round(number, ndigits):
...     pass
...     x = (number*10**ndigits)
...     if x % 1 >= 0.5:
...         new_number = (int(x)+1)/(10**ndigits)
...     else:
...         new_number = int(x)/(10**ndigits)
...     return new_number
...
>>>
>>>
>>> print(my_round(2.1234567, 5))
2.12346
>>> print(my_round(2.1999967, 5))
2.2
>>> print(my_round(2.9999967, 5))
3.0