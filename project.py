basket = {} #list of products' dicts
manual='this basket uses console interface, to interact with it you have to type commands. \nHere is the list of commands you need: \n  stop - if, instead of product you type stop you finish editing the basket and go to the main menu  \n  info - call this manual; \n  basket - enter the basket; \n  clear - clear the basket; \n  delete - delete exact product from the basket; \n  edit_price - edit price of an exact product; \n  edit_amount - edit amount of an exact product; \n  sum - get the the total price of all the products." #variable that contains manual of how to use the program'

def basket_program():
    suma = 0
    while(True):
        product = input("product:")
        if product == "stop":
            break
        price = int(input("price of the product:"))
        amount = int(input("amount of the product on storage:"))
        totalp = price*amount
        basket[product]= {"price": price, "amount": amount,"totalp": totalp}
        print(basket)
basket_program()
while(True):
    choice=input('if you want redact your basket type "basket" or "clear" or "delete" or if you want to change prise of some product type "change prise"or if you want to change amount of some product type "change amount" or if you want to open manual type manual')
    if choice=='basket':
        basket_program()
    elif choice == 'clear':
        basket.clear()
    elif choice == 'delete':
        print(basket)
        dkey=input('which product you want to exclude from the basket?')
        basket.pop(dkey)
        print(basket)
    elif choice == 'manual':
        print(manual)
    elif choice == 'change prise':
        cp = (input('price of what product you want to change?'))
        cpr= int(input('type new price'))
        basket[cp]['price']=cpr
        print(basket)
    elif choice == 'change amount':
        cp = (input('amount of what product you want to change?'))
        cam= int(input('type new amount'))
        basket[cp]['amount']=cam
        print(basket)
    elif choice == "sum":
        suma = 0
        print("sum of all the products =")
        for product in list(basket.keys()):
            suma += basket[product]["totalp"]
        print(suma)