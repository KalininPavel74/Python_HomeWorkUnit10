# Модуль для функций экспорта, импорта даных

import model

UTF_8 = 'utf-8'
CURR_ENCODING = UTF_8

CSV_SEPARATOR = ';'
CSV_SUB_SEPARATOR = ', '

TAB_CHAR = '    '

# ---------------------
# Универсальные функции

def import_lines_from_file(file):
    with open(file, 'r', encoding=CURR_ENCODING) as f:
        return f.readlines()

def export_lines_to_file(file, lines):
    with open(file, 'w', encoding=CURR_ENCODING) as f:
        f.writelines(lines)

def export_text_to_file(file, text):
    with open(file, 'w', encoding=CURR_ENCODING) as f:
        f.write(text)

# ------------------------------------------------------------------
# Функции для разных форматов данных не знающие о предметной области

def import_list_of_lists_from_CSV(file, qty_fields):
    lst = import_lines_from_file(file)
    list2 = []
    for s in lst:
        list2.append( s.split(CSV_SEPARATOR)[:qty_fields] )
    return list2

def export_list_of_lists_to_CSV(file, lists):
    lines = [CSV_SEPARATOR.join(lst) + CSV_SEPARATOR +'\n' for lst in lists]
    qty = len(lines)
    export_lines_to_file(file, lines)
    return qty

def export_list_to_TXT(file, alist):
    lines = list(map(lambda x: str(x) + '\n', alist))
    qty = len(lines)
    export_lines_to_file(file, lines)
    return qty



'''
# ------------------------------------------------------------------
# Функции для разных форматов данных зависящие от предметной области

# записи в виде текста для пользователя:
def get_record_as_text(alist):
    lst = []
    for i in range(1,len(alist)):
        lst.append(f', {model.FIELDS_LIST_RUS_NAME[i]}: {alist[i]}')
    lst[0] = lst[0][1:]
    text = f'{model.FIELD_RUS_NAME_ID}{alist[0]} {"".join(lst)}'
    return text

def get_DB_as_list_of_text(qty_row = 0):
    lst = []
    qty = 1
    for list2 in model.get_DB_as_list_of_lists():
        lst.append(get_record_as_text(list2))
        if qty_row and qty >= qty_row: break
        else: qty += 1   
    return lst

# записи в виде HTML

def export_DB_to_HTML(file):
    lines = []
    lines.append(f'<!DOCTYPE html>')
    lines.append(f'<html lang="ru">')
    lines.append(f'{TAB_CHAR}<head>')
    lines.append(f'{TAB_CHAR*2}<meta charset="{UTF_8}">')
    lines.append(f'{TAB_CHAR*2}<title>{model.DB_RUS_NAME}</title>')
    lines.append(f'{TAB_CHAR}</head>')
    lines.append(f'{TAB_CHAR}<body>')
    lines.append(f'{TAB_CHAR*2}<table border="1">')
    lines.append(f'{TAB_CHAR*3}<tr>')
    for s in model.FIELDS_LIST_RUS_NAME:
        lines.append(f'{TAB_CHAR*4}<th>{s}</th>')
    lines.append(f'{TAB_CHAR*3}</tr>')

    list_of_lists = model.get_DB_as_list_of_lists()
    qty = len(list_of_lists)
    for lst in list_of_lists:
        lines.append(f'{TAB_CHAR*3}<tr>')
        for s in lst:
            lines.append(f'{TAB_CHAR*4}<td>{s}</td>')
        lines.append(f'{TAB_CHAR*3}</tr>')

    lines.append(f'{TAB_CHAR*2}</table>')
    lines.append(f'{TAB_CHAR}</body>')
    lines.append(f'</html>')

    export_list_to_TXT(file, lines)
    return qty


# -----------------------------------
# Функции для Сотрудников компании

# записи в виде XML для Сотрудников компании

def export_DB_to_XML(file):
    lines = []
    lines.append(f'<?xml version="1.1" encoding="{UTF_8}" ?>')
    lines.append(f'<{model.DB_LAT_NAME}>')

    list_of_lists = model.get_DB_as_list_of_lists()
    qty = len(list_of_lists)
    for lst in list_of_lists:
        lines.append(f'{TAB_CHAR}<{model.RECORD_LAT_NAME}>')
        lines.append(f'{TAB_CHAR*2}<{model.FIELD_LAT_NAME_ID}>{lst[0]}</{model.FIELD_LAT_NAME_ID}>')
        lines.append(f'{TAB_CHAR*2}<{model.FIELD_LAT_NAME_FIO}>{lst[1]}</{model.FIELD_LAT_NAME_FIO}>')
        lines.append(f'{TAB_CHAR*2}<{model.FIELD_LAT_NAME_POST}>{lst[2]}</{model.FIELD_LAT_NAME_POST}>')
        lines.append(f'{TAB_CHAR*2}<{model.FIELD_LAT_NAME_SALARY}>{lst[3]}</{model.FIELD_LAT_NAME_SALARY}>')
        lines.append(f'{TAB_CHAR}</{model.RECORD_LAT_NAME}>')
    lines.append(f'</{model.DB_LAT_NAME}>')

    export_list_to_TXT(file, lines)
    return qty
'''