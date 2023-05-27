import datetime
# print(datetime.date.today())

# t = datetime.datetime.now()
# print(t)
# print(t.year)
# print(t.month)
# print(t.second)

# import time
# print(list(time.localtime()))

# d = str(input("(20220701):"))
# dt = datetime.datetime.strptime(d,'%Y%m%d')
# ad = d[:4]+"0101"
# adt = datetime.datetime.strptime(ad,"%Y%m%d")
# print(int((dt-adt).days)+1)

a = datetime.date.today()
print(a+datetime.timedelta(days = 100))
