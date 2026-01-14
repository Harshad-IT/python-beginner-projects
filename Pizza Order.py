def pizza_order(name, *toppings, **details):
    print("------------------ 📃 Order Summary 📃 -----------------------")
    print("Customer: ", name)
    print("Toppings: ", ", ".join(toppings))
    for key, value in details.items():
        print(f"{key}: {value}")
    print("🍕 Thank you for ordering from PYTHON PIZZA 🍕")

def print_bill(name, toppings, details):
    print("-" * 35)
    print("     PYTHON PIZZA 🍕")
    print("-" * 35)
    print(f"Customer: {customer}")
    print(f"Size    : {details['Size']}")
    print("-"*35)
    print(f"{'Base Price':20} {details['Base Price']}")
    print("Toppings: ")
    if toppings:
        for t in toppings:
            print(f" - {t}")
    else:
        print("     No Extra Toppings")

    print(f"{'Toppings Cost':20} {details['Toppings Cost']}")
    print("-" * 35)
    print(f"{'Total':20} {details['Total Price']}")
    print("-" * 35)

    print("Thank you for Orderings! 😊")
    print("-" * 35)



print("--------------- 🍕  WELCOME TO PYTHON PIZZA  🍕--------------------")
customer = input("Enter your name: ")
print("Hello!", customer, "😊")
tops_list = []
print("--------------- 👉 Enter your toppings 👈 ----------------")
print("                Type 'done' when finished 👍       ")
while True:
    toppings = input("Enter toppings: ")
    if toppings.lower() == "done":
        break
    tops_list.append(toppings)

details_dict = {}
print("--------------- 👉 Select Pizza Size 👈 ----------------")
print("1. Small\n2. Medium\n3. Large")
size_choice = input("Choose (1/2/3): ")
if size_choice == "1":
    details_dict["Size"] = "Small"
elif size_choice == "2":
    details_dict["Size"] = "Medium"
elif size_choice == "3":
    details_dict["Size"] = "Large"
else:
    details_dict["Size"] = "Unknown"
print("--------------- 👉 Select Method of Payment 👈 ----------------")
print("1. Cash\n2. UPI\n3. Card")
payment_choice = input("Choose (1/2/3): ")

if payment_choice == "1":
    details_dict["Payment"] = "Cash"
elif payment_choice == "2":
    details_dict["Payment"] = "UPI"
elif payment_choice == "3":
    details_dict["Payment"] = "Card"
else:
    details_dict["Payment"] = "Not Selected"

delivery = input("Home Delivery? (yes/no): ").lower()
details_dict["delivery"] = "yes" if delivery == "yes" else "no"

size_prices = {
    "Small": 199,
    "Medium": 299,
    "Large": 399
}

topping_price = 40
Selected_size = details_dict["Size"].strip().capitalize()
base_price = size_prices.get(Selected_size, 0)
toppings_cost = len(tops_list) * topping_price
total_price = base_price + toppings_cost

details_dict["Base Price"] = f"₹ {base_price}"
details_dict["Toppings Cost"] = f"₹ {toppings_cost}"
details_dict["Total Price"] = f"₹ {total_price}"

print("-"*35)
print_bill(customer, tops_list, details_dict)
