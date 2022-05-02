total = 0
menuList = []
def showBill():
    
    print("---- My Food----")
    for number in range(len(menuList)):
        print(menuList[number])
        print("total : ",total)
    

while True:
    menuName = input("Plese Enter Menu :")
    if(menuName.lower() == "exit"):
        break
    else:
        menuPrice = input("Price :")
        total += int(menuPrice)
        menuList.append([menuName,menuPrice])

showBill()