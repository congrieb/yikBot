import pyak
import time

class YikBot(pyak.Yakker):
    def boot(self):
        while True:
            print "DEBUG: Scanning feed"
            yaks = self.get_yaks()
            for yak in yaks:
                if yak.message.startswith("@yikBot"):
                    print "DEBUG: Found a targeted yak"
                    self.respond(yak)
            print "DEBUG: Going to sleep"
            time.sleep(10)

    def respond(self, yak):
        yak.add_comment("Hi, I'm yikBot")

    def multi_upvote(self, message, count):
        for i in range(0, count):
            yakker = pyak.Yakker()
            print "DEBUG: Registered new user with id %s" % yakker.id
            yakker.update_location(self.location)
            yakkers.append(yakker)

        print "DEBUG: Going to sleep"
        time.sleep(90)

        for yakker in yakkers:
            yaks = yakker.get_yaks()
            for yak in yaks:
                if yak.message == message:
                    yak.upvote()
                    print "DEBUG: Upvoted yak"
                    continue

    def multi_downvote(self, message, count):
        for i in range(0, count):
            yakker = pyak.Yakker()
            print "DEBUG: Registered new user with id %s" % yakker.id
            yakker.update_location(self.location)
            yakkers.append(yakker)

        print "DEBUG: Going to sleep"
        time.sleep(90)

        for yakker in yakkers:
            yaks = yakker.get_yaks()
            for yak in yaks:
                if yak.message == message:
                    yak.downvote()
                    print "DEBUG: Downvoted yak"
                    continue