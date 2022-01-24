import datetime

def get_str_time_now():
    now = datetime.datetime.now()
    return now.strftime('%d.%m.%y %H:%M:%S.%f')

def convert_str_time_to_date_time(str):
    return datetime.datetime.strptime(str, '%d.%m.%y %H:%M:%S.%f')

print(get_str_time_now())
print(type(get_str_time_now()))

print(datetime.datetime.now())
print(type(datetime.datetime.now()))

print(convert_str_time_to_date_time('22.01.22 22:13:59.712212'))
print(type(convert_str_time_to_date_time('22.01.22 22:13:59.712212')))