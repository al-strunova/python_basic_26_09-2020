nbr_products = int(input("Please enter the number of products to be added to the system: "))
entries = []
for i in range(nbr_products):
    name = input(f"What's the name of the #{i + 1} product: ")
    price = int(input(f"What's the price of the #{i + 1} product: "))
    total = int(input(f"How many items of the #{i + 1} product: "))
    entries.append(tuple([i + 1, {"name": name, "price": price, "total": total}]))
    print(f"#{i + 1} product was added this the following characteristics: {entries[i]}")
dic_products = {"name": [], "price": [], "total": []}
for entry in entries:
    dic_products["name"].append(entry[1]["name"])
    dic_products["price"].append(entry[1]["price"])
    dic_products["total"].append(entry[1]["total"])
print(dic_products)
