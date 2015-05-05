
import sys
import os

class FileReader():
	
	@staticmethod
	def read_input(path):
		f = None
		try:
			f = open(path, "r")
			contents = f.readlines()
			N = int(contents[0].replace("\n", ""))
			line2 = contents[1].replace("\n", "").split(" ")
			V = float(line2[0])
			P = float(line2[1])
			linesN = contents[2:]
			v = []
			p = []
			for line in linesN:
				line = line.replace("\n", "")
				line = line.split(" ")
				v.append(line[1])
				p.append(line[2])
			return {'N':N, 'V':V, 'P':P, 'v':v, 'p':p}
		except IOError as ioex:
			print "Error while reading input...", ioex
		finally:
			try:
				f.close()
			except Exception as ex:
				print ex






#FileReader.read_input("/home/crisefd/Documentos/Python/prueba.txt")
