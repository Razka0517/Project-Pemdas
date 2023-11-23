import time 
import datetime


def tigajam(h,m,s) :
    total_detik= h * 3600 + m * 60 + s

    while total_detik > 0:
        timer = datetime.timedelta(seconds=total_detik)

        print(timer,end="\r")
        time.sleep(1)
        total_detik -=1
    print("waktu sudah habis !!")
h=3
m=0
s=0

user = int(input("Mau main berapa jam ? "))

if user == 1 :
    tigajam(int(h),int(m),int(s))

