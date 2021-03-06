import pyak
import time
from multiprocessing import Process

def threaded_scan(pattern1, pattern2, location):
	#yakker = pyak.Yakker()
	#yakker.update_location(location)
	print "created a new yakker on a new thread ", "yakker"
	time.sleep(90)
	print "waking yakker ", "yakker", " back up"
	#yakker.single_scan(pattern1, pattern2)

class YikBot(pyak.Yakker):
    yakkers = []

    def boot(self):
        while True:
            print "DEBUG: Scanning feed"
            yaks = self.get_yaks()
            for yak in yaks:
                if yak.message.startswith("@yikBot"):
                    print "DEBUG: Found a targeted yak"
                    self.respond(yak)
            print "DEBUG: Going to sleep, will repeat in 10 seconds"
            time.sleep(10)

    def multi_scan(self, pattern1, pattern2):
        while True:
            print "DEBUG: Scanning All yaks for"
            print pattern
            for user in self.yakkers:
	        yaks = user.get_yaks()
                for yak in yaks:	
                    if yak.message.find(pattern1) != -1 or yak.message.find(pattern2) != -1:
                        print "Found Yak containing target pattern"
                        yak.upvote()
                print "DEBUG: Sleeping for 2 seconds and scanning again"
                time.sleep(2)

    def single_scan(self, pattern1, pattern2):
        while True:
            print "DEBUG: Yakker ", self
            print "DEBUG: Scanning All yaks for ", pattern1, " or " , pattern2
	    yaks = self.get_yaks()
            for yak in yaks:	
                if yak.message.find(pattern1) != -1 or yak.message.find(pattern2) != -1:
                    print "Found Yak containing target pattern"
                    yak.upvote()
                print "DEBUG: Sleeping for 2 seconds and scanning again"
                time.sleep(2)                   

    def respond(self, yak):
        yak.add_comment("Hi, I'm yikBot")

    def multi_upvote(self, message, count):
        yakkers = []
        for i in range(0, count):
            yakker = pyak.Yakker()
            print "DEBUG: Registered new user with id %s" % yakker.id
            yakker.update_location(self.location)
            yakkers.append(yakker)

        print "DEBUG: Going to sleep, new yakkers must wait ~90 seconds before they can act"
        time.sleep(90)
        print "DEBUG: Waking up and beginning scan"

        for yakker in yakkers:
            print "DEBUG: yakker %s now scanning"
            yaks = yakker.get_yaks()
            for yak in yaks:
                if yak.message == message:
                    yak.upvote()
                    print "DEBUG: Upvoted yak"
                    break


    def multi_downvote(self, message, count):
        yakkers = []
        for i in range(0, count):
            yakker = pyak.Yakker()
            print "DEBUG: Registered new user with id %s" % yakker.id
            yakker.update_location(self.location)
            yakkers.append(yakker)

        print "DEBUG: Going to sleep, new yakkers must wait ~90 seconds before they can act"
        time.sleep(90)
        print "DEBUG: Waking up and beginning scan"

        for yakker in yakkers:
            print "DEBUG: yakker %s now scanning"
            yaks = yakker.get_yaks()
            for yak in yaks:
                if yak.message == message:
                    yak.downvote()
                    print "DEBUG: Downvoted yak"
                    break

    def create_yakkers(self, count):
        for i in range(0, count):
            yakker = pyak.Yakker()
            print "DEBUG: Registered new user with id %s" % yakker.id
            yakker.update_location(self.location)
            self.yakkers.append(yakker)

    def create_and_scan(self, count, pattern1, pattern2):
        for i in range(0, count):
            p = Process(target = threaded_scan, args = (pattern1, pattern2, self.location))
            p.start()

    def clear_yakkers(self):
        self.yakkers = []
