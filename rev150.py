from z3 import *

s = []
for i in range(20):
	
	s.append(Int('s['+str(i)+']')) # define the variables of the password


solver = Solver()
#all password values are digits between 0 and 9
for i in range(20):
	solver.add(s[i]>=0)
	solver.add(s[i]<10)

# add all confiditions
solver.add(s[15] + s[4] == 10)
solver.add(s[1] * s[18] == 2 )
solver.add(s[15] / s[9] == 1)
solver.add(s[17] - s[0] == 4)
solver.add(s[5] - s[17] == -1)
solver.add(s[15] - s[1] == 5)
solver.add(s[1] * s[10] == 18)
solver.add(s[8] + s[13] == 14)
solver.add(s[18] * s[8] == 5)
solver.add(s[4] * s[11] == 0)
solver.add(s[8] + s[9] == 12)
solver.add(s[12] - s[19] == 1)
solver.add(s[9] % s[17] == 7)
solver.add(s[14] * s[16] == 40)
solver.add(s[7] - s[4] == 1)
solver.add(s[6] + s[0] == 6)
solver.add(s[2] - s[16] == 0)
solver.add(s[4] - s[6] == 1)
solver.add(s[0] % s[5] == 4)
solver.add(s[5] * s[11] == 0)
solver.add(s[10] % s[15] == 2)
solver.add(s[11] / s[3] == 0)
solver.add(s[14] - s[13] == -4)
solver.add(s[18] + s[19] == 3)
#don't forget about s[3]!=0 because 's[11] / s[3]' we can't devide by zero
solver.add(s[3]!=0)
if (solver.check() == sat):
	print solver.model()


#easy no !

	

