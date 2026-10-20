class Influencer:
    def __init__(self, username, followers):
        self.username = username
        self.followers = followers

class Brand:
    def __init__(self, brand_name):
        self.brand_name = brand_name

class BrandPartner(Influencer, Brand):
    def __init__(self, username, followers, brand_name):
        Influencer.__init__(self, username, followers)
        Brand.__init__(self, brand_name)

partner1 = BrandPartner("krupipatel", 1000, "Nike")

print("Username:", partner1.username)
print("Followers:", partner1.followers)
print("Brand Name:", partner1.brand_name)