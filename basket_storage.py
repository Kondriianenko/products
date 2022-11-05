basket = {}  # dict of products' dicts
def generete_reseivt():
    extra_text=('Total price = ')
    file = open("reseivt.txt", "w")
    file.write(str(basket))
    file.write(extra_text+str(get_cost()))
    file.close()
    print("your reseivt has been received")


def get_choice(text):
    return input(text)


def print_basket():
    print(basket)


def print_manual():
    print("this basket uses console interface, to interact with it you have to type commands. \nHere is the list of "
          "commands you need: \n  stop - if, instead of product you type stop you finish editing the basket and go to "
          "the main menu  \n  info - call this manual; \n  basket - enter the basket; \n  clear - clear the basket; "
          "\n  delete - delete exact product from the basket; \n  edit_price - edit price of an exact product; \n  "
          "edit_amount - edit amount of an exact product.")


def input_product():
    return input("Input product = ")


def input_price():
    while True:
        try:
            return float(input("Input price = "))
        except ValueError:
            print("Price must be a number")


def input_amount():
    while True:
        try:
            return int(input("Input amount = "))
        except ValueError:
            print("Amount must be a natural number")


def update_basket(product, price, amount):
    """
    Adding data to the basket
    """
    basket[product] = {"price": price,
                       "amount": amount,
                       "total price": price * amount}


def get_cost():
    """
    Iterate through the dictionary to calculate the total price for each product
    return --> sum var
    """
    suma = 0
    for product in list(basket.keys()):
        suma += basket[product]["total price"]
    return suma


def delete_product():
    while True:
        try:
            basket.pop(get_choice("which product do you want to exclude from the basket?"))
            return
        except KeyError:
            print("this product does not exist")


def edit_price():
    while True:
        product = get_choice("price of which product do you want to edit?")
        try:
            basket[product]["price"] = input_price()
            basket[product]["total price"] = basket[product]["price"] * basket[product]["amount"]
            return
        except KeyError:
            print("this product does not exist")


def edit_amount():
    while True:
        product = get_choice("amount of which product do you want to edit?")
        try:
            basket[product]["amount"] = input_amount()
            basket[product]["total price"] = basket[product]["price"] * basket[product]["amount"]
            return
        except KeyError:
            print("this product does not exist")


def basket_program():
    while True:
        print_basket()
        product = input_product()
        if product == 'stop':
            break
        price = input_price()
        amount = input_amount()
        update_basket(product, price, amount)
        print("cost of all the products = ", get_cost())


print_manual()
while True:
    choice = get_choice("type your command here(basket/clear/delete/edit_price/edit_amount/info)")
    if choice == "basket":
        basket_program()
    elif choice == "clear":
        basket.clear()
        print_basket()
    elif choice == "delete":
        print_basket()
        delete_product()
        print_basket()
    elif choice == "edit_price":
        print_basket()
        edit_price()
        print_basket()
    elif choice == "edit_amount":
        print_basket()
        edit_amount()
        print_basket()
    elif choice == "info":
        print_manual()
    elif choice == "buy":
        generete_reseivt()
    else:
        print("invalid command")
