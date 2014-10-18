import pyak
import time

#This registers a new user. 
#In practice, you will want to save and re-use a single user ID.
#The constructor can be called with an optional astring argument for user ID.

# Latitude and Longitude of location where bot should be localized
yLocation = pyak.Location("42.270340", "-83.742224")

yikBot = pyak.Yakker()
yikBot.handle = "yikBot"
print "DEBUG: Registered yikBot with handle %s and id %s" % (yikBot.handle, yikBot.id)
yikBot.update_location(yLocation)

print "DEBUG: yikBot instance immediately after initialization"
print vars(yikBot)

# time.sleep(90)

# print "DEBUG: yikBot instance 90 seconds after initialization"
# print vars(yikBot)

# yakkers = []

# for i in range(0, 10):
#     yakker = pyak.Yakker()
#     print "DEBUG: Registered new user with id %s" % yakker.id
#     yakker.update_location(yLocation)
#     yakkers.append(yakker)

time.sleep(90)

yikBot.post_yak("yikBot test", False, True)

time.sleep(10)

yaks = yikBot.get_yaks()
for yak in yaks:
    # yak.print_yak()
    # comments = yak.get_comments()
    # for comment in comments:
        # print "    %s" % comment.comment
    # print ""

    if yak.message == "yikBot test":
        print "DEBUG: Found the test yak"
        yak.add_comment("yikBot will scan this Yik Yak feed and respond when it is mentioned")
        break

while True:
    print "DEBUG: Scanning feed"
    yaks = yikBot.get_yaks()
    for yak in yaks:
        if yak.message.startswith("@yikBot"):
            print "DEBUG: Found a targeted yak"
            yak.add_comment("Hi, I'm yikBot")
    print "DEBUG: Going to sleep"
    time.sleep(10)



# yaks = yikBot.get_yaks()
# print yaks;
# for yak in yaks:
#   print yak.message

# for yakker in yakkers:
#     print "Attempting to post yak"
#     yakker.post_yak("Strong Bad")

#     yaks = yakker.get_yaks()

#     for yak in yaks:
#         if yak.message == "Test yak":
#             yak.upvote()
#             print "Upvoted your yak"
#         print yak
#     	yak.print_yak()
#     	comments = yak.get_comments()
#     	for comment in comments:
#     		print "    %s" % comment.comment
#     	print ""
