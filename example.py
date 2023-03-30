#DEADCODE move to examples

from interface import *

assumptions = [
    "(Believes! a P)", 
    "(Believes! a Q)" ]


goal = "(Believes! a (and P Q))"

print(prove(assumptions, goal))
