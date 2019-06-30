>>> def lucky_ticket(ticket_number):
...     pass
...     if sum(list(map(int, str(ticket_number)[0:3]))) == sum(list(map(int, str(ticket_number)[3:6]))):
...         return True
...     else:
...         return False
...
>>>
>>> print(lucky_ticket(123006))
True
>>> print(lucky_ticket(12321))
False
>>> print(lucky_ticket(436751))
True