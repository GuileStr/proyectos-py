# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 07:20:25 2020

@author: palar
"""
import sys

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = QWidget()
    w.setWindowTitle('Battle')
    w.setWindowIcon(QIcon('icon.ico'))

    
    btn = QPushButton('Heal', w)
    btn.setToolTip('<b>Heal 16 hp</b>')
    btn.move(1000, 450)

    btn.setIcon(QIcon('icon.ico'))
    btn.clicked.connect(QCoreApplication.instance().quit)

    w.resize(1280, 720)
    w.show()

    sys.exit(app.exec_())