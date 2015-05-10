import sys
import imp
import os
from pylpsolve import LP
from numpy import *


lp = LP()
fileReader = None
try:
	path = os.path.abspath(os.path.dirname(__file__) + '/' + '.././Input/fileReader.py')
	#print ">>>", path
	fileReader = imp.load_source("fileReader", path)
except IOError as err:
	print err
	path = os.path.abspath(os.path.dirname(__file__)  + '.././Input/fileReader.py')
	#print ")))", path
	fileReader = imp.load_source("fileReader", path)

class Solver():
	def initialize(self, path_to_input):
		input_ = fileReader.FileReader.read_input(path_to_input)
		print input_
		self.N = int(input_['N'])
		self.V = float(input_['V'])
		self.P = float(input_['P'])
		self.v = map(float, input_['v'])
		self.p = map(float, input_['p'])
		self.v_acum = 0
		self.p_acum = 0
		self.C = [0] * self.N

	def solve_(self):
		self._add_constraints()
		r = self._set_objective()
		lp.solve()
		print "=========================================="
		print "Solution: ", lp.getSolution()
		print "Solucion with indices: ", lp.getSolution(r)
		print "Solution value: ", lp.getObjectiveValue()
		print "Info: ", lp.getInfo('Iterations')

	def _add_constraints(self):

		coeff_p = self.p[:]
		coeff_p.append(self.P * -1)
		coeff_v = self.v[:]
		coeff_v.append(self.V * -1)
		coeff_vp = []
		for i in range(0, self.N + 1):
			coeff_vp.append(coeff_v[i] + coeff_p[i])

		coeffs = [1] * (self.N )
		coeffs.append(-1)
		
		L = self.N * self.N + self.N
		indices = [i for i in range(0, L)]
		rhs = [0 for i in range(0, self.N)]
		coefficients = []
		k = 0
		for i in range(0, self.N):
			n = 0
			#print "i=",i
			tuple_ = [0] * L
			if i==0:
				x = k
				y = (i + 1) * (self.N + 1)
				k = k + self.N 
			else:
				x = k + 1
				y = (i+1) * (self.N + 1)
				k = k + self.N + 1
			#print "x=", x
			#print "y=", y
			for j in range(x, y):
				#print "j=",j,"n=",n
				try:
					tuple_[j] = coeff_vp[n]
				except IndexError:
					print "Error j=",j,"n=", n
				n += 1
			coefficients.append(tuple_)
			

		#for i in range(0, self.N):
		#	coefficients.append(coeff_vp)
		
		print "\n indices ", indices
		print "Constraints coeffs", coefficients
		print "rhs ", rhs
		lp.addConstraint((indices, coefficients), "<=", rhs)
		for p in range(0, self.N):
			c = [0] * L
			z = p
			while z < L:
				c[z] = 1
				z += self.N + 1
			print "Last constraint coeffs ", c
			lp.addConstraint(c, "=", 1)

		#print "Last constraint coeffs ", c
		
		lp.setBinary(indices)
		#for i in range(0, L):
		#	lp.setBinary(i)

	def _set_objective(self):
		L = self.N * self.N + self.N
		k = self.N
		r = []
		coeffs = [0] * L
		while k < L:
			r.append(k)
			coeffs[k] = 1
			k += self.N + 1

		print "objective coeffs ", coeffs

		lp.setObjective(coeffs, mode="minimize")
		return r
		




		

s = Solver()
s.initialize("/home/crisefd/Documentos/Python/prueba.txt")
#print "Solution ", 
s.solve_()
