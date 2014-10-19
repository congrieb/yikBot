import pyak
import time

class YikBot(Yakker):
    def boot(self):
        while True:
            print "DEBUG: Scanning feed"
            yaks = yikBot.get_yaks()
            for yak in yaks:
                if yak.message.startswith("@yikBot"):
                    yikBot.respond(yak)
            print "DEBUG: Going to sleep"
            time.sleep(10)

    def respond(self, yak):
        print "DEBUG: Found a targeted yak"
        yak.add_comment("Hi, I'm yikBot")
