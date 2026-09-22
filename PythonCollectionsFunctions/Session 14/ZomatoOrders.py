orders = {}

def add_order(order_id, restaurant, item, total):
    orders[order_id] = {
        "restaurant": restaurant,
        "items": [item],
        "total": total
    }


def update_total(order_id, amount):
    orders.setdefault(order_id, {"total": 0})
    orders[order_id]["total"] += amount


add_order(101, "Pizza Point", "Pizza", 500)
update_total(101, 200)

print(orders)