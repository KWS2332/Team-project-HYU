from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QPixmap
import sys
import os

from ui_Test1 import Ui_MainWindow
from ui_Test2 import Ui_MainWindow2
from ui_Test3 import Ui_MainWindow3


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        def load_image(image_file, label):
            resources_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'resources')
            image_path = os.path.join(resources_dir, image_file)
            pixmap = QPixmap(image_path)
            label.setPixmap(pixmap)

        load_image('trussback1.png', self.ui.label)
        load_image('6313503-200.png', self.ui.label_24)
        load_image('5469180-200.png', self.ui.label_25)
        load_image('2018888-200.png', self.ui.label_26)

        self.ui.pushButton.clicked.connect(self.on_pushButton_clicked)

    def on_pushButton_clicked(self):
        self.hide()
        self.window2 = MainWindow2()
        self.window2.show()


class MainWindow2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui2 = Ui_MainWindow2()
        self.ui2.setupUi(self)

        def load_image(image_file, label):
            resources_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'resources')
            image_path = os.path.join(resources_dir, image_file)
            pixmap = QPixmap(image_path)
            label.setPixmap(pixmap)

        load_image('truss11.jpg', self.ui2.label)
        load_image('truss2.jpg', self.ui2.label_2)
        load_image('truss3.jpg', self.ui2.label_3)
        load_image('truss1.png', self.ui2.label_23)
        load_image('DT2.jpg', self.ui2.label_21)
        load_image('DT.png', self.ui2.label_20)

        self.ui2.pushButton.clicked.connect(self.on_pushButton_clicked)

    def on_pushButton_clicked(self):
        self.hide()
        self.window3 = MainWindow3()
        self.window3.show()


class MainWindow3(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui3 = Ui_MainWindow3()
        self.ui3.setupUi(self)

        # load_image 함수를 클래스 내에 정의합니다.
        def load_image(image_file, label):
            resources_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'resources')
            image_path = os.path.join(resources_dir, image_file)
            pixmap = QPixmap(image_path)
            label.setPixmap(pixmap)

        # 이미지 로드 및 표시
        load_image('DT3.jpg', self.ui3.label_22)  # QLabel 이름이 'label_22'이라고 가정합니다.


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
