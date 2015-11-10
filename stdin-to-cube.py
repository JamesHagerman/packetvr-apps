#!/usr/bin/env python
import sys
# for line in sys.stdin:
#     print "."

buff = ''
# while True:
#     buff += sys.stdin.read(1)
#     if buff.endswith('\n'):
#         print buff[:-1]
#         buff = ''


print "This script will place one cube in the world for every character received from standard input"
print "Pipe shell commands and application to this script to display data in VR"

while True:
    buf = sys.stdin.read(1)
    print "Buf: {}".format(buf)
    print "\x1b!1;0.0;0.0;-1.2;0.1;0.1;0.1|"
