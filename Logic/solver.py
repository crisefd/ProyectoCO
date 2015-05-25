import sys
import imp
import os
from pylpsolve import LP
from numpy import *
from abc import ABCMeta, abstractmethod

lp = None
fileReader = None
try:
	path = os.path.abspath(os.path.dirname(__file__) + '/' + '.././Input/fileReader.py')
	fileReader = imp.load_source("fileReader", path)
except IOError as err:
	print err
	path = os.path.abspath(os.path.dirname(__file__)  + '.././Input/fileReader.py')
	fileReader = imp.load_source("fileReader", path)

class Solver():
    __metaclass__ = ABCMeta
    @abstractmethod
    def initialize(self):pass

    @abstractmethod
    def solve(self):pass

    @abstractmethod
    def _add_constraints(self):pass

    @abstractmethod
    def _set_objective(self):pass

class Solver1(Solver):
	def initialize(self, path_to_input):
		global lp
		lp = LP()
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

	def solve(self):
		global lp
		self._add_constraints()
		r = self._set_objective()
		lp.solve()
		sol = lp.getSolution()
		#print ("=========>", len(sol))
		#sol_matrix = []
		msg = ""
		k = 0
		p = self.N
		for i in range(0, self.N):
			#print "k=",k," p=",p
			msg += "knapsack " + str(i) + " boxes: "
			row = sol[k:p]
			for j in range(0, len(row)):
				if row[j] == 1:
					msg += str(j) + ", "

			print row
			msg += "\n"
			#sol_matrix.append(row)
			k += self.N +1
			p += self.N +1
		#solution = ''.join(str(e) + "," for e in sol)
		indices_solution = ''.join(str(e)+ ", " for e in lp.getSolution(r))
		solution_value = str(lp.getObjectiveValue())
		iterations = str(lp.getInfo('Iterations'))
		output = {'msg':msg,'indices_solution':indices_solution,
					'solution_value':solution_value,'Iterations':iterations}
		#print "=========================================="
		#print "Solution: ", lp.getSolution()
		#print "Solucion with indices: ", lp.getSolution(r)
		#print "Solution value: ", lp.getObjectiveValue()
		#print "Info: ", lp.getInfo('Iterations')
		lp = None
		return output




	def _add_constraints(self):
		global lp
		#Copying weights and volumes
		coeff_p = self.p[:]
		coeff_p.append(self.P * -1)
		coeff_v = self.v[:]
		coeff_v.append(self.V * -1)
		coeff_vp = []
		#Adding volumes and weights 
		for i in range(0, self.N + 1):
			coeff_vp.append(coeff_v[i] + coeff_p[i])
		#coeffs = [1] * (self.N )
		#coeffs.append(-1)
		#Setting the amount of the variables in the matrix
		L = self.N * self.N + self.N
		#Setting the indices of the variables in the matrix
		indices = [i for i in range(0, L)]
		#Setting the right hand side constants of the equations
		rhs = [0 for i in range(0, self.N)]
		#Initilizing the coefficients  as an empty list
		coefficients = []
		k = 0
		for i in range(0, self.N):
			n = 0
			#Initializing a coefficient row to zeros
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
			#Inserting v + p values in the row 
			for j in range(x, y):
				#print "j=",j,"n=",n
				try:
					tuple_[j] = coeff_vp[n]
				except IndexError:
					print "Error j=",j,"n=", n
				n += 1
			#Appending new row to the coefficients
			coefficients.append(tuple_)
		#print "\n indices ", indices
		#print "Constraints coeffs", coefficients
		#print "rhs ", rhs
		#Adding constraints a) and b) to the matrix
		lp.addConstraint((indices, coefficients), "<=", rhs)
		#Adding constraint c) to the matrix
		for p in range(0, self.N):
			c = [0] * L
			z = p
			while z < L:
				c[z] = 1
				z += self.N + 1
			#print "Last constraint coeffs ", c
			lp.addConstraint(c, "=", 1)
		#Setting all variables for the a) and b) constraints as binary variables
		lp.setBinary(indices)

	def _set_objective(self):
		global lp
		L = self.N * self.N + self.N
		k = self.N
		r = []
		coeffs = [0] * L
		while k < L:
			r.append(k)
			coeffs[k] = 1
			k += self.N + 1
		#print "objective coeffs ", coeffs
		lp.setObjective(coeffs, mode="minimize")
		return r
		
class Solver2(Solver):
	def initialize(self, M, p, v, P, V):
		global lp
		lp = LP()
		self.M = M
		self.p = p
		self.v = v
		self.P = P
		self.V = V

	def solve(self):
		global lp
		L = self.M * self.M + 2
		print "L=", L
		self._add_constraints()
		self._set_objective()
		lp.solve()
		sol = lp.getSolution()
		#print ("=========>", len(sol))
		#sol_matrix = []
		msg = ""
		k = 0
		p = self.M
		for i in range(0, self.M):
			#print "k=",k," p=",p
			msg += "knapsack " + str(i) + " boxes: "
			row = sol[k:p]
			for j in range(0, len(row)):
				if row[j] == 1:
					msg += str(j) + ", "

			print row
			msg += "\n"
			#sol_matrix.append(row)
			k += self.M + 1
			p += self.M + 1
		#solution = ''.join(str(e) + "," for e in sol)
		indices_solution = ''.join(str(e)+ ", " for e in lp.getSolution([L - 2, L - 1]))
		solution_value = str(lp.getObjectiveValue())
		iterations = str(lp.getInfo('Iterations'))
		output = {'msg':msg,'indices_solution':indices_solution,
					'solution_value':solution_value,'Iterations':iterations}
		#print "=========================================="
		#print "Solution: ", lp.getSolution()
		#print "Solucion with indices: ", lp.getSolution(r)
		#print "Solution value: ", lp.getObjectiveValue()
		#print "Info: ", lp.getInfo('Iterations')
		lp = None
		return output

	def _add_constraints(self):
		global lp
		#Copying weights and volumes
		coeff_p = self.p[:]
		#coeff_p.append(self.P * -1)
		coeff_v = self.v[:]
		#coeff_v.append(self.V * -1)
		#Setting the amount of the variables in the matrix
		L = self.M * self.M + 2
		indices = [i for i in range(0, L)]
		lp.setBinary(indices)
		print "Indices=", indices
		#rhs = [0] * (2*self.M)
		#print "rhs=", rhs
		#for index in range(0, self.M):
		#	rhs[index] = self.P
		#for index in range(self.M, 2*self.M):
		#	rhs[index] = self.V

		print "==========Restriccion a)"
		coefficients = []
		k = 0
		for i in range(0, self.M):
			n = 0
			tuple_ = [0] * L
			if i==0:
				x = k
				y = (i + 1) * (self.M)
				k = k + self.M 
			else:
				x = k #<--------------------------------------
				y = (i + 1) * (self.M)
				k = k + self.M #<-------------------------------
			print "x=", x
			print "y=", y
			for j in range(x, y):
				try:
					tuple_[j] = coeff_p[n]
				except IndexError:
					print "Error j=",j,"n=", n
				n += 1
			coefficients.append(tuple_)
		print "coefficients=", coefficients
		lp.addConstraint((indices, coefficients), "<=", [self.P for i in range(0, self.M)])


		print "==========Restriccion b)"
		coefficients = []
		k = 0
		for i in range(0, self.M):
			n = 0
			tuple_ = [0] * L
			if i==0:
				x = k
				y = (i + 1) * (self.M)
				k = k + self.M 
			else:
				x = k #<--------------------------------------
				y = (i + 1) * (self.M)
				k = k + self.M #<-------------------------------
			print "x=", x
			print "y=", y
			for j in range(x, y):
				try:
					tuple_[j] = coeff_v[n]
				except IndexError:
					print "Error j=",j,"n=", n
				n += 1
			coefficients.append(tuple_)
		print "coefficients=", coefficients
		lp.addConstraint(coefficients, "<=", self.V)

		print "==========Restriccion c)"
		for i in range(0, self.M):
			coefficients = [0] * L
			z = i
			while z < L - 2:
				print "z=", z
				coefficients[z] = 1
				z += self.M
			#print "Last constraint coeffs ", c
			lp.addConstraint(coefficients, "=", 1)
			print coefficients

		
		print "==========Restriccion d) "
		k = 0
		coefficients = []
		for i in range(0, self.M):
			n = 0
			#Initializing a coefficient row to zeros
			tuple_ = [0] * L
			if i==0:
				x = k
				y = (i + 1) * (self.M)
				k = k + self.M
			else:
				x = k 
				y = (i + 1) * (self.M)
				k = k + self.M
			print "x=", x
			print "y=", y
			for j in range(x, y):
				try:
					tuple_[j] = coeff_p[n]
				except IndexError:
					print "Error j=",j,"n=", n
				n += 1
			tuple_[L - 2] = -1
			#Appending new row to the coefficients
			coefficients.append(tuple_)
		print "coefficients=", coefficients
		lp.addConstraint(coefficients, "<=", 0)

		print "==========Restriccion e) "
		k = 0
		coefficients = []
		for i in range(0, self.M):
			n = 0
			#Initializing a coefficient row to zeros
			tuple_ = [0] * L
			if i==0:
				x = k
				y = (i + 1) * (self.M)
				k = k + self.M
			else:
				x = k
				y = (i + 1) * (self.M)
				k = k + self.M
			print "x=", x
			print "y=", y
			for j in range(x, y):
				try:
					tuple_[j] = coeff_p[n] * -1
				except IndexError:
					print "Error j=",j,"n=", n
				n += 1
			tuple_[L - 1] = 1
			#Appending new row to the coefficients
			coefficients.append(tuple_)
		print "coefficients=", coefficients
		lp.addConstraint(coefficients, "<=", 0)

	def _set_objective(self):
		global lp
		L = self.M * self.M + 2
		coefficients = [0] * L
		coefficients[L - 2] = 1
		coefficients[L - 1] = 1
		print "==========Objective ", coefficients
		lp.setObjective(coefficients, mode="minimize")



		

