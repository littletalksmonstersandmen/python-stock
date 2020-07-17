import time
import datetime

def legal_date_time():
    if legal_date() and legal_time():
        return 1
    else:
        return 0

def legal_date():
    a = time.localtime()
    b = time.strftime("%w", a)
    if b in ('1', '2', '3', '4', '5'):
        return 1
    else:
        return 0

def legal_time():
    time1 = datetime.datetime.strptime(str(datetime.datetime.now().date())+'9:15', '%Y-%m-%d%H:%M')
    time2 = datetime.datetime.strptime(str(datetime.datetime.now().date())+'11:30', '%Y-%m-%d%H:%M')
    time3 = datetime.datetime.strptime(str(datetime.datetime.now().date())+'13:00', '%Y-%m-%d%H:%M')
    time4 = datetime.datetime.strptime(str(datetime.datetime.now().date())+'15:00', '%Y-%m-%d%H:%M')

    n_time = datetime.datetime.now()

    if (n_time > time1 and n_time < time2) or (n_time > time3 and n_time < time4):
        return 1
    else:
        return 0
