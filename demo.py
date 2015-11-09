#!/usr/bin/env python

import time

print "This demo will build 4 stacks of 40 cubes in the scene. Watch out!"
#print "\x1b!0|"
for x in range(0,1):
	for y in range(0,40):
		print "\x1b!1;{}.0;{}.0;-1.2;0.1;0.1;0.1|".format(x,y)	

print "Done."


