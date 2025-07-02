# import calendar

# print(" wish a birtday hiral ")
# year= int(input("enter the year :"))
# month=int(input("enter the  month:"))
# date=int(input("enter the  date:"))
# day=str(input("enter the  day:"))



# print(calendar.month(year,month))
# print((date,day))

import calendar

year= int(input(" enter the year :"))

for month in range(1 ,13):
    
    print("\n" + calendar.month_name[month],year)
    
    print(calendar.month(year,month))







