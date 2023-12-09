# pip install numpy matplotlib
# https://www.geeksforgeeks.org/random-walk-implementation-python/
# Python code for 2D random walk.
import numpy
import pylab
import random

# defining the number of steps
n = int(input("Enter the number of steps: "))

#creating two array for containing x and y coordinate
#of size equals to the number of size and filled up with 0's
x = numpy.zeros(n)
y = numpy.zeros(n)

# filling the coordinates with random variables
for i in range(1, n):
	val = random.randint(1, 4)
	if val == 1:
		x[i] = x[i - 1] + 1
		y[i] = y[i - 1]
	elif val == 2:
		x[i] = x[i - 1] - 1
		y[i] = y[i - 1]
	elif val == 3:
		x[i] = x[i - 1]
		y[i] = y[i - 1] + 1
	else:
		x[i] = x[i - 1]
		y[i] = y[i - 1] - 1
	

# plotting stuff:
pylab.title("Random Walk ($n = " + str(n) + "$ steps)")
pylab.plot(x, y)
pylab.show()

# If you want to save the figure, uncomment the line below.
# pylab.savefig("rand_walk"+str(n)+".png",bbox_inches="tight",dpi=1000)