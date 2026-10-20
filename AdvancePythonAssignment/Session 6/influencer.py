class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

class Influencer(User):
    def __init__(self, username, email, followers):
        super().__init__(username, email)
        self.followers = followers

influencer1 = Influencer("s4hil_patel_17kp", "sahilp1532@gmail.com", 5000)

print("Username:", influencer1.username)
print("Email:", influencer1.email)
print("Followers:", influencer1.followers)