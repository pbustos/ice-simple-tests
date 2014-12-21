# -*- coding: utf-8 -*-
"""
Created on Sun Dec 21 11:50:37 2014

@author: pbustos
"""

import sys, traceback, Ice, subprocess
import Arithmetic

icever = Ice.stringVersion()
print icever

subprocess.call(["slice2py", "arithmetic.ice"])

class NaturalI(Arithmetic.Natural):
    def add(self,a, b, current=None):
        return a + b
        
    def substract(self,a, b, current=None):
        if a<0 or b<0 or b>a:
            ex = Arithmetic.GenericError()
            ex.reason = "non natural argument or result"
            raise ex
        else:
            return a - b
        
status = 0
ic = None
try:
    ic = Ice.initialize(sys.argv)
    adapter = ic.createObjectAdapterWithEndpoints("ArithmeticAdapter", "default -p 10000")
    object = NaturalI()
    adapter.add(object, ic.stringToIdentity("Arithmetic"))
    adapter.activate()
    ic.waitForShutdown()
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