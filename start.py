import pyak
import yikbot
import time

# Latitude and Longitude of location where bot should be localized
yLocation = pyak.Location("42.270340", "-83.742224")

yb = yikbot.YikBot()
yb.handle = "yikBot"
yb.update_location(yLocation)
print "DEBUG: Registered yikBot with handle %s and id %s" % (yb.handle, yb.id)

time.sleep(90)

print "DEBUG: yikBot instance 90 seconds after initialization"
print vars(yb)

yb.boot()