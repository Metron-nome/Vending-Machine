"""ASSESSMENT 2: VENDING MACHINE"""

"""SANRIO THEMED VENDING MACHINE"""

"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⢀⡀⠀⢀⣠⣤⣤⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⠶⠚⠋⡿⠟⠋⠉⠉⠉⠉⠉⠉⠉⠛⠳⢶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠞⠋⠀⢴⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣏⠛⠳⢦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣀⣤⠶⠛⠁⠀⠀⢀⡾⠑⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⠀⠀⠀⠙⠻⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣀⣤⡴⠞⠛⠉⠀⠀⠀⠀⠀⢠⡿⠁⠀⣠⣤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡀⠀⠀⠀⠈⠻⣦⡀⠀⠀⠀⠀⠀⠀⠀
⣠⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡁⠀⠤⣍⠉⠉⠀⣤⣀⣤⡀⢀⠀⠀⠀⠶⠷⣦⠀⠀⠈⣧⠀⠀⠀⠀⠀⠈⠻⣦⡀⠀⠀⠀⠀⠀
⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⡾⣷⡀⠀⠙⠀⠀⢀⣬⣿⣿⡿⣿⡁⠀⠀⠀⡀⠀⠠⢤⠀⣿⡀⠀⠀⠀⠀⠀⠀⠈⠛⢷⣄⠀⠀⠀
⠸⣆⠀⠀⠀⠀⠀⠀⣀⣤⠾⠋⠂⠊⠛⠶⢦⣴⠾⣿⡚⠷⣼⣿⠟⣹⣦⣀⠀⠑⠀⠀⢀⣴⠟⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢷⣆⠀
⠀⠙⠻⠶⠤⠴⠾⠛⠋⠀⠀⠀⠀⠀⠀⢀⣾⢁⣴⣟⠻⢦⡤⠼⢿⡏⠉⠻⣷⢶⣟⠛⣏⣁⡀⠙⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⠄
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⠛⠻⢟⣛⣛⣶⣾⢿⣄⠀⠘⠋⢿⡟⠋⠉⠛⢶⣌⠻⢦⣀⠀⠀⠀⠀⠀⢀⣴⡟⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡏⢠⣀⡀⠀⢉⣄⡀⠀⠈⠀⠀⠀⠘⣷⠀⢠⡄⠀⢹⡆⠀⠉⠛⠛⠲⠒⠚⠛⠁⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡁⠾⠏⢻⣤⡟⠉⢻⣆⠀⠀⠀⠀⠀⣿⠛⠛⠁⠀⣼⠇⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣷⠀⠀⢸⣿⠀⠀⠀⢹⡀⠀⠀⢀⣴⠿⢦⣤⣴⠾⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⠶⠟⠻⠷⠶⠶⠿⠷⠾⠚⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

"""
#First, defines a class of items, which includes the item code, item name, price, category of item, and stock of the item.
class Item:
    def __init__(self, code, name, price, category, stock):
        self.code = code
        self.name = name
        self.price = price
        self.category = category
        self.stock = stock

#This is used to define how many stock of the item there is.
    def Is_Available(self):
        return self.stock > 0
#This is used to dispense the item if the stock is available.
    def Dispense(self):
        if self.Is_Available(): #If the item is available, it will decrease the stock by 1.
            self.stock -= 1
            return True
        return False

#Now, this is defining the vending machine itself, and adding multiple algorithims inside the vending machine.
class VendingMachine:
    def __init__(self):
        
        self.items = {
            'A01': Item('A01', 'Kuromi Cappuccino', 11.99, 'Hot Drinks', 5),
            'A02': Item('A02', 'My Melody Caffe Mocha', 5.99, 'Hot Drinks', 5),
            'A03': Item('A03', 'Hello Kitty Hot Chocolate', 6.99, 'Hot Drinks', 10),
            'A04': Item('A04', 'Cinnamoroll Mochaccino', 12.99, 'Hot Drinks', 10),
            'A05': Item('A05', 'Pompompurin Spanish Latte', 11.99, 'Hot Drinks', 15),
            'A06': Item('A06', 'Cappuccino', 11.99, 'Hot Drinks', 10),
            'A07': Item('A07', 'Caffe Mocha', 7.99, 'Hot Drinks', 20),
            'A08': Item('A08', 'Ice Caramel Latte', 11.99, 'Hot Drinks', 15),
            'A09': Item('A09', 'Americano', 5.99, 'Hot Drinks', 25),
            'A10': Item('A10', 'Espresso', 4.99, 'Hot Drinks', 20),
            'A11': Item('A11', 'Meiji Apollo Strawberry Candy', 5.99, 'Sweets', 35),
            'A12': Item('A12', 'Cinnamoroll Crackers', 4.99, 'Sweets', 25),
            'A13': Item('A13', 'Kuromi Chocolate Bar', 5.99,'Sweets', 20),
            'A14': Item('A14', 'Hello Kitty Graham Crackers', 6.99,'Sweets', 25),
            'A15': Item('A15', 'Pompompurin Bar', 5.99,'Sweets', 15)
            #This is the amount of items inside the vending machine.
            #And each item has their own ID, Name, Price, Category, and Stock.
            #However, the category and stock is hidden from the program.
        }

       
        self.suggestions = {
            'A01': 'A13',  
            'A13': 'A01', 
            'A04':'A12',
            'A12':'A04',
            'A05':'A15',
            'A15':'A05',
            'A03':'A14',
            'A14':'A03'
            #This is used to suggest additonal items if the user buys a specific item that is connected to another item.
        }
        
#This is show the display of the vending machine.
    def Display_Menu(self):
        print("---------------- SANRIO VENDING MACHINE -------------")
        print("                                                     ")
        print("                                                     ")
        print("------------------   TOTAL ITEMS: -------------- \n ")
        for item in self.items.values(): #This is the display of items, their code, name and price.
        #The category and stock is hidden.
            print(f"{item.code}: {item.name} |  د.إ{item.price:.2f}")
        print("----------------------------------------------------")

    def User_Money(self): #This defines the amount of money the user will input.
        while True:
            try:
                money = float(input("\nPlease insert money:  د.إ"))
                if money <= 0: #If the user inputs a value lower or equal to 0, the program will not accept it.
                    print("Please insert a positive amount.")
                else:
                    return money
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

#This defines the function where the user will select an item via entering the item code.
    def Select_Items(self):
        while True:
            code = input("Please select an item by code:").upper()
            if code in self.items:
                if self.items[code].Is_Available():
                    return code
                else: #If the item is out of stock.
                    print("Sorry, this item is out of stock.")
            else: #If the user inputs an incorrect item code.
                print("Invalid code. Please try again.")

#This is where the user's money will go through a transaction process.
    def Transaction(self, money, code):
        item = self.items[code]
        if money >= item.price:
            if item.Dispense():
                change = money - item.price
                print(f"\nDispensing {item.name}...")
                return item, change  
            else: #It will fail to dispense if the item is unavailable.
                print("Failed to dispense the item. Please try again.")
                return None, 0  
        else:
            print("Insufficient funds. Please insert more money.")
            return None, 0  #The 0 is used to fix an attribute error in the code.

#This is used to define to suggest the user to buy another item related to the item they bought.
    def Additional_Item_Suggestion(self, code):
        if code in self.suggestions:
            suggested_code = self.suggestions[code]
            suggested_item = self.items[suggested_code]
            print(f"Suggestion: You might also like { suggested_item.name} ({suggested_item.price:.2f}).")

#This is used to print the receipt of the user's purchase.
#However, one drawback of the code is that, it prints one purchase at a time.
    def Receipt(self, item, change):
        print("\n------------------- RECEIPT -------------------")
        print(f"Item: {item.name} | Code: {item.code} | Price: د.إ{item.price:.2f}")
        if change > 0:
            print(f"Change returned: د.إ{change:.2f}\n")
            
        print("                                                  ")    
        print("                                                  ")    
        print("                                                  ")
        print("Thank you for your purchase.\n")
        print("-----------------------------------------------")
       
#This runs the actual vending machine algorithim itself, including the display, and its functions.
    def run(self):
        while True:
            self.Display_Menu()
            money = self.User_Money()
            code = self.Select_Items()
            item, change = self.Transaction(money, code)
            if item:
                self.Additional_Item_Suggestion(code)
                self.Receipt(item, change)
            AdditionalItem = input("Would you like to buy another item? (Y/N): ").strip().lower()
            if AdditionalItem != 'y':
                print("\nThank you for using the vending machine.")
                break

if __name__ == "__main__":
    vending_machine = VendingMachine()
    vending_machine.run()
    
"""
  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠴⢦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣴⣶⣶⣶⣶⣶⣶⣶⣤⣄⠀⠀⠀⠀⠘⠓⣦⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣾⣿⡿⠿⢿⣻⣿⣿⣟⣻⡿⠿⣿⣿⣷⣄⡀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣫⡵⠖⠋⠉⠁⠀⠀⠀⠀⠉⠙⠒⠿⣿⢿⣷⣦⢤⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⢴⣿⡟⡵⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠃⠹⣿⣷⣤⣈⠉⠛⠛⠓⠒⠚⠛⠛⠉⠉⠉⠙⢷⡄
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠞⣡⣾⡏⠅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⡏⠉⢣⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠋⢡⣾⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⠦⠤⢤⣤⡄⠀⢸⣿⣿⡇⠀⠘⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡟
⠀⠀⠀⣀⣀⣤⠴⠞⠉⠀⢠⡏⣿⣿⡏⠀⣀⡠⠴⠖⠃⠀⢀⠀⢀⠀⢰⡀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣇⠀⢰⡁⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠟⠁
⠀⣴⠞⠋⠀⠀⠀⠀⠀⠀⠘⣇⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠸⠾⠋⠙⢚⡃⠀⠀⠀⠀⠀⠀⠀⠀⣹⣿⣿⡦⠏⠙⠛⠶⠶⠤⠤⠴⠶⠛⠋⠁⠀⠀
⢸⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡟⠙⢷⡄⠀⣀⣀⣤⠴⠟⠉⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠘⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡼⠋⠉⠉⠛⠒⠲⢶⡶⡦⠴⠴⠶⠾⡇⠀⠀⢻⠛⠹⣍⣀⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠙⢷⣄⠀⠀⠀⠀⠀⣠⡴⠛⠀⠀⠀⠀⠀⠀⢀⣾⡣⠙⣦⠀⠀⠐⠁⠀⠀⠀⠀⠀⢻⡅⠀⡈⠉⢳⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠉⠉⠛⠚⠋⠉⠉⠀⠀⠀⠀⠀⠀⣠⠶⣾⠁⢸⣄⣼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣷⠀⢹⠄⠈⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣿⠀⠈⠃⠀⠉⠁⠀⠀⠀⠀⠀⡴⠶⣤⠀⠀⢸⡶⠛⠀⣰⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡀⠀⣠⡄⠀⠀⠀⠀⠀⠀⣾⡃⠀⠈⢃⣀⡼⠤⠤⠶⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠙⠓⠒⠒⠒⠶⠿⣤⣤⣤⡼⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""
