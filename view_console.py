# Модуль для взаимодействия с пользователем посредством консоли.

# ---------------------
# Универсальные функции

def print_text(text):
    print(text)

def print_list(alist):
    for x in alist:
        print(x)

def print_list_of_lists(lists):
    for lst in lists:
        print(' '.join(lst))

def input_int_value(text, qty_after_row = 0):
    a = int(input_str_value(text))
    if qty_after_row: print('\n'*(qty_after_row-1))
    return a

def input_str_value(text, qty_after_row = 0):
    s = input(text)
    if qty_after_row: print('\n'*(qty_after_row-1))
    return s

import getpass
def input_password(text, qty_after_row = 0):
    s = getpass.getpass(text)
    print(f'Получено {len(s)} символов.')
    if qty_after_row: print('\n' * (qty_after_row - 1))
    return s
