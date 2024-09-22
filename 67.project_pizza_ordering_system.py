pizza_sizes = {
    "small": 5,
    "medium": 7,
    "large": 9 
    }


toppings = {
    "cheese": 1,
    "pepperoni": 2,
    "mushrooms": 3,
    "olives": 4,
    "onions": 5,
    "bacon": 6
}


choose_pizza_sizes = input("pizza boyutunu girin: ").lower()
choose_toppings = input("malzeme seçimi yapin: ").lower()


if choose_pizza_sizes in pizza_sizes:
    pizza_price = pizza_sizes[choose_pizza_sizes]
else:
    print("Invalid pizza size!")    
    pizza_price = 0

if choose_toppings in toppings:
    toppings_price = toppings[choose_toppings]
else:
    print("Invalid topings")    
    toppings_price = 0


total_price = pizza_price + toppings_price

print(f"Total amount due: {total_price} $")