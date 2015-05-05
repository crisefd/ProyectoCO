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
		self.N = input_['N']
		self.V = input_['V']
		self.P = float(input_['P'])
		self.v = input_['v']
		self.p = input_['p']
		self.v_acum = 0
		self.p_acum = 0
		self.C = [0] * self.N

	def add_constraints(self):
		lp.addConstraint({"Q" : 1, } ,"<=", 1)
		lp.addConstraint({"C" : 1, } ,"<=", 1)
		lp.setBinary(0)
		lp.setBinary(1)		

		coeffs = self.p[:]
		#for i in range(0, self.N):
		#	lp.addConstraint(coeffs, "<=", )



s = Solver()
s.initialize("/home/crisefd/Documentos/Python/prueba.txt")
s.add_constraints()