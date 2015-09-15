
from __future__ import print_function
from sandbox import Sandbox

s=Sandbox()
string ="""
from __future__ import print_function
import math
x= math.factorial(20)
print (x)


"""
s.execute(string)
