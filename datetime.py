import datetime

dir(datetime)
datetime.date.today()
datetime.datetime.now()
date = datetime.date(2023, 8, 10)
date.day
date.month
date.year

horario = datetime.datetime(2023, 8, 10, 11, 50, 0)
horario.hour
horario.minute
horario.second