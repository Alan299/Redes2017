import sys
from PyQt4 import QtCore, QtGui
from GUI import Login as log
from GUI import GUI 
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    login = log.Login()

    if login.exec_() == QtGui.QDialog.Accepted:
        g = GUI.GUI()
        g.show()
        sys.exit(app.exec_())