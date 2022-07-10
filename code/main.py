#!/usr/bin/env python3
#
# Troglobyte AppHub:
# author: Michael Gene Brockus
# Gmail: <mail: michaelbrockus@gmail.com>
#
from .program import greet

import sys
from PyQt6.QtWidgets import QApplication, QPushButton


def main_prog():
    app = QApplication(sys.argv)
    window.show()
    app.exec()
