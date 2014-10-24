import pyak
import time
import yikbot

#bots location
yLocation = pyak.Location("42.270340", "-83.742224")


yb = yikbot.YikBot()

yb.update_location(yLocation)

yb.handle = "William Taft"

print "Bot created and location set, now sleeping for 90 seconds"

