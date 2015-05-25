#GUI

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CambioPass-IGU.ui'
#
# Created: Fri May  8 10:34:34 2015
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import os
import sys
import imp

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)
solver = None
try:
	path = os.path.abspath(os.path.dirname(__file__) + '/' + '.././Logic/solver.py')
	solver = imp.load_source("solver", path)
except IOError as err:
	print err
	path = os.path.abspath(os.path.dirname(__file__)  + '.././Logic/solver.py')
	solver = imp.load_source("solver", path)
"""
class Frame(QtGui.QFrame):
	def setupUi(self, Frame):
		print type(Frame)
		Frame.setObjectName(_fromUtf8("Frame"))
		Frame.resize(266, 179)
       	Frame.setFrameShape(QtGui.QFrame.StyledPanel)
       	Frame.setFrameShadow(QtGui.QFrame.Raised)
       	self.buttonOne = QtGui.QPushButton(Frame)
       	self.buttonOne.setGeometry(QtCore.QRect(80, 50, 100, 27))
       	self.buttonOne.setObjectName(_fromUtf8("buttonOne"))
       	self.buttonTwo = QtGui.QPushButton(Frame)
       	self.buttonTwo.setGeometry(QtCore.QRect(80, 100, 100, 27))
       	self.buttonTwo.setObjectName(_fromUtf8("buttonTwo"))
       	self.retranslateUi(Frame)
       	QtCore.QObject.connect(self.buttonOne, QtCore.SIGNAL(_fromUtf8("pressed()")), Frame.solveProblemOne)
       	QtCore.QObject.connect(self.buttonTwo, QtCore.SIGNAL(_fromUtf8("pressed()")), Frame.solveProblemTwo)
       	QtCore.QMetaObject.connectSlotsByName(Frame)


	def solveProblemOne(self):
		solver = solver.Solver1()
		path = QtGui.QFileDialog.getOpenFileName(None,
   			 _fromUtf8("Open File"), "/home", _fromUtf8("Files (*.txt *.ini)"))
		solver.initialize(path)
		data = solver.solve()
		str_data = "Configuration:\n"+ data['msg'] + "\n" + "Solution: "+ data['indices_solution'] + "\n" + "Solution Value: "+ data['solution_value'] + "\n" +"Iterations: "+ data['Iterations']
		msgBox = QtGui.QMessageBox.information(self, _fromUtf8("Salida"),_fromUtf8(str_data), QtGui.QMessageBox.Ok, QtGui.QMessageBox.Ok)
		self.close()

	def solveProblemTwo(self):
		solver = solver.Solver1()
		path = QtGui.QFileDialog.getOpenFileName(None,
   			 _fromUtf8("Open File"), "/home", _fromUtf8("Files (*.txt *.ini)"))
		solver.initialize(path)
		data = solver.solve()
		M = data['solution_value']
		P = solver.P
		p = solver.p
		V = solver.V
		v = solver.v
		solver = solver.Solver2()
		solver.initialize(M, p, v, P, V)
		data = solver.solve()
		str_data = "Configuration:\n"+ data['msg'] + "\n" + "Solution: "+ data['indices_solution'] + "\n" + "Solution Value: "+ data['solution_value'] + "\n" +"Iterations: "+ data['Iterations']
		msgBox = QtGui.QMessageBox.information(self, _fromUtf8("Salida"),_fromUtf8(str_data), QtGui.QMessageBox.Ok, QtGui.QMessageBox.Ok)
		self.close()

	def retranslateUi(self, Frame):
		Frame.setWindowTitle(_translate("Frame", "Frame", None))
       	self.buttonOne.setText(_translate("Frame", "Problem One", None))
       	self.buttonTwo.setText(_translate("Frame", "Problem Two", None))

	def __init__(self):
		print "Inicializando"
		super(Frame, self).__init__()
		#print type(Frame)
		self.setupUi(self)
"""

class Frame(QtGui.QFrame):
    def __init__(self):
        super(Frame, self).__init__()
        self.setupUi(self)

    def setupUi(self, Frame):
        Frame.setObjectName(_fromUtf8("Frame"))
        Frame.resize(266, 179)
        Frame.setFrameShape(QtGui.QFrame.StyledPanel)
        Frame.setFrameShadow(QtGui.QFrame.Raised)
        self.buttonOne = QtGui.QPushButton(Frame)
        self.buttonOne.setGeometry(QtCore.QRect(80, 50, 100, 27))
        self.buttonOne.setObjectName(_fromUtf8("buttonOne"))
        self.buttonTwo = QtGui.QPushButton(Frame)
        self.buttonTwo.setGeometry(QtCore.QRect(80, 100, 100, 27))
        self.buttonTwo.setObjectName(_fromUtf8("buttonTwo"))

        self.retranslateUi(Frame)
        QtCore.QObject.connect(self.buttonOne, QtCore.SIGNAL(_fromUtf8("pressed()")), Frame.solveProblemOne)
       	QtCore.QObject.connect(self.buttonTwo, QtCore.SIGNAL(_fromUtf8("pressed()")), Frame.solveProblemTwo)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def solveProblemOne(self):
		solver_ = solver.Solver1()
		path = QtGui.QFileDialog.getOpenFileName(None,
   			 _fromUtf8("Open File"), "/home", _fromUtf8("Files (*.txt *.ini)"))
		solver_.initialize(path)
		data = solver_.solve()
		str_data = "Configuration:\n"+ data['msg'] + "\n" + "Solution: "+ data['indices_solution'] + "\n" + "Solution Value: "+ data['solution_value'] + "\n" +"Iterations: "+ data['Iterations']
		msgBox = QtGui.QMessageBox.information(self, _fromUtf8("Salida"),_fromUtf8(str_data), QtGui.QMessageBox.Ok, QtGui.QMessageBox.Ok)
		self.close()

    def solveProblemTwo(self):
		solver_ = solver.Solver1()
		path = QtGui.QFileDialog.getOpenFileName(None,
   			 _fromUtf8("Open File"), "/home", _fromUtf8("Files (*.txt *.ini)"))
		solver_.initialize(path)
		data = solver_.solve()
		M = int(float(data['solution_value']))
		P = solver_.P
		p = solver_.p
		V = solver_.V
		v = solver_.v
		solver_ = solver.Solver2()
		solver_.initialize(M, p, v, P, V)
		data = solver_.solve()
		str_data = "Configuration:\n"+ data['msg'] + "\n" + "Solution: "+ data['indices_solution'] + "\n" + "Solution Value: "+ data['solution_value'] + "\n" +"Iterations: "+ data['Iterations']
		msgBox = QtGui.QMessageBox.information(self, _fromUtf8("Salida"),_fromUtf8(str_data), QtGui.QMessageBox.Ok, QtGui.QMessageBox.Ok)
		self.close()

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(_translate("Frame", "Frame", None))
        self.buttonOne.setText(_translate("Frame", "Problem One", None))
        self.buttonTwo.setText(_translate("Frame", "Problem Two", None))

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    w = Frame()
    w.show()
    sys.exit(app.exec_())