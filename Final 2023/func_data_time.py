import datetime

def data_time():
    now = datetime.datetime.now()
    start_s = now.strftime("%d.%m.%y %H:%M:%S")
    return start_s
