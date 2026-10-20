class Payment:
    def pay(self, amount):
        print("Paying", amount)


class UPI(Payment):
    def pay(self, amount):
        print("Paying", amount, "via UPI")


p1 = Payment()
p2 = UPI()

p1.pay(500)
p2.pay(500)