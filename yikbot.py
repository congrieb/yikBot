import pyak
import time

#This registers a new user. 
#In practice, you will want to save and re-use a single user ID.
#The constructor can be called with an optional astring argument for user ID.

yakkers = []

for i in range(0, 10):
    yakker = pyak.Yakker()
    print "Registered new user with id %s" % yakker.id
    ut = pyak.Location("42.270340", "-83.742224")
    yakker.update_location(ut)
    yakkers.append(yakker)

time.sleep(90)

for yakker in yakkers:
    # print "Attempting to post yak"
    # yakker.post_yak("Strong Bad")

    yaks = yakker.get_yaks()

    for yak in yaks:
        if yak.message == "1-3x4+7=?":
            yak.upvote()
            print "Upvoted your yak"
    	# yak.print_yak()
    	# comments = yak.get_comments()
    	# for comment in comments:
    		# print "    %s" % comment.comment
    	# print ""
