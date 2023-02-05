import datetime

UTF_8 = 'utf-8'
CURR_ENCODING = UTF_8

CSV_SEPARATOR = '^'
TAB_CHAR = '    '
FILE_NAME = 'log.txt'

def log_str(lst: list, file = FILE_NAME):
    if lst:
        lst = map(str, lst)
        with open(file, 'a', encoding=CURR_ENCODING) as f:
            str_date = str(datetime.datetime.now())
            s: str = f'{str_date}{CSV_SEPARATOR}{CSV_SEPARATOR.join(lst)}{CSV_SEPARATOR}'
            s = s.replace("\n"," -> ")
            f.write(s+'\n')
