import sys
import os

from PyQt4 import QtCore, QtGui, uic
from PyQt4.QtGui import QMessageBox
from PyQt4.QtGui import *
from PyQt4.QtCore import *

login = uic.loadUiType("gui/main.ui")[0]

class Login(QtGui.QWidget, login):
	def __init__(self, parent = None):
		super(Login, self).__init__()
		QtGui.QWidget.__init__(self, parent)
		self.setupUi(self)
		self.show()

if __name__=="__main__":
	 app=QtGui.QApplication(sys.argv)
	 FWindows = Login(None)
	 FWindows.show()
	 app.exec_()