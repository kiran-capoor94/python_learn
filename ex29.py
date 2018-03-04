print "enter no of people"
people =raw_input()
print "no of cats"
cats = raw_input()
print "no of dogs"
dogs = raw_input()

if people < cats:
    print "Too many cats."

if people > cats:
    print "Not many cats"

if people < dogs:
    print "drool!"

if people > dogs:
    print "dry!!"