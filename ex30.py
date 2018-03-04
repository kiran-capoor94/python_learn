print " You enter a drak room with two doors. Do yoou go through door  1 or door 2?"

door = raw_input(">  ")

if door == "1":
    print " There's a giant bear here wating a cheese cake. What do you do?"
    print " 1. Take the cake"
    print " 2. Scream at the bear"

    bear = raw_input("> ")

    if bear == "1":
        print "The bear eats your face off. Good Job!"
    elif bear == "2":
        print "The bear eats your legs off. Good Job!"
    else:
        print "Well done, %s is probably better. Bear runs away." % bear

elif door == "2":
    print "You stare into the endless abyss at Cthulu's retina."
    print "1. Blueberries"
    print "2. Yellow jacket clothespins."
    print "3. Understanding revolvers yelling meoldies"

    insanity = raw_input("> ")

    if insanity == "1" or insanity == "2":
        print "Your body survives powered by a mind of jello."
    else:
        print " The insanity rots your eyes into a pool of muck. Great!"
else:
    print " You stumble around and fall on a knife and die. Good job!"