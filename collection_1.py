total = 0
temp = [[1,2,3,4],{"ew" : 32}]
print(temp)
menu_dict = {}

while True:
    
    menu_name = input("pls enter menu : ")
    
    if menu_name.lower() == "exit":
        break
    else:    
        menu_price = int(input("Price : ")) 
        total += menu_price
        menu_dict[menu_name] = menu_price 
print(menu_dict)
print("\ntotal :",total)


