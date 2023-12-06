import pandas as pd
import os
from time import sleep as delay
import time 
import datetime
import header as hd

def bersih_console():
    os.system("cls")

def login():
    try:
        bersih_console()
        name = str(input("Masukkan Nama atau ID : "))
        password = str(input("Masukkan Password : "))
        
        # Membaca data dari file CSV
        data = pd.read_csv('databaselogin.csv')
        # cek_data = (data['name'] == name) & (data['password'] == password)
        cek_data = data[(data['name'] == name) & (data['password'] == password)]
        cek_user = data[(data['name'] == name)]
        cek_pass = data[(data['password'] == password)]

        # Menjalankan keputusan berdasarkan kondisi tertentu
        if(cek_user.empty and cek_pass.empty):
            print("Akun tidak terdaftar. Silakan registrasi.")
            delay(2)
            begin()
            access(option)
        else:
            # Mengecek apakah nama dan password cocok dengan data di CSV
            if(not cek_data.empty):
                bersih_console()
                print("Login berhasil! Selamat datang, " + name)
                delay(1)
                opsiuser()
            else:
                if(not cek_user.empty or cek_pass.empty):
                    print("Password Salah\n")
                    delay(1)
                    login()
                elif(cek_user.empty or not cek_pass.empty):
                    print("User tidak ditemukan\n")
                    delay(1)
                    login()

    except FileNotFoundError:
        print("File CSV tidak ditemukan.")

def opsiuser() :
    hd.headeruser()
    print("""1. Beli waktu
2. Cek waktu
3. Pesan makanan""")


def loginadm():
    try:
        name = str(input("Masukkan Nama atau ID admin: "))
        password = int(input("Masukkan password : "))
        
        # Membaca data dari file CSV
        data = pd.read_csv('databaseadmin.csv')
        # cek_data = (data['name'] == name) & (data['password'] == password)
        cek_data = data[(data['name'] == name) & (data['password'] == password)]
        cek_user = data[(data['name'] == name)]
        cek_pass = data[(data['password'] == password)]

        # Menjalankan keputusan berdasarkan kondisi tertentu
        if(cek_user.empty and cek_pass.empty):
            print("Anda bukan admin")
            delay(2)
            begin()
            access(option)
        else:
            # Mengecek apakah nama dan password cocok dengan data di CSV
            if(not cek_data.empty):
                bersih_console()
                print("Login berhasil! Selamat datang, " + name)
                delay(1)
                opsiuser()
            else:
                if(not cek_user.empty or cek_pass.empty):
                    print("Password Salah\n")
                    delay(1)
                    loginadm()
                elif(cek_user.empty or not cek_pass.empty):
                    print("User tidak ditemukan\n")
                    delay(1)
                    loginadm()

    except FileNotFoundError:
        print("File CSV tidak ditemukan.")


def registrasi() -> None:
    print("Masukkan ID dan Password Anda yang ingin dibuat\n")
    name = input("Masukkan ID: ")
    password = input("Masukkan Password: ")
    data = pd.read_csv('databaselogin.csv')
    data_baru = {'name': name, 'password': password}
    data = data._append(data_baru, ignore_index=True)
    data.to_csv('databaselogin.csv', index=False)
    print("Registrasi akun Anda berhasil! Silahkan login.")
    delay(2)
    begin()
    access(option)

def waktu() :
    total_detik= h * 3600 + m * 60 + s

    while total_detik > 0:
        timer = datetime.timedelta(seconds=total_detik)

        print(timer,end="\r")
        time.sleep(1)
        total_detik -=1
    print("waktu sudah habis !!")
    h=0;m=0;s=0


    #if user == 1 :
    #    waktu(int(h=3),int(m),int(s))

def keluar():
    while(keluar) :
        bersih_console()
        print("Keluar dari program....")
        delay(1)
        break
def access(option):
    global name
    if option == "1":
        login()
    elif option == "3":
        loginadm()
            
    elif option == "2":
        registrasi()
    elif option == "4" :
        keluar()
    else:
        print("Opsi tidak valid.")

def begin():
    global option
    hd.headerawal()
    option = str(input("""Masukkan opsi yang ada di atas 'Contoh : 1' : """))
    if option not in ["1", "2","3","4"]:
        print("Opsi tidak valid.")
        begin()

begin()
access(option)
