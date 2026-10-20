class InvalidCouponCodeError(Exception):
    pass


coupon_code = input("Enter coupon code: ")

try:
    if coupon_code != "FOOD10":
        raise InvalidCouponCodeError("Invalid coupon code")

    print("Coupon applied successfully")

except InvalidCouponCodeError as e:
    print(e)