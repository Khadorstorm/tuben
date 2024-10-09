import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QTableWidget, \
    QTableWidgetItem
from PyQt5.QtGui import QPixmap, QPainter, QPen, QColor
from PyQt5.QtCore import Qt, QPoint
from formantsynt import synthesize_vowel_sequence
import base64


img = "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"
tmp = open('vowel_chart.png', 'wb')
tmp.write(base64.b64decode(img))
tmp.close()


class MyWindow(QWidget):
    def __init__(self, imagePath):
        super().__init__()
        self.imagePath = imagePath
        self.setWindowTitle("Main Window with Image Click")
        self.originalPixmap = QPixmap(imagePath)
        self.initUI()

    def initUI(self):
        self.mainLayout = QHBoxLayout(self)

        # Table with additional columns for Name and Duration
        self.tableWidget = QTableWidget(0, 4)
        self.tableWidget.setHorizontalHeaderLabels(['F1', 'F2', 'Name', 'Duration'])
        self.addButton = QPushButton('Add Entry', self)
        self.delButton = QPushButton('Delete Entry', self)
        self.sumButton = QPushButton('Synthesize Trajectory', self)

        tableLayout = QVBoxLayout()
        tableLayout.addWidget(self.tableWidget)
        tableLayout.addWidget(self.addButton)
        tableLayout.addWidget(self.delButton)
        tableLayout.addWidget(self.sumButton)

        # Image layout
        imageLayout = QVBoxLayout()
        self.imageLabel = QLabel(self)
        self.imageLabel.setPixmap(self.originalPixmap.scaled(316, 215, Qt.KeepAspectRatio))
        self.imageLabel.setFixedSize(316, 215)
        self.addFromImageButton = QPushButton('Add from Image Click', self)
        imageLayout.addWidget(self.imageLabel)
        imageLayout.addWidget(self.addFromImageButton)

        self.mainLayout.addLayout(tableLayout)
        self.mainLayout.addLayout(imageLayout)

        self.addButton.clicked.connect(self.addEntry)
        self.delButton.clicked.connect(self.deleteEntry)
        self.addFromImageButton.clicked.connect(self.addClickPositionToTable)
        self.sumButton.clicked.connect(lambda: synthesize_vowel_sequence(fs=16000, formant_sequence=self.list_prepare()))

        self.resize(900, 600)

    def addClickPositionToTable(self):
        if self.lastClickPosition:
            x, y = self.lastClickPosition
            # manually calculated scaling
            x = int(2.111*x+248.27)
            y = int(-106/15*y+2300.666)
            self.tableWidget.insertRow(self.tableWidget.rowCount())
            self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 0, QTableWidgetItem(str(x)))
            self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 1, QTableWidgetItem(str(y)))
            self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 2, QTableWidgetItem("vowel"))
            self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 3, QTableWidgetItem("1"))
            self.lastClickPosition = None  # Reset after adding

    def addEntry(self):
        self.tableWidget.insertRow(self.tableWidget.rowCount())
        for i in range(4):
            if i == 2:  # Name column
                self.tableWidget.setItem(self.tableWidget.rowCount() - 1, i, QTableWidgetItem("vowel"))
            elif i == 3:  # Duration column
                self.tableWidget.setItem(self.tableWidget.rowCount() - 1, i, QTableWidgetItem("1"))
            else:
                self.tableWidget.setItem(self.tableWidget.rowCount() - 1, i, QTableWidgetItem("0"))

    def deleteEntry(self):
        selected_rows = set(index.row() for index in self.tableWidget.selectedIndexes())
        for row in sorted(selected_rows, reverse=True):
            self.tableWidget.removeRow(row)

    def list_prepare(self):
        traj_list = []
        for row in range(self.tableWidget.rowCount()):
            traj_list.append(([float(self.tableWidget.item(row, 0).text()),
                               float(self.tableWidget.item(row, 1).text())],
                              float(self.tableWidget.item(row, 3).text())))
        return traj_list

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            clickPosition = self.imageLabel.mapFromGlobal(self.mapToGlobal(event.pos()))
            if 0 <= clickPosition.x() < self.imageLabel.width() and 0 <= clickPosition.y() < self.imageLabel.height():
                x_ratio = self.originalPixmap.width() / self.imageLabel.width()
                y_ratio = self.originalPixmap.height() / self.imageLabel.height()
                scaled_x = int(clickPosition.x() * x_ratio)
                scaled_y = int(clickPosition.y() * y_ratio)
                self.lastClickPosition = (scaled_x, scaled_y)
                self.markPoint(scaled_x, scaled_y)

    def markPoint(self, x, y):
        pixmap = self.originalPixmap.copy()
        painter = QPainter(pixmap)
        pen = QPen(QColor(255, 0, 0))
        pen.setWidth(10)
        painter.setPen(pen)
        painter.drawPoint(QPoint(x, y))
        painter.end()
        self.imageLabel.setPixmap(pixmap.scaled(316, 215, Qt.KeepAspectRatio))


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Window")
        self.initUI()
        self.childWindow = MyWindow('vowel_chart.png')  # Create instance of your child window

    def initUI(self):
        layout = QVBoxLayout(self)
        openChildWindowButton = QPushButton('Open Child Window', self)
        setFeaturesButton = QPushButton('Set Features in Child Window', self)

        layout.addWidget(openChildWindowButton)
        layout.addWidget(setFeaturesButton)

        openChildWindowButton.clicked.connect(self.openChildWindow)
        setFeaturesButton.clicked.connect(self.setFeaturesInChild)

    def openChildWindow(self):
        self.childWindow.show()  # Show the child window in a non-blocking way

    def setFeaturesInChild(self):
        # Example of setting features in the child window
        # This can be adapted to set whatever data or features you need
        if self.childWindow.isVisible():
            self.childWindow.addEntry()  # Add an entry to the child window's table


def main():
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
