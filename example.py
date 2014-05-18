import pyak

yakker = pyak.Yakker()

ut = pyak.Location("35.943356", "-83.938699")

yakker.update_location(ut)

yaks = yakker.get_yaks()

for yak in yaks:
	yak.print_yak()
	print ""