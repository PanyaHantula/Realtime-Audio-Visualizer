"""
git remote add origin https://github.com/PanyaHantula/Realtime-Audio-Visualizer.git
git branch -M main
git push -u origin main

"""

import sys
from PySide6.QtGui import QGuiApplication, QFont
from PySide6.QtCore import Qt, QSize, QTimer, QTime
from PySide6.QtWidgets import QApplication, QMainWindow, \
    QGridLayout, QHBoxLayout, QVBoxLayout, \
    QWidget, QPushButton, QLineEdit, QCheckBox, QLabel, QGroupBox
import pyqtgraph as pg

class MainWindown (QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Real Time Audio Visualize')
        self.setFixedSize(QSize(800,420))

if __name__ == '__main__':
    app = QApplication([])
    with open('./Stylesheet.qss','r') as style:
         app.setStyleSheet(style.read())

    EMedHealth_windown = MainWindown()
    EMedHealth_windown.show()
    app.exec()
