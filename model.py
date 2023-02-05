DB = []

USER_ID, FULL_NAME, IS_BEGIN_MAIL, LAST_BUTTON_NUMBER, CURR_REPLY_MARKUP, MAIL_TEXT = range(6)

def get_DB_as_list_of_lists():
    return DB[:]

def set_data(user_id, full_name, isBeginMail, last_button_number, curr_reply_markup, mail_text):
    lst = [user_id, full_name, isBeginMail, last_button_number, curr_reply_markup, mail_text]
    for i, ob in enumerate(DB):
        if user_id == ob[USER_ID]:
            DB[i] = lst
            return
    DB.append(lst)

def get_data(user_id, init_full_name, init_mail_text, init_curr_reply_markup):
    for ob in DB:
        if user_id == ob[USER_ID]:
            return ob
    lst = [user_id, init_full_name, False, -1, init_curr_reply_markup, init_mail_text]
    DB.append(lst)
    return lst
