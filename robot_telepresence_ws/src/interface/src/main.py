#!/usr/bin/env python3
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *
import rospy
import sys

import std_msgs.msg


class MainWindow(QMainWindow):

    def coucou(self):
        sender = self.sender()
        self.pub.publish(std_msgs.msg.String(sender.property("value")))

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        rospy.init_node("appli")
        self.pub = rospy.Publisher('key_app', std_msgs.msg.String, queue_size=10)



        self.online_webcams = QCameraInfo.availableCameras()
        if not self.online_webcams:
            pass #quit
        self.exist = QCameraViewfinder()
        #self.exist.show()
        wid = QWidget()

        # Première ligne
        laybut = QHBoxLayout()

        but1 = QPushButton()
        but2 = QPushButton()
        but3 = QPushButton()
        but10 = QPushButton()

        laybut.addWidget(but1)
        laybut.addWidget(but2)
        laybut.addWidget(but3)
        laybut.addWidget(but10)

        but1.setText("a")
        but2.setText("z")
        but3.setText("e")
        but10.setText("up")

        but1.setProperty("value", "a")
        but2.setProperty("value", "z")
        but3.setProperty("value", "e")
        but10.setProperty("value", "up")

        #Deuxième ligne
        laybut1 = QHBoxLayout()

        but4 = QPushButton()
        but5 = QPushButton()
        but6 = QPushButton()
        but11 = QPushButton()

        laybut1.addWidget(but4)
        laybut1.addWidget(but5)
        laybut1.addWidget(but6)
        laybut1.addWidget(but11)

        but4.setText("q")
        but5.setText("s")
        but6.setText("d")

        but4.setProperty("value", "q")
        but5.setProperty("value", "s")
        but6.setProperty("value", "d")

        but11.setDisabled(True)

        #Troisième ligne
        laybut2 = QHBoxLayout()

        but7 = QPushButton()
        but8 = QPushButton()
        but9 = QPushButton()
        but12 = QPushButton()

        laybut2.addWidget(but7)
        laybut2.addWidget(but8)
        laybut2.addWidget(but9)
        laybut2.addWidget(but12)

        but8.setText("x")
        but8.setProperty("value", "x")

        but12.setText("down")
        but12.setProperty("value", "down")


        but7.setDisabled(True)
        but9.setDisabled(True)

        #Create all signals

        but1.clicked.connect(self.coucou)
        but2.clicked.connect(self.coucou)
        but3.clicked.connect(self.coucou)
        but4.clicked.connect(self.coucou)
        but5.clicked.connect(self.coucou)
        but6.clicked.connect(self.coucou)
        but8.clicked.connect(self.coucou)
        but10.clicked.connect(self.coucou)
        but12.clicked.connect(self.coucou)

        #Add all in widget
        lay = QVBoxLayout()
        lay.addWidget(self.exist)
        lay.addLayout(laybut)
        lay.addLayout(laybut1)
        lay.addLayout(laybut2)
        wid.setLayout(lay)

        self.setCentralWidget(wid)
        # set the default webcam.
        self.get_webcam(0)
        self.setWindowTitle("WebCam")
        self.show()

    def get_webcam(self, i):
        self.my_webcam = QCamera(self.online_webcams[i])
        self.my_webcam.setViewfinder(self.exist)
        self.my_webcam.setCaptureMode(QCamera.CaptureStillImage)
        self.my_webcam.error.connect(lambda: self.alert(self.my_webcam.errorString()))
        self.my_webcam.start()

    def alert(self, s):
        """
        This handle errors and displaying alerts.
        """
        err = QErrorMessage(self)
        err.showMessage(s)

    def keyPressEvent(self, event):
        key = event.key()
        print(key)

        if key == QtCore.Qt.Key_A:
            print('a')
            self.pub.publish(std_msgs.msg.String('a'))
        elif key == QtCore.Qt.Key_Z:
            print('z')
            self.pub.publish(std_msgs.msg.String('z'))
        elif key == QtCore.Qt.Key_E:
            print('e')
            self.pub.publish(std_msgs.msg.String('e'))
        elif key == QtCore.Qt.Key_Q:
            print('q')
            self.pub.publish(std_msgs.msg.String('q'))
        elif key == QtCore.Qt.Key_S:
            print('s')
            self.pub.publish(std_msgs.msg.String('s'))
        elif key == QtCore.Qt.Key_D:
            print('d')
            self.pub.publish(std_msgs.msg.String('d'))
        elif key == QtCore.Qt.Key_X:
            print('x')
            self.pub.publish(std_msgs.msg.String('x'))


if __name__ == '__main__':

    app = QApplication(sys.argv)
    app.setApplicationName("WebCam")

    window = MainWindow()
    app.exec_()
