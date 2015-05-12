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

class AppGUI(QtGui.QFrame):
	def __init__(self):
		super(AppGUI, self).__init__()
		self.solver = solver.Solver()
		path = QtGui.QFileDialog.getOpenFileName(None,
   			 _fromUtf8("Open File"), "/home", _fromUtf8("Files (*.txt *.ini)"))
		self.solver.initialize(path)
		data = self.solver.solve_()
		str_data = "Solution: "+ data['solution'] + "\n" + "Indices Solution: "+ data['indices_solution'] + "\n" + "Solution Value: "+ data['solution_value'] + "\n" +"Iterations: "+ data['Iterations']
		msgBox = QtGui.QMessageBox.information(self, _fromUtf8("Salida"),_fromUtf8(str_data), QtGui.QMessageBox.Ok, QtGui.QMessageBox.Ok)
		#self.close()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    w = AppGUI()
    #w.show()
    sys.exit(app.exec_())