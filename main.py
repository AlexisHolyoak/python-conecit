import sys
import os
#PARA LLAMAR A LA ENCRIPTACION
import hashlib
from PyQt4 import QtCore, QtGui, uic
from PyQt4.QtGui import QMessageBox
from PyQt4.QtGui import *
from PyQt4.QtCore import *

try:
	import config
except Exception as e: 
	print e

login = uic.loadUiType("gui/main.ui")[0]
swin = uic.loadUiType("gui/content.ui")[0]
class Login(QtGui.QWidget, login):
	def __init__(self, parent = None):
		super(Login, self).__init__()
		QtGui.QWidget.__init__(self, parent)
		self.setupUi(self)
		self.show()
		self.BTN_INGRESAR.clicked.connect(self.ValidarUsuario)

	def ValidarUsuario(self):
		usuario = self.TXTUSUARIO.text()
		passw = self.TXTPASS.text()
		if usuario == "":
			print "INGRESAR USUARIO"
			self.TXTUSUARIO.setFocus()
		elif passw == "":
			print "INGRESAR CONTRASena"
			self.TXTPASS.setFocus()
		else:
			self.Loguear(usuario,passw)

	def Loguear(self,usuario,passw): 
		query ="SELECT Passw from Usuarios "
		query +="where Usuario like '%s'" % usuario
		query += "limit 1"
		result = config.run_query(query)
		if len(result) ==0:
			print "NO HAY USUARIOS REGISTRADOS"
		else:
			passw1 = hashlib.sha512(passw).hexdigest()
			passw2 = result[0][0]
			if passw1 == passw2:
				self.IngresarRegistro()
			else:
				print "ERROR"
	def IngresarRegistro(self):
		self.children = []
		child = SystemWindows()
		self.children.append(child)
		self.close()

class SystemWindows(QtGui.QWidget,swin):
	def __init__(self, parent = None):
		super(SystemWindows,self).__init__()
		QtGui.QWidget.__init__(self,parent)
		self.setupUi(self)
		self.show()

if __name__=="__main__":
	 app=QtGui.QApplication(sys.argv)
	 FWindows = Login(None)
	 FWindows.show()
	 app.exec_()

