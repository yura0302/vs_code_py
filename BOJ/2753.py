leap_year=int(input())
if leap_year%4==0 and leap_year%100 != 0 or leap_year%400==0:
    print("1")
else:
    print("0")