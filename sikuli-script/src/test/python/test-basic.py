from __future__ import with_statement
from sikuli.Sikuli import *


if Key.ENTER: print "Key exists"

r = Region(0,0,100,100)
if r: print "Region exists"

s = Screen()
if s: print "Screen exists"

if getBounds(): print "global functions exposed"

v = VDict()
v["test-res/apple.png"]="apple"
if v["test-res/apple.png"][0] == "apple": 
   print "VDict works"
