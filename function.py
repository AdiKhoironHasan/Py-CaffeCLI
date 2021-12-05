import config
import os
from time import sleep

dataUser = 0

def hello() :
    global dataUser
    print(dataUser)

def home():
    global dataUser
    print("================================================\n")
    print("*** SELAMAT DATANG DI CAFE ***\n")
    print("    Silahkan Login...\n")
    
    print("================================================\n\n")
    usr = str(input("username : "))
    pwd = str(input("password : "))
    
    ret = 0
    for i in range(len(config.data)) :
        if (usr == config.data[i]["usr"]) and (pwd == config.data[i]["pwd"]) :
            dataUser = i
            os.system("clear")
            print("selamat datang", config.data[i]["nama"])
            print("saldo anda : Rp ", config.data[i]["saldo"])
            ret = 1
    print("kesalahan username atau password !")
    return ret

def menu():
    ret = 0
    os.system("clear")
    print("Menu :")
    print("1. Makanan")
    print("2. Minuman")
    print("3. Isi Saldo")
    print("4. Keluar")
    menu = int(input("masukan angka untuk pilih menu : "))
    if menu == 1 :
        ret = 1
    elif menu == 2:
        ret = 2
    elif menu == 3:
        ret = 3
    elif menu == 4:
        ret = 4
    
    return ret

def foodMenu() :
    global dataUser
    ret = 0
    os.system("clear")
    print("menu makanan : ")
    for i in range(len(config.foodMenus)) :
        print(config.foodMenus[i]["no"],". ", config.foodMenus[i]["nama"]," ", config.foodMenus[i]["harga"])
    menu = int(input("masukan angka untuk pilih menu : "))
    print("saldo kamu : ", config.data[dataUser]["saldo"])
    config.data[dataUser]["saldo"] = (config.data[dataUser]["saldo"]-config.foodMenus[menu-1]["harga"])
    if config.data[dataUser]["saldo"] < 0 :
        print("Maaf Saldo Anda Tidak cukup, Silakan isi saldo")
        mySaldo()
        ret = 0
    else :
        print("kamu telah membeli", config.foodMenus[menu-1]["nama"], ", harga", config.foodMenus[menu-1]["harga"])
        print("sisa saldo : ", config.data[dataUser]["saldo"])
        x = int(input("ingin memilih menu lagi ? [0/1]"))
        if x == True :
            ret = 1        
    return ret

def drinkMenu() :
    ret = 0
    os.system("clear")
    print("menu minuman : ")
    for i in range(len(config.drinkMenus)) :
        print(config.drinkMenus[i]["no"],". ", config.drinkMenus[i]["nama"]," ", config.drinkMenus[i]["harga"])
    menu = int(input("masukan angka untuk pilih menu : "))
    print("saldo kamu : ", config.data[dataUser]["saldo"])
    config.data[dataUser]["saldo"] = (config.data[dataUser]["saldo"]-config.drinkMenus[menu-1]["harga"])
    if config.data[dataUser]["saldo"] < 0 :
        print("Maaf Saldo Anda Tidak cukup, Silakan isi saldo")
        ret = 0
    else :
        print("kamu telah membeli", config.drinkMenus[menu-1]["nama"], ", harga", config.drinkMenus[menu-1]["harga"])
        print("sisa saldo : ", config.data[dataUser]["saldo"])
        x = int(input("ingin memilih menu lagi ? [0/1]"))
        if x == True :
            ret = 1        
    return ret

def mySaldo() :
    os.system("clear")
    print("Saldo Anda ", config.data[dataUser]["saldo"])
    i = int(input("Ingin mengisi saldo?[0/1]"))
    if i == True :
        s = int(input("Masukan jumlah saldo : "))
        config.data[dataUser]["saldo"] = config.data[dataUser]["saldo"] + s
        os.system("clear")
        print("Isi saldo berhasil :")
        print("Saldo Anda ", config.data[dataUser]["saldo"])
        sleep(3)