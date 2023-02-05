import mail, model, log, view_console, export

LOG_FILE_NAME = 'log.txt'
LOG_ERROR_FILE_NAME = 'log_err.txt'

EMOJI_THINK = '\U0001F914'
EMOJI_GOOD_LUCK = '\U0001F91E'
EMOJI_MONOCLE = '\U0001F9D0'
EMOJI_LIGHTNING = '\u26a1\ufe0f '
EMOJI_THUMBS_UP = '\U0001F44D'
EMOJI_THUMBS_DOWN = '\U0001F44E'
EMOJI_TORTLE = '\U0001F422'

ASCII_ARROW_DOWN = '\u2193'


SEND_MAIL = "ОТПРАВИТЬ письмо. "+EMOJI_THUMBS_UP # 0
CANCEL_MAIL = "ОТМЕНА "+EMOJI_THUMBS_DOWN # 13
BUTTON_NAMES = ["НАЧАТЬ быстрое письмо." # 0
              , EMOJI_MONOCLE+"Не вижу прог." # 1
              , EMOJI_THINK+" Зависает" # 2
              , EMOJI_TORTLE+"Тормозит" # 3
              , EMOJI_THINK+"Непонят. сообщения" # 4
              , EMOJI_LIGHTNING+"Нет подключения" # 5
              , EMOJI_MONOCLE+"Не вижу ЛП" # 6
              , "Новый леч.врач" # 7
              , "7 нозологий" # 8
              , ASCII_ARROW_DOWN+ASCII_ARROW_DOWN+ASCII_ARROW_DOWN \
                +" Ниже можно свой текст добавить" # 9
              , "Ответы:" # 10
              , "Спасибо!" # 11
              , "Успехов! "+EMOJI_GOOD_LUCK # 12
                ]
SUBTEXT      = [" Текст быстрого письма: "
              , EMOJI_MONOCLE+" Не вижу программу. "
              , EMOJI_THINK+" Программа зависает. "
              , EMOJI_TORTLE+" Программа тормозит. "
              , EMOJI_THINK+" Программа выдает непонятные сообщения. "
              , EMOJI_LIGHTNING + " Нет подключения. "
              , EMOJI_MONOCLE+" Не вижу ЛП (напишите внизу код ЛП и код ЛПУ). "
              , " Новый леч. врач "
              , " 7 нозологий "
              , "Ниже можно свой текст добавить"
              , "Ответы:"
              , "Спасибо!" # 11
              , "Успехов! "+EMOJI_GOOD_LUCK # 12
                ]

from telegram import (InlineKeyboardButton, InlineKeyboardMarkup)

keyboard_1 = [
    [InlineKeyboardButton(BUTTON_NAMES[0], callback_data="0")],
    [InlineKeyboardButton(BUTTON_NAMES[1], callback_data="1"), InlineKeyboardButton(BUTTON_NAMES[2], callback_data="2")],
    [InlineKeyboardButton(BUTTON_NAMES[3], callback_data="3"), InlineKeyboardButton(BUTTON_NAMES[4], callback_data="4")],
    [InlineKeyboardButton(BUTTON_NAMES[5], callback_data="5"), InlineKeyboardButton(BUTTON_NAMES[6], callback_data="6")],
    [InlineKeyboardButton(BUTTON_NAMES[11], callback_data="11"), InlineKeyboardButton(BUTTON_NAMES[12], callback_data="12")],
#    [InlineKeyboardButton(BUTTON_NAMES[10], callback_data="10")],
#    [InlineKeyboardButton(BUTTON_NAMES[7], callback_data="7"), InlineKeyboardButton(BUTTON_NAMES[8], callback_data="8")],
    [InlineKeyboardButton(BUTTON_NAMES[9], callback_data="9")],
]
reply_markup_1 = InlineKeyboardMarkup(keyboard_1)

keyboard_2 = [
    [InlineKeyboardButton(SEND_MAIL, callback_data="0"), InlineKeyboardButton(CANCEL_MAIL, callback_data="13") ],
    [InlineKeyboardButton(BUTTON_NAMES[1], callback_data="1"), InlineKeyboardButton(BUTTON_NAMES[2], callback_data="2")],
    [InlineKeyboardButton(BUTTON_NAMES[3], callback_data="3"), InlineKeyboardButton(BUTTON_NAMES[4], callback_data="4")],
    [InlineKeyboardButton(BUTTON_NAMES[5], callback_data="5"), InlineKeyboardButton(BUTTON_NAMES[6], callback_data="6")],
    [InlineKeyboardButton(BUTTON_NAMES[11], callback_data="11"), InlineKeyboardButton(BUTTON_NAMES[12], callback_data="12")],
    #    [InlineKeyboardButton(BUTTON_NAMES[10], callback_data="10")],
#    [InlineKeyboardButton(BUTTON_NAMES[7], callback_data="7"), InlineKeyboardButton(BUTTON_NAMES[8], callback_data="8")],
    [InlineKeyboardButton(BUTTON_NAMES[9], callback_data="9")],
]
reply_markup_2 = InlineKeyboardMarkup(keyboard_2)

BEGIN_TEXT = "кнопка 'НАЧАТЬ быстрое письмо.' "+ASCII_ARROW_DOWN
SENDED_TEXT = "ГОТОВО. Письмо отправлено."
MAIL_OK = "Письмо отправлено!"
MAIL_ERROR = "Письмо НЕ отправлено!"


def get_start_data(user_id, full_name):
    ob = model.get_data(user_id, full_name, BEGIN_TEXT, reply_markup_1)
    return ob[model.MAIL_TEXT], ob[model.CURR_REPLY_MARKUP]

def db_to_file():
    rez_list = []
    lists = model.get_DB_as_list_of_lists()
    if lists:
        for lst in lists:
            lst[model.CURR_REPLY_MARKUP]='_'
            lst = map(str, lst)
            s: str = f'{log.CSV_SEPARATOR.join(lst)}{log.CSV_SEPARATOR}'
            s = s.replace("\n"," -> ")
            rez_list.append(f'{s}\n')
    export.export_lines_to_file('db.csv', rez_list)

def get_echo_data(user_id, full_name, a_text):
    ob = model.get_data(user_id, full_name, BEGIN_TEXT, reply_markup_1)
    s = ob[model.MAIL_TEXT]
    if s and ob[model.IS_BEGIN_MAIL]:
        s += '\n' + a_text
        ob[model.MAIL_TEXT] = s
    else: ob[model.MAIL_TEXT] = BEGIN_TEXT
    model.set_data(*ob)
    return ob[model.MAIL_TEXT], ob[model.CURR_REPLY_MARKUP]

def get_button_data(user_id, full_name, button_number):
    ob = model.get_data(user_id, full_name, BEGIN_TEXT, reply_markup_1)
    temp_s = ob[model.MAIL_TEXT]
    if ob[model.LAST_BUTTON_NUMBER] == button_number:
        if button_number: return None, None
    ob[model.LAST_BUTTON_NUMBER] = button_number

    if button_number == 0 and not ob[model.IS_BEGIN_MAIL]: # начать письмо
        ob[model.IS_BEGIN_MAIL] = True
        ob[model.MAIL_TEXT] = f'{SUBTEXT[0]}\nкому: Калинину Павлу\nот: {full_name} '
        ob[model.CURR_REPLY_MARKUP] = reply_markup_2

    elif button_number == 13 and ob[model.IS_BEGIN_MAIL]: # отмена письма
        ob[model.IS_BEGIN_MAIL] = False
        ob[model.MAIL_TEXT] = BEGIN_TEXT
        ob[model.CURR_REPLY_MARKUP] = reply_markup_1

    elif button_number == 0 and ob[model.IS_BEGIN_MAIL]: # отправка письма
        try:
            mail.mail_send(ob[model.MAIL_TEXT])
        except Exception as e:
            view_console.print_text(MAIL_ERROR +' | '+ ob[model.FULL_NAME])
            # логирование
            log.log_str( [
                ob[model.USER_ID]
              , ob[model.FULL_NAME]
              , MAIL_ERROR
              ]
            )
            log.log_str( [
                  ob[model.USER_ID]
                , ob[model.FULL_NAME]
                , MAIL_ERROR
              ] , LOG_ERROR_FILE_NAME
            )
        else:
            view_console.print_text(MAIL_OK +' | '+ ob[model.FULL_NAME])
            # логирование
            log.log_str( [
                  ob[model.USER_ID]
                , ob[model.FULL_NAME]
                , ob[model.MAIL_TEXT]
              ]
            )

        ob[model.IS_BEGIN_MAIL] = False
        ob[model.MAIL_TEXT] = SENDED_TEXT
        ob[model.CURR_REPLY_MARKUP] = reply_markup_1

    elif button_number == 7:
        ob[model.MAIL_TEXT] = '''Новая запись о лечащем враче:
 кнопка "Справочная система" -> контакт специалиста по ЛПУ и врачам'''
        return ob[model.MAIL_TEXT], ob[model.CURR_REPLY_MARKUP]
    elif button_number == 8:
        ob[model.MAIL_TEXT] = '''Получить информацию связанную с "7 нозологий":
 кнопка "Отчетная система" -> Папка "Отчеты по сводным данным Минздрава"
 -> отчет "Заявки по 7-ми нозологиям ..."'''
        return ob[model.MAIL_TEXT], ob[model.CURR_REPLY_MARKUP]
    elif button_number == 9:
        return None, None
    elif button_number == 10:
        return None, None
    elif ob[model.IS_BEGIN_MAIL]:
        ob[model.MAIL_TEXT] += '\n'+SUBTEXT[button_number]

    # убрать
    if not ob[model.IS_BEGIN_MAIL] and not ob[model.MAIL_TEXT].replace(" ",""): s = BEGIN_TEXT

    if temp_s == ob[model.MAIL_TEXT]: # чтобы повтора не было и не сыпались ворнинги
        ob[model.MAIL_TEXT] += '_'
        ob[model.MAIL_TEXT] = ob[model.MAIL_TEXT].replace('___', '')
    return ob[model.MAIL_TEXT], ob[model.CURR_REPLY_MARKUP]
