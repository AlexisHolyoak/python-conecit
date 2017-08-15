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
		self.BTN_INGRESAR.clicked.connect(self.ValidarUsuario)

	def ValidarUsuario(self):
		 import hashlib
		 tmp = hashlib.sha512("alex").hexdigest()
#35f319ca1dfc9689f5a33631c8f93ed7c3120ee7afa05b1672c7df7b71f63a6753def5fd3ac9db2eaf90ccab6bff31a486b51c7095ff958d228102b84efd7736

		 self.TXTUSUARIO.setText(tmp)
if __name__=="__main__":
	 app=QtGui.QApplication(sys.argv)
	 FWindows = Login(None)
	 FWindows.show()
	 app.exec_()
