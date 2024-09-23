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
import numpy as np
from random import randint

class MainPage (QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Real Time Audio Visualize')
        self.setFixedSize(QSize(1024,600))

        #Create hBox1
        GraphBox = QHBoxLayout()
        self.setLayout(GraphBox)

        # ------------------------------------------------------------ #
        # Creat vBox Graph No.1 (Left Layer)
        AudioWaveformGraphVBoxLeft = QVBoxLayout()
        GraphBox.addLayout(AudioWaveformGraphVBoxLeft)

        self.GraphWaveformAudio = pg.PlotWidget()           # Creat Graph Widget
        AudioWaveformGraphVBoxLeft.addWidget(self.GraphWaveformAudio)       # add vBox for  in hBox1

        # Dummy data to plot graph
        self.WaveformData_X = list(range(100))  # 100 time points
        self.WaveformData_Y = [randint(0,100) for _ in range(100)]  # 100 data points

        # plot data: x, y values
        self.GraphWaveformAudio.setBackground('#FFFFFF')        # Background Colour
        pen = pg.mkPen(color=(255, 0, 0),width=5)               # Line Colour, Width & Style
        self.GraphWaveformAudio.setTitle("Audio waveform", color="b", size="20pt")    # Plot Titles
        
        styles = {'color':'r', 'font-size':'20px'}      # Axis Labels
        self.GraphWaveformAudio.setLabel('left', 'Amplitude', **styles)
        self.GraphWaveformAudio.setLabel('bottom', 'Time (Sec)', **styles) 
        self.GraphWaveformAudio.showGrid(x=True, y=True)# Background Grid
        #self.GraphWaveformAudio.setXRange(0, 10, padding=0)    # Setting Axis Limits
        #self.GraphWaveformAudio.setYRange(20, 55, padding=0)
        self.data_line =  self.GraphWaveformAudio.plot(self.WaveformData_X, self.WaveformData_Y, pen=pen)

        # ------------------------------------------------------------ #
        # Creat vBox Graph No.2 (Right Layer)
        AudioWaveformGraphVBoxRight = QVBoxLayout()
        GraphBox.addLayout(AudioWaveformGraphVBoxRight)

        self.GraphFFTAudio = pg.PlotWidget()           # Creat Graph Widget
        AudioWaveformGraphVBoxLeft.addWidget(self.GraphFFTAudio)       # add vBox for  in hBox1

        # Dummy data to plot graph
        self.FFTx = list(range(100))  # 100 time points
        self.FFTy = [randint(0,100) for _ in range(100)]  # 100 data points

        # plot data: x, y values
        self.GraphFFTAudio.setBackground('#FFFFFF')        # Background Colour
        pen = pg.mkPen(color=(0, 0, 255),width=5)               # Line Colour, Width & Style
        self.GraphFFTAudio.setTitle("Audio waveform", color="b", size="20pt")    # Plot Titles
        
        styles = {'color':'r', 'font-size':'20px'}      # Axis Labels
        self.GraphFFTAudio.setLabel('left', 'Amplitude', **styles)
        self.GraphFFTAudio.setLabel('bottom', 'Time (Sec)', **styles) 
        self.GraphFFTAudio.showGrid(x=True, y=True)# Background Grid
        #self.GraphFFTAudio.setXRange(0, 10, padding=0)    # Setting Axis Limits
        #self.GraphFFTAudio.setYRange(20, 55, padding=0)
        self.data_line_FFT =  self.GraphFFTAudio.plot(self.FFTx, self.FFTy, pen=pen)

    def update_plot_data(self):
        # Dummy data to plot graph
        self.WaveformData_X = list(range(100))  # 100 time points
        self.WaveformData_Y = [randint(0,100) for _ in range(100)]  # 100 data points
        self.data_line.setData(self.WaveformData_X, self.WaveformData_Y)  # Update the data.

        # Dummy data to plot graph
        self.FFTx = list(range(100))  # 100 time points
        self.FFTy = [randint(0,100) for _ in range(100)]  # 100 data points
        self.data_line_FFT.setData(self.FFTx, self.FFTy)  # Update the data.

if __name__ == '__main__':
    app = QApplication([])
    EMedHealth_windown = MainPage()

    timer = QTimer()
    timer.setInterval(50)
    timer.timeout.connect(EMedHealth_windown.update_plot_data)
    timer.start()
    
    EMedHealth_windown.show()
    app.exec()
