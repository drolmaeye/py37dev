__author__ = 'jssmith'

import sys
from PyQt5 import QtWidgets
from epics import Motor


# ###def window():
# ###    app = QtWidgets.QApplication(sys.argv)
# ###    w = QtWidgets.QWidget()
# ###    l = QtWidgets.QLabel(w)
# ###    m = Motor('16TEST1:m9')
# ###    text = str(m.get('RBV'))
# ###    print(text)
# ###    l.setText(text)
# ###    w.show()
# ###    sys.exit(app.exec_())
# ###
# ###
# ###window()


class Window(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.b = QtWidgets.QPushButton('Push me')
        self.l = QtWidgets.QLabel('I have not been clicked yet')
        self.m = Motor('16TEST1:m9')

        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addWidget(self.l)
        h_box.addStretch()

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.b)
        v_box.addLayout(h_box)

        self.setLayout(v_box)
        self.setWindowTitle('PyQt5 Lesson 5')

        self.b.clicked.connect(self.btn_click)

        self.show()

    def btn_click(self):
        text = str(self.m.get('RBV'))
        self.l.setText(text)



app = QtWidgets.QApplication(sys.argv)
a_window = Window()
sys.exit(app.exec_())

