
from PyQt5 import QtCore, QtGui, QtWidgets,QtMultimedia
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import os
import os.path
import time

path = f"{os.path.expanduser('~')}\\Music\\MrPlayer-songs"
if os.path.exists(path):
    pass
else:
    os.mkdir(path)

# #### stylesheet of main slider
slider_style=("QSlider::groove:horizontal {\n"
"border: 1px solid #bbb;\n"
"background: white;\n"
"height: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"background: qlineargradient(x1: 0, y1: 0,    x2: 0, y2: 1,\n"
"    stop: 0 #9464B9, stop: 1 #bbf);\n"
"background: qlineargradient(x1: 0, y1: 0.2, x2: 1, y2: 1,\n"
"    stop: 0 #D83B01, stop: 1 #55f);\n"
"border: 1px solid #777;\n"
"height: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"background: black;\n"
"border: 1px solid #777;\n"
"height: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"    stop:0 #D83B01, stop:1 #ccc);\n"
"border: 1px solid #777;\n"
"width: 13px;\n"
"margin-top: -10px;\n"
"margin-bottom: -10px;\n"
"border-radius: 4px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"    stop:0 #9464B9, stop:1 #ddd);\n"
"border: 1px solid #444;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal:disabled {\n"
"background: #bbb;\n"
"border-color: #999;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal:disabled {\n"
"background: #eee;\n"
"border-color: #999;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:disabled {\n"
"background: #eee;\n"
"border: 1px solid #aaa;\n"
"border-radius: 4px;\n"
"}\n"
"")

# Style sheet of volume slider
vol_slider_style=("QSlider::groove:horizontal {\n"
"border: 1px solid #bbb;\n"
"background: white;\n"
"height: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"background: qlineargradient(x1: 0, y1: 0,    x2: 0, y2: 1,\n"
"    stop: 0 #9464B9, stop: 1 #bbf);\n"
"background: qlineargradient(x1: 0, y1: 0.2, x2: 1, y2: 1,\n"
"    stop: 0 #D83B01, stop: 1 #55f);\n"
"border: 1px solid #777;\n"
"height: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"background: black;\n"
"border: 1px solid #777;\n"
"height: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"background: #9464B9;\n"
"border: 1px solid #777;\n"
"width: 6px;\n"
"margin-top: -10px;\n"
"margin-bottom: -10px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal:disabled {\n"
"background: #bbb;\n"
"border-color: #999;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal:disabled {\n"
"background: #eee;\n"
"border-color: #999;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:disabled {\n"
"background: #eee;\n"
"border: 1px solid #aaa;\n"
"border-radius: 4px;\n"
"}\n"
"")

class helpWindow(object):
    def setupUi(self, se):
        se.setObjectName("HelpWindow")
        se.resize(619, 84)
        se.setStyleSheet("background-color:#0D3622")
        se.setDocumentMode(False)

        self.label = QtWidgets.QLabel()

        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color:rgb(148, 100, 185)")
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        se.setCentralWidget(self.label)

        self.retranslateUi(se)
        QtCore.QMetaObject.connectSlotsByName(se)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Help ❓"))
        self.label.setText(_translate("MainWindow", "MrPlayer is a MP3 player made on Python. First time you will run it , it wil create a folder in your \n"
"Music folder. Close the app and add songs in the MrPlayer-songs folder in Music filder and re run the \n"
"app.  Enjoy using  MrPlayer 😎😎\n"
"\n"
"Made by AkshatChauhan18 "))
        self.label.setFont(QFont('arial',14))


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(QSize(410,620))
        MainWindow.setStyleSheet("background-color:black;color:#9464B9")
        MainWindow.setWindowFlags(Qt.FramelessWindowHint)
        
# Adding toolbar as title bar
        self.toolbar = QToolBar()
        self.toolbar.setFloatable(False)
        self.toolbar.setMovable(False)
        MainWindow.addToolBar(self.toolbar)
        self.icon = QLabel()
        self.icon.setPixmap(QPixmap('icon.png').scaled(25,25))
        self.texticon = QLabel('                           MrPlayer              ')
        self.texticon.setFont(QFont('Arial',14))
        self.texticon.setStyleSheet('color:gray')
        self.toolbar.addWidget(self.icon)
        self.toolbar.addWidget(self.texticon)
        self.toolbar.setStyleSheet('background-color:#21252B ; border-top: 0px solid black')
        self.closeAction = QAction()
        self.closeAction.setIcon(QIcon('assets/close.png'))
        self.miniAction = QAction()
        self.miniAction.setIcon(QIcon('assets/minimize.png'))
        self.help_btn = QAction()
        self.help_btn.setIcon(QIcon('assets/help.png'))
        self.toolbar.addAction(self.help_btn)
        self.toolbar.addAction(self.closeAction)
        self.toolbar.addAction(self.miniAction)
       
# ###############################################################

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 10, 241, 240))
        self.label.setStyleSheet("background-color:black")
        self.label.setText("")
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 250, 391, 181))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(16)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("color:rgb(148, 100, 185);")
        self.groupBox.setObjectName("groupBox")
        self.listWidget = QtWidgets.QListWidget(self.groupBox)
        self.listWidget.setGeometry(QtCore.QRect(10, 30, 371, 140))
        self.listWidget.setStyleSheet("color:rgb(216, 59, 1)")

        self.listWidget.setObjectName("listWidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 440, 391, 91))
        self.frame.setStyleSheet("background-color:#0D3622")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.slider = QtWidgets.QSlider(self.frame)
        self.slider.setGeometry(QtCore.QRect(10, 10, 371, 31))
        self.slider.setStyleSheet(slider_style)
        self.slider.setOrientation(QtCore.Qt.Horizontal)
        self.slider.setObjectName("slider")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setEnabled(True)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 410, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
       
        font.setUnderline(False)
        font.setWeight(75)
        self.menubar.setFont(font)
        self.menubar.setDefaultUp(False)
        self.menubar.setNativeMenuBar(True)
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
       
       


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.listWidget.setCurrentRow(0)
# ### adding items in list
        for item in os.listdir(path):
            if item.endswith('.mp3'):
                self.listWidget.insertItem(0,item.strip('.mp3'))

# ############### adding backward button
        self.backward_btn = QPushButton(self.frame)
        self.backward_btn.setIcon(QIcon('assets\\backward.png'))
        self.backward_btn.setIconSize(QSize(40,40))
        self.backward_btn.setGeometry(QtCore.QRect(10, 45, 40, 40))

# ############### adding play button
        self.play_btn = QPushButton(self.frame)
        self.play_btn.setIcon(QIcon('assets\\play.png'))
        self.play_btn.setIconSize(QSize(40, 40))
        self.play_btn.setGeometry(QtCore.QRect(60, 45, 40, 40))

# ############### adding pause button
        self.pause_btn = QPushButton(self.frame)
        self.pause_btn.setIcon(QIcon('assets\\pause.png'))
        self.pause_btn.setIconSize(QSize(40, 40))
        self.pause_btn.setGeometry(QtCore.QRect(110, 45, 40, 40))

# ############### adding forward button
        self.forward_btn = QPushButton(self.frame)
        self.forward_btn.setIcon(QIcon('assets\\forward.png'))
        self.forward_btn.setIconSize(QSize(40, 40))
        self.forward_btn.setGeometry(QtCore.QRect(160, 45, 40, 40))

# ############### adding visualizer to label
        self.movie = QMovie('assets\\visualize1.gif')
        self.label.setMovie(self.movie)

# ##################################################### adding volume img
        vol=QPixmap('assets\\vol.png')
        vol=vol.scaled(30,30)
        vol_img_label = QLabel(self.frame)
        vol_img_label.setPixmap(vol)
        vol_img_label.setGeometry(QtCore.QRect(240, 50, 30, 30))

# Adding music status
        self.status_label = QLabel(self.centralwidget)
        self.status_label.setGeometry(QRect(10, 531, 391, 70))
        self.status_label.setStyleSheet('color:white')
# adding volume slider
        self.vol_slider = QSlider(Qt.Horizontal,self.frame)
        self.vol_slider.setGeometry(QtCore.QRect(280, 50, 100, 30))
        self.vol_slider.setRange(0,100)
        self.vol_slider.setValue(100)
        self.vol_slider.setStyleSheet(vol_slider_style)
# Adding Audio player
        try:
            self.player = QtMultimedia.QMediaPlayer()
            self.listWidget.setCurrentRow(0)
            item = self.listWidget.item(0)

            self.content = QtMultimedia.QMediaContent(QUrl.fromLocalFile(str(f'{path}\\{item.text()}.mp3')))
            self.player.setMedia(self.content)
            self.player.play()
            self.player.pause()
        except:
            pass

# Triggering actions
        self.play_btn.clicked.connect(self.Play_Music)
        self.pause_btn.clicked.connect(self.Pause_music)
        self.player.positionChanged.connect(self.MediaPosition_changed)
        self.player.durationChanged.connect(self.MediaDuration_Changed)
        self.slider.sliderMoved.connect(self.SetMedia_Position)
        self.vol_slider.sliderMoved.connect(self.SetVolume)
        self.forward_btn.clicked.connect(self.next_song)
        self.listWidget.itemSelectionChanged.connect(self.Setplayer_content)
        self.backward_btn.clicked.connect(self.previous_song)
        self.help_btn.triggered.connect(self.help)
        self.miniAction.triggered.connect(self.minimize)
        self.closeAction.triggered.connect(self.closewin)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MrPlayer"))
        self.groupBox.setTitle(_translate("MainWindow", "Songs"))


    def Play_Music(self):

        if self.listWidget.count()==0:
            return

        self.player.play()
        self.movie.start()

    def Pause_music(self):
        self.player.pause()
        self.movie.stop()

    def MediaPosition_changed(self,position):
        self.slider.setValue(position)
        dur = self.player.duration()/1000
        conver = time.strftime('%M:%S',time.gmtime(dur))
        current_time = self.player.position()/1000
        converted_time = time.strftime('%M:%S',time.gmtime(current_time))
        self.status_label.setText(f'{converted_time} /{conver}     {self.listWidget.currentItem().text()} ')
    def MediaDuration_Changed(self,duration):
        self.slider.setRange(0,duration)
    def SetMedia_Position(self,position):
        self.player.setPosition(position)
        if self.player.position() == self.player.duration():
            self.movie.stop()
    def SetVolume(self,vol):
        self.player.setVolume(vol)
    def Setplayer_content(self):
        try:
            item = self.listWidget.currentItem()

            self.content = QtMultimedia.QMediaContent(QUrl.fromLocalFile(str(f'{path}\\{item.text()}.mp3')))
            self.player.setMedia(self.content)
            self.movie.stop()
        except:
            pass

    def next_song(self):

        try :
            if self.listWidget.currentRow()==self.listWidget.count()-1:
                return
            else:
                self.listWidget.setCurrentRow(self.listWidget.currentRow()+1)
                item = self.listWidget.currentItem()

                self.content = QtMultimedia.QMediaContent(QUrl.fromLocalFile(str(f'{path}\\{item.text()}.mp3')))
                self.player.setMedia(self.content)
                self.player.play()
                self.movie.start()
        except Exception as e:
            print(e)

    def previous_song(self):
        try:
            if self.listWidget.currentRow()==0:
                return

            self.listWidget.setCurrentRow(self.listWidget.currentRow() -1)
            item = self.listWidget.currentItem()

            self.content = QtMultimedia.QMediaContent(QUrl.fromLocalFile(str(f'{path}\\{item.text()}.mp3')))
            self.player.setMedia(self.content)
            self.player.play()
            self.movie.start()
        except:
            pass


    def stop_movie(self):
        if self.player.position() == self.player.duration():
            self.movie.stop()

    def help(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = helpWindow()
        self.ui.setupUi(self.window)
        self.window.show()
    def minimize(self):
        MainWindow.showMinimized()
    def closewin(self):
        MainWindow.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
