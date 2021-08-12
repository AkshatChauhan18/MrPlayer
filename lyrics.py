###################################################
# This is lyrics part of MrPlayer made in 2021    #
# Copyright (c) Akshat Chauhan                    #
###################################################

from PySide2 import QtCore, QtGui, QtWidgets
import lyricsgenius
import os.path

path = f"{os.path.expanduser('~')}\\.MrPlayer\\"
if os.path.exists(path):
    None
else:
    os.mkdir(path)

class LyricsThread(QtCore.QThread):
    lyrics_signal = QtCore.Signal(str)
    def __init__(self,song:str,artist:str):
        super(LyricsThread,self).__init__()
        self.song = song
        self.artist = artist
    def run(self):
        self.lyrics_signal.emit('loadingSHA25690')
        try:
            self.api_key = open(f"{path}\\api_key.txt").read()  
            genius = lyricsgenius.Genius(self.api_key)
            self.lyric = genius.search_song(
                self.song, self.artist)
            self.lyrics_signal.emit(str(self.lyric.lyrics))

        except Exception as e:
            self.lyrics_signal.emit(f"Something went wrong :\n{e}")



browser_v_slider = ("""
        QScrollBar:vertical {  
            border: 1px solid #aaa;            
            border-radius:2px;
            background:white;
            width:13px;
            margin: 0px 3px 0px 0px;
        }
        QScrollBar::handle:vertical {
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
            stop: 0 #3fe433,  stop: 1 #3febe8);
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
browser_h_slider = ("""
       QScrollBar:horizontal {
        border: 1px solid #aaa;            
        border-radius:2px;
  background-color: white;
    height: 13px;
    margin: 3px 0px 0px 0px;
 }

 QScrollBar::handle:horizontal {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
    stop: 0 #3fe433,  stop: 1 #3febe8);
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


class Ui_LyricsWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setObjectName("LyricsWindow")
        self.setFixedSize(474, 591)
        self.setStyleSheet("background-color:rgb(28, 27, 34)")
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.songBox = QtWidgets.QLineEdit(self.centralwidget)
        self.songBox.setGeometry(QtCore.QRect(10, 30, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.songBox.setFont(font)
        self.songBox.setStyleSheet("color:white")
        self.songBox.setObjectName("songBox")
        self.artistBox = QtWidgets.QLineEdit(self.centralwidget)
        self.artistBox.setGeometry(QtCore.QRect(180, 30, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.artistBox.setFont(font)
        self.artistBox.setStyleSheet("color:white")
        self.artistBox.setObjectName("artistBox")
        self.SearchButton = QtWidgets.QPushButton(self.centralwidget)
        self.SearchButton.setGeometry(QtCore.QRect(420, 30, 41, 31))
        self.SearchButton.setText("")
        self.SearchButton.setObjectName("SearchButton")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 70, 451, 481))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.dragPos = QtCore.QPoint()
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet(
            "border:5px solid  qlineargradient(x1: 0, y1: 0,    x2: 0, y2: 1,stop: 0 rgb(251, 108, 73), stop: 1 rgb(252, 30, 167));color:rgb(251, 108, 73)\n"
            " ")
        self.textBrowser.setOpenExternalLinks(True)
        self.textBrowser.setOpenLinks(True)
        self.textBrowser.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.textBrowser.setObjectName("textBrowser")
        self.setCentralWidget(self.centralwidget)
        self.textBrowser.openLinks()
        self.loaderUI = QtWidgets.QLabel(self.centralwidget)
        self.loaderUI.setGeometry(QtCore.QRect(125,170,200,200))
        self.loaderUI.setHidden(True)
        
        self.SearchButton.clicked.connect(self.getLyrics)
        QtCore.QMetaObject.connectSlotsByName(self)
        self.SearchButton.setIcon(QtGui.QIcon('assets/search.png'))
        # adding titlebar
        self.titlebar = QtWidgets.QToolBar()
        self.titlebar.setFloatable(False)
        self.titlebar.setMovable(False)
        self.addToolBar(self.titlebar)
        self.icon = QtWidgets.QLabel()
        self.icon.setPixmap(QtGui.QPixmap('assets/icon_small.png').scaled(25, 25))
        self.texticon = QtWidgets.QLabel('MrPlayer')
        self.texticon.setFont(QtGui.QFont('Arial', 14))
        self.texticon.setStyleSheet('color:gray')
        self.titlebar.addWidget(self.icon)
        self.titlebar.addWidget(self.texticon)
        self.spacer = QtWidgets.QWidget()
        self.spacer.setSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.titlebar.addWidget(self.spacer)
        self.titlebar.setStyleSheet(
            'background-color:#21252B ; border-top: 0px solid black')
        self.closeAction = QtWidgets.QAction()
        self.closeAction.setIcon(QtGui.QIcon('assets/close.png'))
        self.miniAction = QtWidgets.QAction()
        self.miniAction.setIcon(QtGui.QIcon('assets/minimize.png'))
        self.titlebar.addAction(self.closeAction)
        self.titlebar.addAction(self.miniAction)
        self.closeAction.triggered.connect(self.closewin)
        self.miniAction.triggered.connect(self.minimize)
        self.titlebar.mouseMoveEvent = self.mouseMoveEvent
        self.titlebar.mousePressEvent = self.mousePressEvent
        self.artistBox.setPlaceholderText("Artist")
        self.songBox.setPlaceholderText("Song")
        self.textBrowser.setHtml(
            "<!DOCTYPE HTML>\n"
            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
            "p, li { white-space: pre-wrap; }\n"
            "</style></head><body style=\" font-family:\'Gabriola\'; font-size:18pt; font-weight:400; font-style:normal;\">\n"
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p></body></html>")
        self.textBrowser.horizontalScrollBar().setStyleSheet(browser_h_slider)
        self.textBrowser.verticalScrollBar().setStyleSheet(browser_v_slider)
        self.show()

    def getLyrics(self):
        new_thread = LyricsThread(self.songBox.text(),self.artistBox.text())
        new_thread.lyrics_signal.connect(self.update_text_browser)
        self.worker = new_thread
        self.worker.start()

    def minimize(self):
        self.showMinimized()

    def closewin(self):
        self.close()

    def mousePressEvent(self, event):  
        self.dragPos = event.globalPos()

    def mouseMoveEvent(self, event): 
        if event.buttons() == QtCore.Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()

    def update_text_browser(self,text):
        if text == "loadingSHA25690":
            self.loaderUI.setHidden(False)
            self.loading_gif = QtGui.QMovie('assets/loader.gif')
            self.loading_gif.setScaledSize(QtCore.QSize(200,200))
            self.loaderUI.setMovie(self.loading_gif)
            self.loading_gif.start()
        else:
            self.loading_gif.stop()
            self.loaderUI.setHidden(True)
            self.textBrowser.setText(text)    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    lyricsWindow = Ui_LyricsWindow()
    sys.exit(app.exec_())
