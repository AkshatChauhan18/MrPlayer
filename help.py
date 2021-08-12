######################################
# Copyright (c) Akshat Chauahn ,2021 #
# This help window of MrPlayer       #
######################################
from PySide2 import QtCore, QtGui, QtWidgets


class Ui_HelpWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setObjectName("HelpWindow")
        self.setFixedSize(601, 450)
        self.setStyleSheet("background-color:black")
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.HelpView = QtWidgets.QTextBrowser(self.centralwidget)
        self.HelpView.setGeometry(QtCore.QRect(10, 30, 581, 420))
        self.HelpView.setStyleSheet("color:#DD521F;border:0px")
        self.HelpView.setObjectName("textBrowser")
# #################### adding title bar
        self.titlebar = QtWidgets.QToolBar()
        self.titlebar.setFloatable(False)
        self.titlebar.setMovable(False)
        self.addToolBar(self.titlebar)
        self.dragPos = QtCore.QPoint()
        self.titlebar.mousePressEvent = self.mousePressEvent
        self.titlebar.mouseMoveEvent = self.mouseMoveEvent
        self.texticon = QtWidgets.QLabel('Help ?')
        self.texticon.setFont(QtGui.QFont('Arial', 14))
        self.texticon.setStyleSheet('color:gray')
        self.titlebar.addWidget(self.texticon)
        self.spacer = QtWidgets.QWidget()
        self.spacer.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.titlebar.addWidget(self.spacer)
        self.titlebar.setStyleSheet('background-color:#21252B ; border-top: 0px solid black')
        self.closeAction = QtWidgets.QAction()
        self.closeAction.setIcon(QtGui.QIcon('assets/close.png'))
        self.miniAction = QtWidgets.QAction()
        self.miniAction.setIcon(QtGui.QIcon('assets/minimize.png'))
        self.titlebar.addAction(self.closeAction)
        self.titlebar.addAction(self.miniAction)
        self.setCentralWidget(self.centralwidget)
        self.HelpView.setOpenExternalLinks(True)
        QtCore.QMetaObject.connectSlotsByName(self)
        self.miniAction.triggered.connect(self.minimize)
        self.closeAction.triggered.connect(self.closewin)
        self.html=open('assets/help.html','r').read()
        self.HelpView.setHtml(self.html)
        self.show()
    def mousePressEvent(self, event):  # +
        self.dragPos = event.globalPos()

    def mouseMoveEvent(self, event):  # !!!
        if event.buttons() == QtCore.Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()
    def minimize(self):
        self.showMinimized()

    def closewin(self):
        self.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    helpWindow = Ui_HelpWindow()
    sys.exit(app.exec_())
