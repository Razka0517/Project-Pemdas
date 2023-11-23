from os import access, name
from typing import Optional
import time
import datetime

def login(name,password) :
    sukses = False
    file = open("databaselogin.txt","r")
    for i in file :
        a,b = i.split(",")
        b = b.strip()
        if (a == name and b == password) :
            sukses = True
            break
    file.close()
    if (sukses) :
        print("login berhasil! selamat datang, "+name)
        int(input("Masukkan kode billing yang akan anda beli"))
    else :
        print("Akun anda belum terdaftar, silahkan lakukan registrasi akun !")

def registrasi(name,password) :
    """ a untuk append (menambahkan)"""
    file = open("databaselogin.txt","a")
    file.write("\n"+name+","+password)
    
def billing(bill) :
    file = open("databaselogin.txt","a")
    file.write("\n",)

def access(option) :
    global name 
    if (option == "login") :
        name = input("Masukkan nama atau ID : ")
        password = input("Masukkan Password : ")
        login(name,password)
    else :
        print("Masukkan ID dan Password anda yang ingin di buat : ")
        name = input("Masukkan ID : ")
        password = input("Masukkan Password : ")
        registrasi(name,password)
        print("Registrasi akun anda berhasil !!, silahkan login")

def begin () :
    global option
    print("Selamat datang !!")
    print("ketik 'login' jika anda ingin login")
    print("ketik 'reg' jika anda ingin registrasi")
    option = str(input("Masukkan opsi yang ada diatas : "))
    if (option !="login" and option !="reg") :
        begin()



begin()
access(option)
