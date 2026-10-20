class InstaStory:
    def share(self):
        print("Sharing story")


class WhatsAppStory(InstaStory):
    def share(self):
        print("Sharing a status")


s1 = InstaStory()
s2 = WhatsAppStory()

s1.share()
s2.share()