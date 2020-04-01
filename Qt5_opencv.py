__author__ = 'jssmith'

import sys
from PyQt5 import QtWidgets
import cv2


class Window(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.b1 = QtWidgets.QPushButton('Activate Camera')
        self.b2 = QtWidgets.QPushButton('Record')

        # ###h_box = QtWidgets.QHBoxLayout()
        # ###h_box.addStretch()
        # ###h_box.addWidget(self.l)
        # ###h_box.addStretch()

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.b1)
        v_box.addWidget(self.b2)
        # ###v_box.addLayout(h_box)

        self.setLayout(v_box)
        self.setWindowTitle('PyQt5 Lesson 5')

        self.b1.clicked.connect(self.activate_click)

        self.show()

    def activate_click(self):
        print('hallo')
        camera = cv2.VideoCapture(0)
        while camera.isOpened():

            ret, frame = camera.read()

            if ret:
                # frame = cv2.flip(frame,0)
                # cv2.putText(frame, alpha, (50, 460), cv2.FONT_ITALIC, 0.8, (255, 255, 255))
                # cv2.putText(frame, ts.value, (50, 400), 5, 0.8, (255, 255, 255))
                # cv2.putText(frame2, ts.value, (50, 400), 5, 0.8, (255, 255, 255))
                # cv2.putText(frame, hotness, (50, 430), 5, 0.8, (255, 255, 255))

                # write the flipped frame
                # out.write(frame)

                cv2.imshow('LiveFeed-LOM', frame)

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    camera.release()
                    cv2.destroyAllWindows()
                    break
            else:
                break

        # out.release()
        # cv2.destroyAllWindows()


app = QtWidgets.QApplication(sys.argv)
a_window = Window()
sys.exit(app.exec_())
