# -*- coding: utf-8 -*-
"""
Created on Sun Dec 21 11:50:37 2014

@author: pbustos
"""

import sys, traceback, Ice
import Arithmetic

status = 0
ic = None
try:
    ic = Ice.initialize(sys.argv)
    base = ic.stringToProxy("Arithmetic:default -p 10000")
    natural = Arithmetic.NaturalPrx.checkedCast(base)
    if not natural:
        raise RuntimeError("Invalid proxy")

    if len(sys.argv) == 3:
        a = int(sys.argv[1])
        b = int(sys.argv[2])
        print "Calling server to substract", a, "-", b, "= ",natural.substract(a, b)

except:
    traceback.print_exc()
    status = 1

if ic:
    # Clean up
    try:
        ic.destroy()
    except:
        traceback.print_exc()
        status = 1

sys.exit(status)
