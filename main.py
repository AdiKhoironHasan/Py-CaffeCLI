import function
import config

i = 1
if function.home() == True :
    print("loginnn")
    while i == True :
        menu = function.menu()
        if menu == 1 :
            if function.foodMenu() == False :
                i = 0
        elif menu == 2 :
            if function.drinkMenu() == False :
                i = 0
        elif menu == 3 :
            if function.mySaldo() == False :
                i = 0
        elif menu == 4 :
            if function.home() == False :
                i = 0


# print(config.data[0]["nama"])