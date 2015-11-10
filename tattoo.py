#!/usr/bin/env python

import time

print "This demo will draw 10 dynamic cubes, one every second at the location in the world the hands are pointing. Ctrl-c will stop the demo if you want to quit early."
#print "\x1b!0|"
for y in range(0,10):
	print "\x1b!8;0.0;0.0;0.0;0.1;0.1;0.1|"
	time.sleep(1)

print "Done!"


