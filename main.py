from test import *
import sys
import time
import sys 
import cv2
import psutil
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *


class main(Ui_MainWindow):

    def __init__(self, window):
        self.setupUi(window)
        self.Reset.clicked.connect(self.webcamshow)
        self.Stop.clicked.connect(self.stopprog)


    def webcamshow(self):
        self.available_cameras = QCameraInfo.availableCameras()
        self.select_camera(0)
        camera_selector = self.VideoInput()
        camera_selector.addItems([camera.description() for camera in self.available_cameras])
        camera_selector.currentIndexChanged.connect(self.select_camera)

    def select_camera(self, i):
        self.camera = QCamera(self.available_cameras[i])
        self.camera.start()
        self.current_camera_name = self.available_cameras[i].description()

    

    


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = main(MainWindow)
MainWindow.show()
app.exec_()

























