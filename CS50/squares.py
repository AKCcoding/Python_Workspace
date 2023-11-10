""" 
if functions module been called will import all of the methods in it
import functions

for i in range(10):
     print (f"The square of {i} is {functions.square(i)}")

or you can invoke like this
"""

from functions import square

for i in range(10):
     print (f"The square of {i} is {square(i)}")

