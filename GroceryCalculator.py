class Item:

    #Constructor
    def __init__(self, name, price, taxable):
        self.name = name
        self.price = price
        self.taxable = taxable  

    def comparePrice(self, otherItemPrice):
        return (self.price > otherItemPrice)

    def changeName(self, newName):
        self.name = name

    def changePrice(self, newPrice):
        self.price = price

    def itemDisplay(self):
        return "Item: " + self.name + " $" + str(self.price) + "\n"

    #Function to determine if Item should be taxed (assuming PST exempt, and GST = 5%)
    def shouldItemBeTaxed(self):
        if(self.taxable):
             tax = float(self.price) * 0.05
             total = float(self.price) + tax
             return total
        return float(self.price)



class Cart:

    #Constructor
    def __init__(self, cartOwnerName, cart):
        self.cartOwnerName = cartOwnerName
        #Start off with cart having 10 spaces, more space will be created if necessary
        self.cart = [None] * 10

    #Function to add item to cart
    def add(self, itemToAdd):
        x = 0
        #Use while loop to find where to put Item in array
        while(x < len(self.cart)):
            if(self.cart[x] == None):
                self.cart[x] = itemToAdd
                return
            else:
                x = x + 1
        #If while loop is exited, then more space must be added to cart in order to accomodate more items 
        expandBy = (len(self.cart)) + 10
        newCart = [None] * expandBy
        x = 0
        while(x < len(self.cart)):
            newCart[x] = self.cart[x]
            x = x + 1
        self.cart = newCart

    #Function to display Items in cart
    def displayCart(self):
        print("Cart owner: " + str(self.cartOwnerName))
        print("Items in cart: ")
        x = 0
        #Use while loop to print out each Item
        while(self.cart[x] != None or x == len(self.cart)):
            print(self.cart[x].itemDisplay())
            x = x + 1

    #Function to calculate total price of groceries
    def totalPrice(self):
        total = 0
        x = 0
        #Use while loop to calculate full cost (including tax cost)
        while(self.cart[x] != None or x == len(self.cart)):
            total = total + self.cart[x].shouldItemBeTaxed()
            x = x + 1
        print("Your total grocery cost is: " + str(round(total, 2)))

#Function to start up program
def start():
    name = input("What is your name? ")
    newCart = Cart(name, [])
    print("Please know that these items are taxable: alcohol (including non-alcoholic), carbonated beverages, fruit juice beverages, beverages, puddings, bulk or unbottled water, candy, bars (any type of bar), snack foods, ice cream (including similar products), fruit based snack foods, sweetened goods (including similar products), heated foods or beverages, salads, sandwiches, platters, dispensed beverages")
    x = 0
    while True:
        answer = input("Would you like to continue? ")
        if(answer == "no"):
            break
        options(newCart)

#Function for options menu
def options(newCart):
    choice = input(".Add item (a) " + "\n" ".Print cart (p)" + "\n" + ".Calculate total price (t) " + "\n")
        
    #To add Item to Cart
    if(choice == 'a' or choice == 'A'):
        itemName = input("What is the name of your item? ")
        price = input("What is the price of your item? ")
        taxable = input("Is your item taxable? ")

        if(taxable == "YES" or taxable == "yes" or taxable == "y" or taxable == "Y" or taxable == "True" or taxable == "TRUE" or taxable == "true"):
            newItem = Item(itemName, price, True)
            newCart.add(newItem)

        elif(taxable == "NO" or taxable == "no" or taxable == "no" or taxable == "N" or taxable == "False" or taxable == "false" or taxable == "FALSE"):
            newItem = Item(itemName, price, False)
            newCart.add(newItem)

        else:
            print("Invalid command entered. Please try again.")
            options(newCart) 
    
    #To print Item in Cart
    elif(choice == 'p' or choice == 'P'):
        newCart.displayCart()

    #To get total price of Item in Cart 
    elif(choice == 't' or choice == 'T'):
        newCart.totalPrice()

    #If no valid command entered
    else:
        print("Invalid command entered. Please try again.")
        options(newCart)

#Run to start program
start()

  
    
    
            
            
        

    


       

