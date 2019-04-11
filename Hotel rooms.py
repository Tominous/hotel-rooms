

types=["     ","B&B","Half-board","Full-board"]
r1=["Room 1","25","35","45"]
r2=["Room 2","30","40","50"]
r3=["Room 3","35","50","65"]
allrooms=[types,r1,r2,r3]


def menu():
    print("\n************MENU***********")
    print("(1) Display all prices")
    print("(2) Display a specific price")
    print("(3) Change price")
    print("(4) Exit")
    print("\n***************************")

    option=input("\nPlease choose an option :")
    
    if option == "1":
        O1()
        
    elif option == "2":
        O2()
            
    elif option == "3":
        O3()

    elif option == "4":
        O4()
                
    else:
        print("Incorrect")

def finished():
    r_menu=input("\nDo you want to go back to the menu. Y or N:")

    if r_menu == "Y":
        menu()

    else:
        print("\nGood bye")
    

def O1():
    for each in allrooms:
              print(" ")
              for eachitem in each:
                      print("{0:>20}".format(eachitem),end=" ")

    print("\n")

    finished()

def O2():
    C_type=int(input("Enter room type (1)B&B, (2)Half-Board or (3)Full-Board: "))
    C_room=int(input("Enter room number(1),(2) or (3): "))
    ans=(allrooms[C_room][C_type])
    print("\nThe price of room {0}, {1} is £{2} per night".format(C_type,types[C_type],ans))

    finished()

def O3():
    print("Which price do you wish to change ")
    c_type=int(input("Enter board type (1)B&B, (2)Half Board or (3)Full Board: "))
    c_choice=int(input("Enter room number(1),(2) or (3): "))
    value=int(input("Enter new price "))
    allrooms[c_choice][c_type]=value
    O1()
    finished()

def O4():
    print("\nGood bye")

menu()
              
          
          
