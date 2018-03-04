from sys import argv

Script, Filename = argv

Txt = open(Filename)

print "Here's your file %r" % Filename
print Txt.read()

print "I'll also ask you to type it again;"
File_again = raw_input(">")

Txt_again = open(File_again)

print Txt_again.read()

print "closing file now"

Txt.close()
Txt_again.close()