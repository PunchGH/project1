from forex_python.converter import CurrencyRates

def convert_command():
    
    while True:
        try:
            c = CurrencyRates()
            currency_1 = input("Type your first currency\n>>")
            currency_2 = input("Type your second currency\n>>")
            amount = input("Type your amount of money\n>>")
            c.convert(currency_1,currency_2 ,amount )
            break
        except:
            print("Cant convert",amount,"from",currency_1,"to",currency_2,"becuase one or both \ncurrency you type was not defined")

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
       

def conversion():
    
    c = CurrencyRates()
    
    while True:
    
        try:
            first_currency = input("Type your first currency\n>>")
            second_currency = input("Type your second currency\n>>")

            print(c.get_rate(first_currency, second_currency))
            break
        except:
            
            print("Cant convert",first_currency,"to",second_currency,"becuase one or both \ncurrency you type was not defined")

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
            
        elif user_command == "conversion":
            conversion()
        
        elif user_command == "convert":
            convert_command()
        
        else:
            print("the command",user_command,"is not detected")
        
        



main_menu()
controll_panel()