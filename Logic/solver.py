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
		#print input_
		self.N = input_['N']
		self.V = input_['V']
		self.P = float(input_['P'])
		self.v = input_['v']
		self.p = input_['p']
		self.v_acum = 0
		self.p_acum = 0
		self.C = [0] * self.N

	def solve_(self):
		self._add_constraints()
		self._set_objective()
		lp.solve()
		return lp.getSolution()

	def _add_constraints(self):

		coeff_p = self.p[:]
		coeff_p.append(self.P * -1)
		coeff_v = self.v[:]
		coeff_v.append(self.V * -1)
		coeffs = [1] * self.N
		coeffs.append(-1)
		for i in range(0, self.N):
			lp.addConstraint(coeff_p, "<=", 0)
			lp.addConstraint(coeff_v, "<=", 0)

		lp.addConstraint(coeffs, "=", 0)

		print lp.get_column(1)

		for i in range(1, self.N ):
			lp.setBinary(i)

	def _set_objective(self):
		coeffs = [1] * self.N
		lp.setObjective(coeffs, mode="minimize")



		

s = Solver()
s.initialize("/home/crisefd/Documentos/Python/prueba.txt")
print s.solve_()
