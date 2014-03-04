#figuring out sets
from sets import Set

oldie = [ "bloop","blahp","bleep","burp"]

newbie = [ "bloop","insert","bleep","blahp","dog"]

oldSet = Set(oldie)
newSet = Set(newbie)

raw_input("It set!")

print newSet - oldSet

for x in newSet-oldSet:
	print x


raw_input("It ran!")