def update_cart(cart, item, qty):
    cart[item] = qty
    return cart


cart= {
    "Mobile": 1,
    "Headphones": 2
}

cart=update_cart(cart, "Laptop", 1)

print(cart)