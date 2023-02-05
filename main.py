# Модуль для запуска приложения.

# https://github.com/KalininPavel74/Python_HomeWorkUnit10.git

# Калинин Павел 31.01.2023
# # Знакомство с языком Python (семинары)
# Урок 10.
# Домашняя работа

# . venv/Scripts/activate
# pip freeze > requirements.txt

import view_console as view, control_telegram, mail

taskName = '''Задание  №1. Создать телеграмм бота желательно сложнее чем калькулятор.
(Проявите свою фантазию и сделайте что то интересное)'''
view.print_text("-----------------------------------\n\r" + taskName)
view.print_text("")

l_TELEGRAM_TOKEN = view.input_password(
    "Введите телеграм-TOKEN и нажмите Enter (невижимый режим): ")
control_telegram.init_telegram_token(l_TELEGRAM_TOKEN)

l_MAIL_username = view.input_str_value(
    "Введите адрес электронной почты (Например: telegram20230202@mail.ru): ")
l_MAIL_password = view.input_password(
    "Введите пароль от почты и нажмите Enter (невижимый режим): ")
l_MAIL_smtp_host = view.input_str_value(
    "Введите адрес smtp_host (Например: smtp.mail.ru): ")
mail.init_mail(l_MAIL_smtp_host, l_MAIL_username, l_MAIL_password)

control_telegram.main()