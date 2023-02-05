MAIL_smtp_host = ''
MAIL_address   = ''
MAIL_password  = ''

def init_mail(aMAIL_smtp_host, aMAIL_address, aMAIL_password):
    global MAIL_smtp_host, MAIL_address, MAIL_password
    MAIL_smtp_host,  MAIL_address,  MAIL_password \
 = aMAIL_smtp_host, aMAIL_address, aMAIL_password

import mail1

def mail_send(atext, asubject = 'Письмо из Телеграм'):
    mail1.send(
        subject=asubject,
        text=atext,
        recipients=MAIL_address,
        sender=MAIL_address,
        smtp_host=MAIL_smtp_host,
        # smtp_port='465', # лучше не указывать, само по определяет протокол
        username=MAIL_address,
        password=MAIL_password,
        # attachments={'1.txt': '1.txt'}
    )
