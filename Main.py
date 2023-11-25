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
        print("\nlogin berhasil! selamat datang, "+name)

    else :
        print("Akun anda belum terdaftar, silahkan lakukan registrasi akun !")

def loginadm(name,password) :
    sukses = False
    file = open("databaseadmin.txt","r")
    for i in file :
        a,b=i.split(",")
        b = b.strip()
        if (a == name and b == password) :
            sukses = True
            break
    file.close()
    if (sukses) :
        print("Selamat datang,",name)

    else :
        print("Password salah !!")

waktu = 0

def registrasi(name,password) :
    """ a untuk append (menambahkan)"""
    file = open("databaselogin.txt","a")
    file.write("\n"+name+","+password,+waktu)
    
def border() :
    print("*"*40)

def access(option) :
    global name 
    if (option == "login") :
        name = input("Masukkan nama atau ID : ")
        password = input("Masukkan Password : ")
        login(name,password)
    elif (option == "admin") :
        print("==============Menu admin==============")
        name="admin"
        password=input("Masukkan Password : ")
        loginadm(name,password)
    else :
        print("Masukkan ID dan Password anda yang ingin di buat : ")
        name = input("Masukkan ID : ")
        password = input("Masukkan Password : ")
        registrasi(name,password)
        print("Registrasi akun anda berhasil !!, silahkan login")

def begin () :
    global option
    print("Selamat datang di zero.net")
    border()
    print("ketik 'login' jika anda ingin login")
    print("ketik 'reg' jika anda ingin registrasi")
    print("ketik 'admin' untuk login sebagai admin")
    border()
    option = str(input("Masukkan opsi yang ada diatas : "))
    if (option !="login" and option !="reg" and option !="admin") :
        begin()



begin()
access(option)
