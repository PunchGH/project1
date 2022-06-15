from forex_python.converter import CurrencyRates

def list_currency_command():
    
    c = CurrencyRates()
    all_currency = c.get_rates('USD')
    all_currency['USD'] = 1
    
    for i in all_currency:
        print(i)
        
def list_rates_command():
    
    
    while True:
    
        try:    
            c = CurrencyRates()
            user_currency = input("Type your currency\n>>").upper()
            rates = c.get_rates(user_currency)
            
            for i in rates:
                print("\n1",user_currency," : ",rates[i],i)
            
            
            break
        
        except:
            print("There no currency called",user_currency)
       




def main_menu():
    
    print("          welcome          ")
    print("----Currency Calculator----")

    print("\nwelcome,we have some commands for you to choose(The program will change your input to lower case and the data you get is based by now) : ")

    print("\n1) Stop the program from running type  :     exit")
    
    print("\n2) List all the currency               :     list_currency")
    
    print("\n3) List all latest currency rates      :     list_rate")
    
    print("\n4) Get conversion rate type            :     conversion")
    
    print("\n5) convert amount money                :     convert")
    
        

def controll_panel():
    
    while True:
        user_command = input(">>").lower()
        
        if user_command == "exit":
            print("finished running program")
            break
        
        elif user_command == "list_currency":
            list_currency_command()
        
        elif user_command == "list_rate":
            list_rates_command()
            
        else:
            print("the command",user_command,"is not detected")
        
        



main_menu()
controll_panel()