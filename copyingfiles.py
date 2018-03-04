""" asdas"""

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print("copying from %s to %s" % (from_file, to_file))

rinput = open(from_file)
indata = rinput.read()

print("the input file is %s bytes long." % len(indata))

print("does the out file exis? %r" % exists(to_file))
print("ready? hit enter to continue and ctrl+c to exit.")
input()

routput = open(to_file, 'w')
routput.write(indata)

print("DONE!")

routput.close()
rinput.close()
