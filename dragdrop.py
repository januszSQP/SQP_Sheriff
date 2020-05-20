from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *

'''
Class for managing drag & drop function for Show:poster
and Shot:thumbnails
'''


class DragAndDrop(QLabel):
    def __init__(self):
        super(DragAndDrop, self).__init__()
        self.setAcceptDrops(True)
        self.setAlignment(Qt.AlignCenter)
        self.setText('\n\n Drop Image Here \n\n')
        self.setStyleSheet('''
            QLabel{
                border: 2px dashed #03f1c2
            }
        ''')

        self.thumb_path = ''


    def returnImagePath(self):
        return self.thumb_path


    def dragEnterEvent(self, event):
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        data = event.mimeData()
        if data.urls():
            event.setDropAction(Qt.CopyAction)
            file_path = event.mimeData().urls()[0].toLocalFile()
            pixmap = QPixmap(file_path).scaledToHeight(180, Qt.SmoothTransformation)
            self.setPixmap(pixmap)
            self.thumb_path = file_path
            event.accept()
        else:
            event.ignore()

