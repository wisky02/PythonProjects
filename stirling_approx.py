#checks the size of the terms in stirlings approximation

from math import log, pi
import numpy

def comp_func(N):
	first = N*log(N)
	second = -1*N
	third = .5*log(N)
	fourth = .5*log(2*pi) 
	out = [first, second, third, fourth]
	return(out)	

number = raw_input("value to be compared: ") #raw_input produces the arg as a str.
print("You selected: {}".format(number))
N = float(number)
compare = comp_func(N)
print_list = ["NlogN = ", "-N = ", "0.5lnN = ", "0.5ln(2pi)"]
for x in range(len(compare)):
	print print_list[x] ,compare[x]
	
