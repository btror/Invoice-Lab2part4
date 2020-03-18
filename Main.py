from Invoice import Invoice

products = {}
total_amount = 0
repeat = ''
# new variable to keep track of amount of items
# item_count = 0

while True:
    # product = input("What is your product : ")
    product = Invoice().inputName("What is your product: ")
    unit_price = Invoice().inputNumber("Please enter unit price : ")
    qnt = Invoice().inputNumber("Please enter quantity of product : ")
    discount = Invoice().inputNumber("Discount percent (%) : ")
    repeat = Invoice().inputAnswer("Another product? (y,n) : ")
    result = Invoice().addProduct(qnt, unit_price, discount, product)
    products[product] = result
    if repeat == "n":
        break;

total_amount = Invoice().totalPurePrice(products)
print("Your total pure price is: ", total_amount)

# print the total amount of items
names = Invoice().allNames(products)
print("Types of items purchased: ", names)
