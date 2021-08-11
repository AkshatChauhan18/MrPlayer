#################################################################
# This is an open source project made in 2021 by Akshat Chauhan  #
# copyright (c) Akshat Chauhan                                   #
#################################################################

from PySide2 import QtCore, QtGui, QtWidgets, QtMultimedia
from PySide2.QtWidgets import QLabel, QPushButton, QToolBar, QWidget, QSlider, QSizePolicy, QAction,QStatusBar
from PySide2.QtCore import Qt, QSize, QUrl, QPoint
from PySide2.QtGui import Qt, QFont, QPixmap, QIcon, QMovie
import os
import os.path
import time
from help import Ui_HelpWindow
from lyrics import Ui_LyricsWindow

path = f"{os.path.expanduser('~')}\\Music\\MrPlayer-songs"
if os.path.exists(path):
    None
else:
    os.mkdir(path)

# #### stylesheet of main slider
slider_style = ("QSlider::groove:horizontal {\n"
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
####################################################
# Style sheet of volume slider
vol_slider_style = ("QSlider::groove:horizontal {\n"
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
######################################
# creating listwidget verticle scrollbar stylesheet
qlist_v_slider = ("""
        QScrollBar:vertical {  
            border: 1px solid #aaa;            
            border-radius:2px;
            background:white;
            width:13px;
            margin: 0px 3px 0px 0px;
        }
        QScrollBar::handle:vertical {
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
            stop: 0 rgb(251, 108, 73),  stop: 1 rgb(252, 30, 167));
            min-height: 0px;
        }
        QScrollBar::add-line:vertical {
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
            stop: 0 rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130),  stop:1 rgb(32, 47, 130));
            height: 0px;
            subcontrol-position: bottom;
            subcontrol-origin: margin;
        }
        QScrollBar::sub-line:vertical {
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
            stop: 0  rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130),  stop:1 rgb(32, 47, 130));
            height: 0 px;
            subcontrol-position: top;
            subcontrol-origin: margin;
        }
    """)
##############################################################################################

# creating qlist horizontal scrollbar stylesheet
qlist_h_slider = ("""
       QScrollBar:horizontal {
        border: 1px solid #aaa;            
        border-radius:2px;
  background-color: white;
    height: 13px;
    margin: 3px 0px 0px 0px;
 }

 QScrollBar::handle:horizontal {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
    stop: 0 rgb(251, 108, 73),  stop: 1 rgb(252, 30, 167));
    min-width: 25px;
 }
QScrollBar::add-line:horizontal {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
    stop: 0 rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130),  stop:1 rgb(32, 47, 130));
    height: 0px;
    subcontrol-position: right;
    subcontrol-origin: margin;
 }

 QScrollBar::sub-line:horizontal {
     background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
    stop: 0  rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130),  stop:1 rgb(32, 47, 130));
    height: 0 px;
    
    subcontrol-position: left;
    subcontrol-origin: margin;
 }
    """)

#################################################################################################################################################################

# creating main window
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(QSize(600, 630))
        MainWindow.setStyleSheet("background-color:black;color:#9464B9")
        MainWindow.setWindowFlags(Qt.FramelessWindowHint)

        # Adding toolbar as title bar
        self.titlebar = QToolBar()
        self.titlebar.setFloatable(False)
        self.titlebar.setMovable(False)
        MainWindow.addToolBar(self.titlebar)
        self.icon = QLabel()
        self.icon.setPixmap(QPixmap('icon.png').scaled(25, 25))
        self.texticon = QLabel('MrPlayer')
        self.texticon.setFont(QFont('Arial', 14))
        self.texticon.setStyleSheet('color:gray')
        self.titlebar.addWidget(self.icon)
        self.titlebar.addWidget(self.texticon)
        self.spacer = QWidget()
        self.spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.titlebar.addWidget(self.spacer)
        self.titlebar.setStyleSheet('background-color:#21252B ; border-top: 0px solid black')
        self.closeAction = QAction()
        self.closeAction.setIcon(QIcon('assets/close.png'))
        self.miniAction = QAction()
        self.miniAction.setIcon(QIcon('assets/minimize.png'))
        self.help_btn = QAction()
        self.help_btn.setIcon(QIcon('assets/help.png'))
        self.titlebar.addAction(self.help_btn)
        self.titlebar.addAction(self.closeAction)
        self.titlebar.addAction(self.miniAction)

        # ###############################################################

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        # adding visualizer label
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 10, 240, 240))
        self.label.setStyleSheet("background-color:black")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(307, 10, 240, 240))
        self.label2.setStyleSheet("background-color:black")
        self.label2.setText("")
        self.label2.setObjectName("label")
        #####################################################################
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 210, 581, 220))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(16)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("color:rgb(148, 100, 185);")
        self.groupBox.setObjectName("groupBox")
        self.listWidget = QtWidgets.QListWidget(self.groupBox)
        self.listWidget.setGeometry(QtCore.QRect(10, 30, 561, 179))
        self.listWidget.setStyleSheet("color:rgb(216, 59, 1)")
        self.listWidget.verticalScrollBar().setStyleSheet(qlist_v_slider)
        self.listWidget.horizontalScrollBar().setStyleSheet(qlist_h_slider)
        self.listWidget.setObjectName("listWidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 440, 581, 91))
        self.frame.setStyleSheet("background-color:#0D3622")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        # adding time slider
        self.slider = QtWidgets.QSlider(self.frame)
        self.slider.setGeometry(QtCore.QRect(10, 10, 561, 31))
        self.slider.setStyleSheet(slider_style)
        self.slider.setOrientation(QtCore.Qt.Horizontal)
        self.slider.setObjectName("slider")
        self.dragPos = QPoint()
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.listWidget.setCurrentRow(0)
        # ### adding items in list
        for item in os.listdir(path):
            if item.endswith('.mp3'):
                self.listWidget.insertItem(0, item.split('.mp3')[0])

        # ############### adding backward button
        self.backward_btn = QPushButton(self.frame)
        self.backward_btn.setIcon(QIcon('assets\\backward.png'))
        self.backward_btn.setIconSize(QSize(40, 40))
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
        self.movie = QMovie('assets\\visualizer.gif')

        # ########### adding volume mute button
        self.mute_btn = QPushButton(self.frame)
        self.mute_btn.setIcon(QIcon('assets\\vol.png'))
        self.mute_btn.setIconSize(QSize(30, 30))
        self.mute_btn.setGeometry(QtCore.QRect(340, 50, 30, 30))
        self.mute_btn.setStyleSheet('border-style: solid')

        # Adding music status
        self.status_bar = QStatusBar()
        self.status_bar.setStyleSheet('color:white')
        MainWindow.setStatusBar(self.status_bar)
        # adding volume slider
        self.vol_slider = QSlider(Qt.Horizontal, self.frame)
        self.vol_slider.setGeometry(QtCore.QRect(380, 50, 190, 30))
        self.vol_slider.setRange(0, 100)
        self.vol_slider.setValue(100)
        self.vol_slider.setStyleSheet(vol_slider_style)
        # adding lyrics button
        self.lyricsbutton = QPushButton(self.frame)
        self.lyricsbutton.setIcon(QIcon('assets\\lyrics.png'))
        self.lyricsbutton.setIconSize(QSize(30,30))
        self.lyricsbutton.setObjectName('Lyrics')
        self.lyricsbutton.setStyleSheet('border-style: solid')
        self.lyricsbutton.setGeometry(QtCore.QRect(300, 50, 30, 30))
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
        self.help_btn.triggered.connect(self.get_help)
        self.miniAction.triggered.connect(self.minimize)
        self.closeAction.triggered.connect(self.closewin)
        self.mute_btn.clicked.connect(self.muteUNMUTE)
        self.titlebar.mouseMoveEvent = self.mouseMoveEvent
        self.titlebar.mousePressEvent = self.mousePressEvent
        self.lyricsbutton.clicked.connect(self.show_lyrics)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MrPlayer"))
        self.groupBox.setTitle(_translate("MainWindow", "Songs"))

    def Play_Music(self):

        if self.listWidget.count() == 0:
            return
        self.label2.setMovie(self.movie)
        self.label.setMovie(self.movie)
        self.player.play()
        self.movie.start()

    def Pause_music(self):
        self.player.pause()
        self.label.clear()
        self.label2.clear()

    def MediaPosition_changed(self, position):

        if self.player.position() == self.player.duration():
            if self.player.duration() == 0:
                None
            else:
                self.movie.stop()
                self.label2.clear()
                self.label.clear()
        self.slider.setValue(position)
        dur = self.player.duration() / 1000
        conver = time.strftime('%M:%S', time.gmtime(dur))
        current_time = self.player.position() / 1000
        converted_time = time.strftime('%M:%S', time.gmtime(current_time))
        self.status_bar.showMessage(f'{converted_time} /{conver}     {self.listWidget.currentItem().text()} ')

    def MediaDuration_Changed(self, duration):
        self.slider.setRange(0, duration)

    def SetMedia_Position(self, position):
        self.player.setPosition(position)
        if self.player.position() == self.player.duration():
            self.movie.stop()

    def SetVolume(self, vol):
        self.player.setVolume(vol)

    def Setplayer_content(self):
        try:
            item = self.listWidget.currentItem()
            self.content = QtMultimedia.QMediaContent(QUrl.fromLocalFile(str(f'{path}\\{item.text()}.mp3')))
            self.player.setMedia(self.content)
            self.movie.stop()
            self.Play_Music()
        except:
            pass

    def next_song(self):

        try:
            if self.listWidget.currentRow() == self.listWidget.count() - 1:
                return
            else:
                self.listWidget.setCurrentRow(self.listWidget.currentRow() + 1)
                item = self.listWidget.currentItem()

                self.content = QtMultimedia.QMediaContent(QUrl.fromLocalFile(str(f'{path}\\{item.text()}.mp3')))
                self.player.setMedia(self.content)
                self.Pause_music()
                self.Play_Music()
        except Exception as e:
            print(e)

    def previous_song(self):
        try:
            if self.listWidget.currentRow() == 0:
                return

            self.listWidget.setCurrentRow(self.listWidget.currentRow() - 1)
            item = self.listWidget.currentItem()

            self.content = QtMultimedia.QMediaContent(QUrl.fromLocalFile(str(f'{path}\\{item.text()}.mp3')))
            self.player.setMedia(self.content)
            self.Pause_music()
            self.Play_Music()

        except:
            pass

    def get_help(self):
        self.helpWindow=Ui_HelpWindow()
        self.helpWindow.show()
    def minimize(self):
        MainWindow.showMinimized()

    def closewin(self):
        MainWindow.close()
        sys.exit()

    def muteUNMUTE(self):
        if self.player.isMuted():
            self.player.setMuted(False)
            self.mute_btn.setIcon(QIcon('assets/vol.png'))
        else:
            self.player.setMuted(True)
            self.mute_btn.setIcon(QIcon('assets/mute.png'))
    def mousePressEvent(self, event):  # +
        self.dragPos = event.globalPos()

    def mouseMoveEvent(self, event):  # !!!
        if event.buttons() == QtCore.Qt.LeftButton:
            MainWindow.move(MainWindow.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()
            
    def show_lyrics(self):
        self.LyricsWindow = Ui_LyricsWindow()
        self.LyricsWindow.show()
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
