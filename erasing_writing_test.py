from sys import argv

script, filename = argv

print "earse %r" % filename
print "are you sure? press Ctrl+C to cancel"
print "press enter to confirm."

raw_input("?")

print "opening the file..."
target = open(filename, 'w')

print "truncating the file"
target.truncate()

print "Enter the data you want to enter"
line1 = raw_input("line 1: " )
line2 = raw_input("line 2: " )
line3 = raw_input("line 3: " )
total = line1 +'\n' + line2 +'\n' + line3

print "writing.."

target.write(total)

print "closing.."
target.close()