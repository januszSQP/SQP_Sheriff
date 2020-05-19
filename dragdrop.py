from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *

'''
Class for managing drag & drop function for Show:poster
and Shot:thumbnails
'''
class DragAndDrop(QLabel):
    def __init__(self):
        super().__init__()

        # self.setAlignment(Qt.AlignCenter)
        # self.setText('\n\n Drop Image Here \n\n')
        # self.setStyleSheet('''
        #     QLabel{
        #         border: 4px dashed #aaa
        #     }
        # ''')

    def setPixmap(self, image):
        super().setPixmap(image)