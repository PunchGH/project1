price = 0
UsernameInput = input("User name : ")
PasswordInput = input("Pass word : ")
if UsernameInput == "admin" and PasswordInput == "12345" :
    print("Welcome !")
    print("-------ishop--------")
    print("choose what you want to buy")
    print("1.banana 2.apple 3.meat 4.keyboard 5.calculate and show result")
    
    while(True):    
    
        print("select product or exit")
        user_selected = int(input(">>"))
    
        if user_selected == 5:
            break
    
        
    
        print("enter number of the product u want")    
        number_selected = int(input(">>"))
    
    
        if user_selected == 1:
        
            print("banana",number_selected)
            price += 5*number_selected
        
        elif user_selected == 2:
            
            print("apple",number_selected)   
            price += 25 * number_selected
        
        elif user_selected == 3:
        
            print("meat",number_selected)    
            price += 500 * number_selected
        
        elif user_selected == 4:
            
            print("key board",number_selected)
            price += 8000 * number_selected
    print("price  : ",price)        