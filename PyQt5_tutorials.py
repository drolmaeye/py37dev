__author__ = 'jssmith'

import sys
from PyQt5 import QtWidgets
from epics import Motor


def window():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    l = QtWidgets.QLabel(w)
    m = Motor('16TEST1:m9')
    text = str(m.get('RBV'))
    print(text)
    l.setText(text)
    w.show()
    sys.exit(app.exec_())


window()
