from os.path import exists

def copyf(copy_file):
    print "Enter the dstination file name."
    copy_file  = raw_input()    
    print " file exists %r" % exists(copy_file)
    output = open(copy_file, 'w')
    print "This file will be erased and all data in it will be lost.Ready?"
    raw_input()
    copy_file.truncate()
    print "Hit Enter to continue the copy."
    raw_input()
    output.write()