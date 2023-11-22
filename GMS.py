# author: jy-liew

def login():    # login() function
    try:
        customer_db = open("customer database.txt", "r")  
    except:
        print("File cannot be opened: customer database.txt")  
        quit()                                                 
    try:
        admin_db = open("admin database.txt", "r") 
    except:
        print("File cannot be opened: admin database.txt")  
        quit()                                              

    success_customer = False                    
    success_admin = False                       
    userid = input("Enter your User ID: ")      
    password = input("Enter your Password: ")   

    if len(userid) < 1 and len(password) < 1:   # if length of userid and length of password are less than 1 (nothing was entered)
        print("No user ID and password were entered.\n")   
        login()                                 

    elif len(userid) < 1:                    # if length of userid is less than 1 (nothing was entered)
        print("No user ID was entered.\n")   
        login()                              

    elif len(password) < 1:                   # if length of password is less than 1 (nothing was entered)
        print("No password was entered.\n")   
        login()                               

    else: 
        for line in customer_db:          # for each line in customer_db
            if ";" in line:               
                a, b = line.split("; ")   # split line at "; " and assign the first part as 'a' variable, second part as 'b' variable
                b = b.strip()             # remove whitespace from string
                if userid == a and password == b:  
                    success_customer = True        
                    break                          

        for line in admin_db:            # for each line in admin_db
            if ";" in line:              
                a, b = line.split("; ")  # split line at "; " and assign the first part as 'a' variable, second part as 'b' variable
                b = b.strip()            # remove whitespace from string
                if userid == a and password == b:   
                    success_admin = True            
                    break                           

        customer_db.close()    
        admin_db.close()       

        if success_customer == True:    # if customer log ins successfully
            print("Customer login successful.\n")  
            customer_menu(userid)                  

        elif success_admin == True:     # if admin log ins successfully
            print("Administrator login successful.\n")
            admin_menu()

        else:
            print("Wrong user ID or password was entered.\n")
            while True:
                choice = input("Enter 1 to try again or 2 to exit: ")  
                if choice == "1":                        
                    login()
                elif choice == "2":                      
                    quit()
                else:                                    
                    print("Error: Invalid selection")
                    continue                             


def admin_menu():       # admin_menu() function
    print("-" * 20)
    print("MENU (Administrator)")                
    print("-" * 20)
    print("1. Upload grocery details")           
    print("2. View all groceries")
    print("3. Modify grocery details")
    print("4. Delete grocery")
    print("5. Search grocery details")
    print("6. View all orders of customers")
    print("7. Search order of specific customer")
    print("8. Exit\n")

    while True:
        result = input("Please select by entering 1, 2, 3, 4, 5, 6, 7, 8: ")  
        print("")              

        if result == "1":      
            upload_grocery()
            admin_menu()       
        elif result == "2":    
            view_grocery()
            admin_menu()       
        elif result == "3":   
            modify_grocery()
            admin_menu()     
        elif result == "4":   
            delete_grocery()
            admin_menu()     
        elif result == "5":   
            search_grocery()
            admin_menu()      
        elif result == "6":    
            view_all_orders()
            admin_menu()      
        elif result == "7":   
            search_order()
            admin_menu()       
        elif result == "8":   
            quit()
        else:                 
            print("Error: Invalid selection")
            continue


def upload_grocery():   # upload_grocery() function
    try:
        groceries_file = open("groceries.txt", "a")    
    except:
        print("File cannot be opened: groceries.txt")   
        quit()                                          
    
    master_groceries = []     # master list
    grocery = []              # list

    name = input("Enter name: ")     
    grocery.append(name)             
    units = input("Enter unit: ")    
    grocery.append(units + " units")               
    details = input("Enter detail of grocery: ")
    grocery.append(details)
    exp_date = input("Enter expire date: ")
    grocery.append(exp_date)
    price = str(input("Enter price: RM "))
    grocery.append("RM " + price)
    master_groceries.append(grocery)

    for item in master_groceries:             # for each item in master_groceries
        for detail in item:                   # for each detail in item
            groceries_file.write(detail)      # write detail into text file
            groceries_file.write("\t")        
        groceries_file.write("\n")            
    groceries_file.close()                    
    print("Grocery has been uploaded successfully.\n")  


def view_grocery():     # view_grocery() function
    try:
        groceries_file = open("groceries.txt", "r")     
    except:
        print("File cannot be opened: groceries.txt")   
        quit()                                          
        
    print("Available groceries:")    
    print(groceries_file.read())     # print all the strings that are read from text file
    groceries_file.close()           


def modify_grocery():   # modify_grocery() function
    try:
        groceries_file = open("groceries.txt", "r")     
    except:
        print("File cannot be opened: groceries.txt")   
        quit()                                          

    print("Available Groceries:")                                 
    print(groceries_file.read())    # print all the strings that are read from text file
    print("Choose the grocery you want to modify.")               
    print("Type 1 for first product, 2 for second product, etc")  
    
    groceries_file.seek(0)                      # change the position of the file handle to the beginning in text file
    groceries = groceries_file.readlines()      # read all the lines in text file then insert each line as a string element in 'groceries' list
    while True:
        try:
            choice_grocery = int(input("> "))                  
            list1 = groceries[choice_grocery - 1].split("\t")  # split the chosen string element in 'groceries' list at tab and insert each part into list1
            list1.pop()                                        # remove the last element in list1: '\n'
            break                                              
        except:
            print("Error: The value entered is too big or not an integer.")  
                                                                             

    print("Choose the detail you want to modify")                        
    print("Type 1 for name, type 2 for units, type 3 for details, etc")  
    while True:
        try:
            choice_detail = int(input("> "))    # whileloop to get choice of detail to modify from user (must be integer)
            list1[choice_detail - 1]            # check if index entered by user exceeds index of list1
            break                               
        except:
            print("Error: The value entered is too big or not an integer.")  


    new_detail = input("Enter the new detail: ")       
    list1[choice_detail - 1] = new_detail       # set chosen detail in list1 as new detail

    groceries_file = open("groceries.txt", "w")        
    for item in groceries:                              # for every item in 'groceries' list
        if groceries[choice_grocery - 1] != item:       # write every item to text file except for the chosen item to modify
            groceries_file.write(item)

    groceries_file = open("groceries.txt", "a")         
    for detail in list1:                # for every detail in list1
        groceries_file.write(detail)    # write detail into text file
        groceries_file.write("\t")                      
    groceries_file.write("\n")                          
    groceries_file.close()                              
    print("Grocery has been modified successfully.\n")  


def delete_grocery():   # delete_grocery() function
    try:
        groceries_file = open("groceries.txt", "r")

    except:
        print("File cannot be opened: groceries.txt")   
        quit()                                          

    filedata = groceries_file.read()    # read all the lines in text file and store them as strings in 'filedata' variable
    print("Available groceries:")                         
    print(filedata)                     # print all the strings that are stored in 'filedata' variable
    print("Enter the name of grocery you want to delete")  
    print("Example: Massimo Bread")                        

    while True:
        name = input("> ")                                  
        if name not in filedata:    # if name of grocery is not in filedata
            print("The grocery entered is not available.")  
            continue                                        
        else:                                               
            break                                           

    groceries_file.seek(0)                      # change the position of the file handle to the beginning in text file
    groceries = groceries_file.readlines()      # read all the lines in text file then insert each line as a string element in 'groceries' list
    groceries_file = open("groceries.txt", "w")
    for item in groceries:                      # for every item in 'groceries' list
        if name not in item:                    # write every item to text file except for the chosen item to delete
            groceries_file.write(item)
    
    groceries_file.close()
    print("Grocery has been deleted successfully.\n")  


def search_grocery():   # search_grocery() function
    try:
        groceries_file = open("groceries.txt", "r")      

    except:
        print("File cannot be opened: groceries.txt")    
        quit()                                           

    print("Enter the grocery detail to search:")                
    print("Example: Mi Sedap Noodle, 50 units, RM 4.75, etc")   

    filedata = groceries_file.read()    # read all the lines in text file and store them as strings in 'filedata' variable
    while True:
        detail = input("> ")                            # whileloop to get detail of grocery to search from user
        if detail.lower() not in filedata.lower():      # if detail of grocery is not in filedata
            print("The detail entered does not match any grocery.")  
            continue                                                 
        else:                                                        
            break                                                    

    groceries_file.seek(0)                  # change the position of the file handle to the beginning in text file
    for line in groceries_file:             # for every line in text file
        line = line.rstrip()                # remove newline after each string
        if detail.lower() in line.lower():  # print line if detail of grocery is in line
            print(line)
    print("")                 
    groceries_file.close()    


def view_all_orders():      # view_all_orders() function
    try:
        orders_file = open("orders.txt", "r")       
    except:
        print("File cannot be opened: orders.txt")  
        quit()                                      

    print("All customer orders:")                   
    print(orders_file.read())   # print all the strings that are read from text file
    orders_file.close()                             


def search_order():     # search_order() function
    try:
        orders_file = open("orders.txt", "r")        
    except:
        print("File cannot be opened: orders.txt")   
        quit()                                       

    print("Enter the name of customer to search:")   

    filedata = orders_file.read()                    # read all the lines in text file and store them as strings in 'filedata' variable
    while True:
        name = input("> ")                          # whileloop to get name of customer from user
        if name.lower() not in filedata.lower():    # if name of customer is not in filedata
            print("The customer entered has not made an order.")  
            continue                                              
        else:                                                     
            print("\nOrders by", name.capitalize())               
            break                                         

    orders_file.seek(0)                               # change the position of the file handle to the beginning in text file
    for line in orders_file:                          # for every line in text file
        line = line.rstrip()                          # remove newline after each string
        if (line.lower()).startswith(name.lower()):   # if the line starts with name of customer
            print(line)
    print("")                                         
    orders_file.close()                               


def new_customer_menu():    # new_customer_menu() function
    print("-" * 20)
    print("MENU (New Customer)")        
    print("-" * 20)
    print("1. View all groceries")      
    print("2. Register a customer account")
    print("3. Exit\n")

    while True:
        result = input("Please select by entering 1, 2 or 3: ")  
        print("")           

        if result == "1":          
            view_grocery()
            new_customer_menu()    
        elif result == "2":     
            register()
            new_customer_menu()  
        elif result == "3":    
            quit()
        else:                 
            print("Error: Invalid selection")
            continue          


def register():     # register() function
    try:
        customer_db = open("customer database.txt", "a")
    except:    
        print("File cannot be opened: customer database.txt")   
        quit()                               

    name = input("Name: ")                    
    address = input("Address: ")
    contact_num = input("Contact Number: ")
    gender = input("Gender: ")
    d_o_b = input("Date of Birth: ")
    email = input("Email: ")
    userid = input("User ID: ")

    while True:
        password = input("Password: ")                        # whileloop to get password from user
        password_confirm = input("Confirm your password: ")   

        if password != password_confirm:                      # if the passwords entered are not the same
            print("Passwords entered do not match. Please enter the password again.\n")  
            continue                                         
        else:                                                 
            break                                             
    
    if len(userid) < 1 and len(password) < 1:              # if length of userid and length of password are less than 1 (nothing was entered)
        print("No user ID and password were entered.\n")   
        register()                                         

    elif len(userid) < 1:                                  # if length of userid is less than 1 (nothing was entered)
        print("No user ID was entered.\n")                 
        register()                                         

    elif len(password) < 1:                                # if length of password is less than 1 (nothing was entered)
        print("No password was entered.\n")                
        register()                                         
    
    else:                                                  
        customer_db.write("User ID: " + userid + "\n")     # write userid, name, address, contact number, gender, date of birth, email and password to text file 
        customer_db.write("Name: " + name + "\n")
        customer_db.write("Address: " + address + "\n")
        customer_db.write("Contact Number: " + contact_num + "\n")
        customer_db.write("Gender: " + gender + "\n")
        customer_db.write("Date of Birth: " + d_o_b + "\n")
        customer_db.write("Email: " + email + "\n")
        customer_db.write(userid + "; " + password + "\n\n")
        customer_db.close()                                        
        print("\nCustomer account successfully created!\n")        


def customer_menu(userid):      # customer_menu(userid) function has 1 parameter
    print("-" * 27)
    print("MENU (Registered Customer)")   
    print("-" * 27)
    print("1. View all groceries")     
    print("2. Order groceries")
    print("3. View own order")
    print("4. View personal informaton")
    print("5. Exit\n")

    while True:
        result = input("Please select by entering 1, 2, 3 or 4: ") 
        print("")                                        

        if result == "1":          
            view_grocery()
            customer_menu(userid)   
        elif result == "2":       
            order(userid)
            customer_menu(userid)  
        elif result == "3":        
            view_own_order(userid)
            customer_menu(userid)      
        elif result == "4":            
            view_personal_info(userid)
            customer_menu(userid)     
        elif result == "5":         
            quit()
        else:                      
            print("Error: Invalid selection")
            continue                


def get_name_from_userid(userid):       # function get_name_from_userid(userid) has 1 parameter
    try:
        customer_db = open("customer database.txt", "r")        
    except:
        print("File cannot be opened: customer database.txt")  
        quit()                                                  

    list1 = customer_db.readlines()                             # read all the lines in text file then insert each line as a string element in list1
    customer_db.close()                         

    index_of_userid = list1.index("User ID: " + userid + "\n")  # find the index of customer's userid in list1 and store the index in 'index_of_userid' variable
    name = (list1[index_of_userid + 1].split(" "))[1]           # split the string element that contains customer's name in list1 at space and store the second part in 'name' variable
                                                                # index_of_userid + 1 = index of string element that contains customer's name
    name = name.rstrip()     # remove newline after the string
    return(name)


def order(userid):      # function order(userid) has 1 parameter
    try:
        groceries_file = open("groceries.txt", "r")                     
    except:
        print("File cannot be opened: groceries.txt")                  
        quit()                                                       

    print("Available Groceries:")                                     
    print(groceries_file.read())                                        # print all the strings that are read from text file
    print("Choose the grocery you want to order.")                  
    print("Type 1 for first product, type 2 for second product, etc")
    
    groceries_file.seek(0)                             # change the position of the file handle to the beginning in text file
    groceries = groceries_file.readlines()             # read all the lines in text file then insert each line as a string element in 'groceries' list
    while True:
        try:
            choice = int(input("> "))                      # whileloop to get choice of grocery from user (must be integer)
            if choice > 0:                                 # if statement to check whether value entered is positive
                list1 = groceries[choice - 1].split("\t")  # split the chosen string element of 'groceries' list at tab and insert each part into list1
                break                                      
            else:
                print("Error: The value entered is invalid.")  # print error message if value entered is a negative number
                continue                                       
        except:
            print("Error: The value entered is too big or not an integer.")  # print error message if input from user is not in the form of integer
                                                                             # or exceeds index of 'groceries' list

    while True:
        try:
            units = int(input("How many units do you want? "))                      # whileloop to get units of grocery from user (must be integer)
            if units > int((list1[1].split(" "))[0]):                               # if units of grocery is more than stock available then print error message
                print("Error: The value entered is greater than stock available.")  # stock available = the first part of split the second string element of list1 at space
                continue                                                            
            elif units <= 0:                                                        # if negative value is entered, an error message is displayed
                print("Error: The value entered is invalid.")
                continue                                                            
            else:                                                                   # if units of grocery does not exceed the stock available
                break                                                               

        except:
                print("Error: Value entered is not an integer.")                    # print error message if input from user is not in the form of integer

    price = (list1[4].split(" "))[1]         # split the fifth string element of list1 at space and store the second part in 'price' variable
    price = (float(price)) * units           # multiply price of grocery with units to get the total price 
    price = round(price, 2)                  # round the total price to 2 decimal places
    print("Amount to be paid: RM", price)

    while True:
        try:
            amount_paid = float(input("Your payment amount: RM "))  # whileloop to get amount of money paid from user (must be float)
            break                                       
        except:
            print("Error: Value entered is not a number")           # print error message if input from user is not in the form of floating point number

    difference = round(amount_paid - price, 2)          # round the result of subtracting total price from amount of money paid to 2 decimal places


    def write_to_file():    # write_to_file() function
        try:
            orders_file = open("orders.txt", 'a')       
        except:
            print("File cannot be opened: orders.txt")  
            quit()                             
        
        name = get_name_from_userid(userid)           # get the customer's name using userid
        orders_file.write(name + "\t")                # write customer's name, name of grocery, units of grocery and total price into text file
        orders_file.write(list1[0] + "\t")            # list1[0] = the first string element in list1 that contains the name of grocery
        orders_file.write(str(units) + " units\t")
        orders_file.write("RM " + str(price) + "\n")
        orders_file.close()
    
    if difference == 0:     # if difference is equal to 0
        print("Purchase successful.\n")     
        write_to_file()

    elif difference > 0:    # if difference is a positive value      
        print("Purchase successful. RM", str(difference), "will be given as change.\n")
        write_to_file()

    elif difference < 0:    # if difference is a negative value
        print("Purchase failed. RM", str(difference), "still needs to be paid.\n")

    groceries_file.close()


def view_own_order(userid):     # function view_own_order(userid) has 1 parameter
    try:
        orders_file = open("orders.txt", "r")        
    except:
        print("File cannot be opened: orders.txt")   
        quit()                     

    filedata = orders_file.read()                # read all the lines in text file and store them as strings in 'filedata' variable        

    name = get_name_from_userid(userid)          # get the customer's name using userid        
    if name.lower() not in filedata.lower():     # if customer's name is not in filedata
        print("You have not made an order.\n")

    else:
        orders_file.seek(0)                      # change the position of the file handle to the beginning in text file   
        for line in orders_file:                 # for every line in text file
            line = line.rstrip()                 # remove newline after each string
            if (line.lower()).startswith(name.lower()):  # if the line starts with customer's name
                print(line)
        print("")                    
    orders_file.close()                


def view_personal_info(userid):     # view_personal_info(userid) function has 1 parameter
    try:
        customer_db = open("customer database.txt", "r")        
    except:
        print("File cannot be opened: customer database.txt")   
        quit()                                                  

    list1 = customer_db.readlines()                         # read all the lines in text file then insert each line as a string element in list1
    start = list1.index("User ID: " + userid + "\n") + 1    # index of customer's userid in list1 + 1 = index of customer's name in list1
    end = start + 5                                         # start + 5 = index of customer's email in list1
    
    for detail in list1[start:end + 1]:   # forloop to print customer's details in list1 from name to email
        detail = detail.rstrip()          # remove newline after each string
        print(detail)
    print("")                     
    customer_db.close()            


print("-" * 36)     # Main program
print("FRESHCO Groceries Management System")
print("-" * 36)
print("""WELCOME user
1. Administrator Login          
2. New Customer
3. Registered Customer Login
4. Exit
""")
    
while True:
    result = input("Please select by entering 1, 2, 3 or 4: ")
    print("")

    if result == "1":    
        login()
    elif result == "2":  
        new_customer_menu()
    elif result == "3": 
        login()
    elif result == "4":  
        quit()
    else:             
        print("Error: Invalid selection")
        continue
