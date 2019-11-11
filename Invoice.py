# -------------------------------------------------------------------------------
# Name: Nathan Workman
# Date:   3/12/19
# Assignment:  Project 2 - Autoshop Selection
# Description:   Calculate an invoice for automotive services.
# -------------------------------------------------------------------------------
service1=''         #Initializing The varaible service1
service2=''         #Initializing The varaible service2
Menu = ''           #Initializing The varaible Menu
Cost = ''           #Initializing The varaible Cost
tax =''             #Initializing The varaible tax
grandtotal =''      #Initializing The varaible grandtotal

print("Hello! Welcome to AutoParts! Please look at the menu and choose the services needed by typing the service")      #Prints welcome message and instructions for selection
print("There is also a 6% tax on all services.")                        #Reminds User that there is a 6% tax on all services
print('Oil Change - $35\nTire Rotation - $19\nCar Wash - $7\nCar Wax - $12')        #prints services menu for selection
Menu = {'Oil Change':35,'Tire Rotation':19,'Car Wash':7,'Car Wax':12,'None':0}       #Creates a dictionary of the menu, pairs the price to the serivce
service1 = input('Service 1: ')             #Gets input from user user for first service selection
if service1 not in Menu:                    #If-statement, if what is inputed isnt on the menu(Dictionary) then prints, this is not a selection
    print("This is not a selection")
    exit()                                  #Exits program if something not allowed was inputed/stops the code from having an error
service2= input('Service 2: (If no second service is needed just enter ‘-‘)')    #Gets input from  user for second service selection
if service2 == '-':        #If no second service is wanted and '-' is entered then it assignes the value of none a price of zero, allows for just one service to be selected
    service2 = 'None'
elif service2 not in Menu:    #If-statement, if what is inputed isnt on the menu(Dictionary) then prints, this is not a selection
    print('This is not a selection')
    exit()                      #Exits program if something not allowed was inputed/stops the code from having an error
Cost = Menu[service1] + Menu[service2]     #Adds the paired prices together from the services located in the Dictionary
tax = Cost * .06                            #Calculates the tax based on the price from the two services combined
grandtotal = Cost + tax                     #Gets a grand total by adding the cost of the two services and the tax together
print("Here is your automated invoice for todays vist")        #Prints here is your invoice for today
print("Service 1:",service1,'$',Menu[service1])                 #Prints the service selected and the price of that service
print('Service 2:', service2,'$',Menu[service2])                #Prints the  second service selected and the price of that service
print("Tax:",'$', tax)                                            #Prints the curent tac on those services combined
print("Grand Total:", '$',grandtotal)                              #Prints grandtotal of the whole vist
print('Thank you for your vist! Come Again!')                    #prints a thank you/come again moto

