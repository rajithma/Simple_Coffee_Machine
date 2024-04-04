water = 1000
milk = 1000
coffee = 1000
cups = 1000
money = 0
choice = ""


def menu(option):
    if option == "1":
        buy_option()
    if option == "2":
        fill_option()
    if option == "3":
        income_option()  # amount of brewed coffees
    if option == "4":
        remaining_option()


def machine_details(machine_water, machine_milk, machine_coffee, machine_cups, machine_money):
    print("\nMachine haves : ")
    print("Water = " + str(machine_water))
    print("Milk = " + str(machine_milk))
    print("Coffee beans = " + str(machine_coffee))
    print("Coffee cups = " + str(machine_cups))


def buy_option():
    # user selected option
    buy_answer = int(input("""
    [1]-ESPRESSO        LKR 100.00      Italy
    [2]-BLACK COFFEE    LKR  50.00      Ethiopia
    [3]-CAPPUCCINO      LKR 200.00      Italy
    [0]-MAIN MENU \n\nSelect your choice : """))

    if buy_answer == 1:
        machine_content(buy_answer)
    if buy_answer == 2:
        machine_content(buy_answer)
    if buy_answer == 3:
        machine_content(buy_answer)
    if buy_answer == 0:
        pass


def fill_option():
    global water, milk, coffee, cups, money
    fill_water = int(input("Quantity of add water (ml) : "))
    water = water + fill_water
    fill_milk = int(input("Quantity of add milk (g) : "))
    milk = milk + fill_milk
    fill_coffee = int(input("Quantity of add coffee beans (g) : "))
    coffee = coffee + fill_coffee
    fill_cups = int(input("Quantity of add disposable cups : "))
    cups = cups + fill_cups
    # return machine_details(water, milk, coffee, cups, money)


def income_option():
    global water, milk, coffee, cups, money
    print("\nMachine have $ " + str(money))
    # return machine_details(water, milk, coffee, cups, money)


def remaining_option():
    machine_details(water, milk, coffee, cups, money)


def machine_content(cal_answer):
    global water, milk, coffee, cups, money
    if cal_answer == 1:
        price = int(input("Please enter money LKR : "))
        bal = price - 100
        if price >= 100:
            if water < 200 or milk < 50 or coffee < 15 or cups < 1:
                check_content(cal_answer)
            elif water >= 200 and coffee >= 15 and cups >= 1:
                print("Here your balance LKR : " + str(bal))
                print("\nMaking your coffee, Please wait !")
                print("Making your coffee, Please wait !")
                print("Making your coffee, Please wait !")
                print("Here is your coffee, Enjoy your coffee :)")

                water = water - 200
                milk = milk - 50
                coffee = coffee - 15
                cups = cups - 1
                money = money + 100
        # if (water or milk or coffee or cups or money) enough
        #     check_content(cal_answer)
        # else print("I'm making you a coffee, Please wait !")
        else:
            print("Money not enough sir !")

    if cal_answer == 2:
        price = int(input("Please enter money LKR : "))
        bal = price - 50

        if price >= 50:
            if water < 200 or coffee < 20 or cups < 1:
                check_content(cal_answer)
            elif water >= 200 and coffee >= 20 and cups >= 1:
                print("\nHere your balance LKR : " + str(bal))
                print("\nMaking your coffee, Please wait !")
                print("Making your coffee, Please wait !")
                print("Making your coffee, Please wait !")
                print("Here is your coffee, Enjoy your coffee :)")
                water = water - 200
                coffee = coffee - 20
                cups = cups - 1
                money = money + 50
        # if (water or milk or coffee or cups or money) enough
        #     check_content(cal_answer)
        # else print("I'm making you a coffee, Please wait !")
        else:
            print("Money not enough sir !")
    if cal_answer == 3:
        price = int(input("Please enter money LKR : "))
        bal = price - 200

        if price >= 200:
            if water < 250 or milk < 100 or coffee < 10 or cups < 1:
                check_content(cal_answer)
            else:
                print("Here your balance LKR : " + str(bal))
                print("\nMaking your coffee, Please wait !")
                print("Making your coffee, Please wait !")
                print("Making your coffee, Please wait !")
                print("Here is your coffee, Enjoy your coffee :)")

                water = water - 250
                milk = milk - 100
                coffee = coffee - 10
                cups = cups - 1
                money = money + 200
        # if (water or milk or coffee or cups or money) enough
        #     check_content(cal_answer)
        # else print("I'm making you a coffee, Please wait !")
        else:
            print("Money not enough sir !")


def check_content(option):
    global water, milk, coffee, cups, money
    if option == 1:
        min_water = 200
        min_milk = 50
        min_coffee = 15
        min_cup = 1
        if water < min_water:
            print("Sorry sir, water not enough !")

        if milk < min_milk:
            print("Sorry sir, milk not enough !")

        if coffee <= min_coffee:
            print("Sorry sir, coffee not enough !")

        if cups <= min_cup:
            print("Sorry sir, cups not enough !")

    if option == 2:
        min_water = 200
        min_coffee = 20
        min_cup = 1
        if water < min_water:
            print("Sorry sir, water not enough !")

        if coffee <= min_coffee:
            print("Sorry sir, coffee not enough !")

        if cups <= min_cup:
            print("Sorry sir, cups not enough !")

    if option == 3:
        min_water = 250
        min_milk = 100
        min_coffee = 10
        min_cup = 1
        if water < min_water:
            print("Sorry sir, water not enough !")

        if milk < min_milk:
            print("Sorry sir, milk not enough !")

        if coffee <= min_coffee:
            print("Sorry sir, coffee not enough !")

        if cups <= min_cup:
            print("Sorry sir, cups not enough !")


on = True
while on:
    # machine_details(water, milk, coffee, cups, money)
    choice = input("""\n____________________________________________________________________
================ WELCOME FRESH BEAN COFFEE SHOP ====================
____________________________________________________________________
[1]-buy                 [2]-fill            [3]-brewed coffees money 
[4]-remaining material  [0]-exit \n\nSelect action : """)
    if choice == "0":
        break
    menu(choice)
