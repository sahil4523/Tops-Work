class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

class Influencer(User):
    def __init__(self, username, email, followers):
        super().__init__(username, email)
        self.followers = followers

class VerifiedInfluencer(Influencer):
    def __init__(self, username, email, followers, badge):
        super().__init__(username, email, followers)
        self.badge = badge

    def display_profile(self):
        if self.followers >= 1000:
            count = str(round(self.followers/1000, 1)) + "K"
        else:
            count = str(self.followers)

        print("Username:", self.username)
        print("Email:", self.email)
        print("Followers:", count)
        print("Badge:", self.badge)

user1 = VerifiedInfluencer("s4hil_patel", "sahil@gmail.com", 1500, "Verified")
user1.display_profile()