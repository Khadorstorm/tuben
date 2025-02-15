# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_main.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtWidgets


class Ui_TubeN(object):
    def setupUi(self, TubeN):
        TubeN.setObjectName("TubeN")
        TubeN.resize(1499, 800)
        self.centralwidget = QtWidgets.QWidget(TubeN)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1500, 800))
        self.frame.setStyleSheet("background-color: rgb(234, 233, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.illustration = QtWidgets.QGraphicsView(self.frame)
        self.illustration.setGeometry(QtCore.QRect(400, 30, 700, 360))
        self.illustration.setObjectName("illustration")
        self.pushButton_add = QtWidgets.QPushButton(self.frame)
        self.pushButton_add.setGeometry(QtCore.QRect(110, 30, 70, 50))
        self.pushButton_add.setStyleSheet("QPushButton{\n"
"    font: 10pt \"Arial\";\n"
"}\n"
"QPushButton::hover{\n"
"    font: 87 10pt \"Arial Black\";\n"
"    background-color: rgb(255, 170, 255);\n"
"}")
        self.pushButton_add.setObjectName("pushButton_add")
        self.pushButton_sound = QtWidgets.QPushButton(self.frame)
        self.pushButton_sound.setGeometry(QtCore.QRect(170, 255, 150, 50))
        self.pushButton_sound.setStyleSheet("QPushButton{\n"
"    font: 10pt \"Arial\";\n"
"}\n"
"QPushButton::hover{\n"
"    font: 87 10pt \"Arial Black\";\n"
"    background-color: rgb(255, 170, 255);\n"
"}")
        self.pushButton_sound.setObjectName("pushButton_sound")
        self.pushButton_illustrate = QtWidgets.QPushButton(self.frame)
        self.pushButton_illustrate.setGeometry(QtCore.QRect(170, 330, 150, 50))
        self.pushButton_illustrate.setStyleSheet("QPushButton{\n"
"    font: 10pt \"Arial\";\n"
"}\n"
"QPushButton::hover{\n"
"    font: 87 10pt \"Arial Black\";\n"
"    background-color: rgb(255, 170, 255);\n"
"}")
        self.pushButton_illustrate.setObjectName("pushButton_illustrate")
        self.pushButton_remove = QtWidgets.QPushButton(self.frame)
        self.pushButton_remove.setGeometry(QtCore.QRect(205, 30, 70, 50))
        self.pushButton_remove.setStyleSheet("QPushButton{\n"
"    font: 10pt \"Arial\";\n"
"}\n"
"QPushButton::hover{\n"
"    font: 87 10pt \"Arial Black\";\n"
"    background-color: rgb(255, 170, 255);\n"
"}")
        self.pushButton_remove.setObjectName("pushButton_remove")
        self.play_audio = QtWidgets.QCommandLinkButton(self.frame)
        self.play_audio.setGeometry(QtCore.QRect(75, 260, 75, 40))
        self.play_audio.setObjectName("play_audio")
        self.pushButton_alter = QtWidgets.QPushButton(self.frame)
        self.pushButton_alter.setGeometry(QtCore.QRect(300, 30, 70, 50))
        self.pushButton_alter.setStyleSheet("QPushButton{\n"
"    font: 10pt \"Arial\";\n"
"}\n"
"QPushButton::hover{\n"
"    font: 87 10pt \"Arial Black\";\n"
"    background-color: rgb(255, 170, 255);\n"
"}")
        self.pushButton_alter.setObjectName("pushButton_alter")
        self.input_information_output = QtWidgets.QTextBrowser(self.frame)
        self.input_information_output.setGeometry(QtCore.QRect(1130, 80, 275, 310))
        self.input_information_output.setObjectName("input_information_output")
        self.input_sign = QtWidgets.QLabel(self.frame)
        self.input_sign.setGeometry(QtCore.QRect(1170, 30, 260, 35))
        self.input_sign.setStyleSheet("QLabel:{\n"
"    font: 10pt \"Arial\";\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.input_sign.setObjectName("input_sign")
        self.pushButton_scale = QtWidgets.QPushButton(self.frame)
        self.pushButton_scale.setGeometry(QtCore.QRect(170, 105, 150, 50))
        self.pushButton_scale.setStyleSheet("QPushButton{\n"
"    font: 10pt \"Arial\";\n"
"}\n"
"QPushButton::hover{\n"
"    font: 87 10pt \"Arial Black\";\n"
"    background-color: rgb(255, 170, 255);\n"
"}")
        self.pushButton_scale.setObjectName("pushButton_scale")
        self.example_a = QtWidgets.QPushButton(self.frame)
        self.example_a.setGeometry(QtCore.QRect(145, 480, 60, 50))
        self.example_a.setStyleSheet("QPushButton{\n"
"    font: 10pt \"Arial\";\n"
"}\n"
"QPushButton::hover{\n"
"    font: 87 10pt \"Arial Black\";\n"
"    background-color: rgb(255, 170, 255);\n"
"}")
        self.example_a.setObjectName("example_a")
        self.pushButton_obliviate = QtWidgets.QPushButton(self.frame)
        self.pushButton_obliviate.setGeometry(QtCore.QRect(170, 555, 150, 50))
        self.pushButton_obliviate.setStyleSheet("QPushButton{\n"
"    font: 10pt \"Arial\";\n"
"}\n"
"QPushButton::hover{\n"
"    font: 87 10pt \"Arial Black\";\n"
"    background-color: rgb(255, 170, 255);\n"
"}")
        self.pushButton_obliviate.setObjectName("pushButton_obliviate")
        self.doubleSpinBox_scale = QtWidgets.QDoubleSpinBox(self.frame)
        self.doubleSpinBox_scale.setGeometry(QtCore.QRect(70, 110, 75, 40))
        self.doubleSpinBox_scale.setObjectName("doubleSpinBox_scale")
        self.pushButton_3d = QtWidgets.QPushButton(self.frame)
        self.pushButton_3d.setGeometry(QtCore.QRect(170, 405, 150, 50))
        self.pushButton_3d.setStyleSheet("QPushButton{\n"
"    font: 10pt \"Arial\";\n"
"}\n"
"QPushButton::hover{\n"
"    font: 87 8pt \"Arial Black\";\n"
"    background-color: rgb(255, 170, 255);\n"
"}")
        self.pushButton_3d.setObjectName("pushButton_3d")
        self.example_i = QtWidgets.QPushButton(self.frame)
        self.example_i.setGeometry(QtCore.QRect(225, 480, 60, 50))
        self.example_i.setStyleSheet("QPushButton{\n"
"    font: 10pt \"Arial\";\n"
"}\n"
"QPushButton::hover{\n"
"    font: 87 10pt \"Arial Black\";\n"
"    background-color: rgb(255, 170, 255);\n"
"}")
        self.example_i.setObjectName("example_i")
        self.example_u = QtWidgets.QPushButton(self.frame)
        self.example_u.setGeometry(QtCore.QRect(305, 480, 60, 50))
        self.example_u.setStyleSheet("QPushButton{\n"
"    font: 10pt \"Arial\";\n"
"}\n"
"QPushButton::hover{\n"
"    font: 87 10pt \"Arial Black\";\n"
"    background-color: rgb(255, 170, 255);\n"
"}")
        self.example_u.setObjectName("example_u")
        self.pushButton_trajectory = QtWidgets.QPushButton(self.frame)
        self.pushButton_trajectory.setGeometry(QtCore.QRect(170, 630, 150, 50))
        self.pushButton_trajectory.setStyleSheet("QPushButton{\n"
"    font: 10pt \"Arial\";\n"
"}\n"
"QPushButton::hover{\n"
"    font: 87 10pt \"Arial Black\";\n"
"    background-color: rgb(255, 170, 255);\n"
"}")
        self.pushButton_trajectory.setObjectName("pushButton_trajectory")
        self.graphics_formants = QtWidgets.QGraphicsView(self.frame)
        self.graphics_formants.setGeometry(QtCore.QRect(400, 405, 1005, 350))
        self.graphics_formants.setObjectName("graphics_formants")
        self.pushButton_save = QtWidgets.QPushButton(self.frame)
        self.pushButton_save.setGeometry(QtCore.QRect(170, 180, 150, 50))
        self.pushButton_save.setStyleSheet("QPushButton{\n"
"    font: 10pt \"Arial\";\n"
"}\n"
"QPushButton::hover{\n"
"    font: 87 10pt \"Arial Black\";\n"
"    background-color: rgb(255, 170, 255);\n"
"}")
        self.pushButton_save.setObjectName("pushButton_save")
        self.pushButton_explore = QtWidgets.QPushButton(self.frame)
        self.pushButton_explore.setGeometry(QtCore.QRect(170, 705, 150, 50))
        self.pushButton_explore.setStyleSheet("QPushButton{\n"
"    font: 10pt \"Arial\";\n"
"}\n"
"QPushButton::hover{\n"
"    font: 87 10pt \"Arial Black\";\n"
"    background-color: rgb(255, 170, 255);\n"
"}")
        self.pushButton_explore.setObjectName("pushButton_explore")
        TubeN.setCentralWidget(self.centralwidget)

        self.retranslateUi(TubeN)
        QtCore.QMetaObject.connectSlotsByName(TubeN)

    def retranslateUi(self, TubeN):
        _translate = QtCore.QCoreApplication.translate
        TubeN.setWindowTitle(_translate("TubeN", "MainWindow"))
        self.pushButton_add.setText(_translate("TubeN", "Add"))
        self.pushButton_sound.setText(_translate("TubeN", "Generate Sound"))
        self.pushButton_illustrate.setText(_translate("TubeN", "Illustrate"))
        self.pushButton_remove.setText(_translate("TubeN", "Remove"))
        self.play_audio.setText(_translate("TubeN", "play"))
        self.pushButton_alter.setText(_translate("TubeN", "Alter"))
        self.input_sign.setText(_translate("TubeN", "Operational Information"))
        self.pushButton_scale.setText(_translate("TubeN", "Scale"))
        self.example_a.setText(_translate("TubeN", "/a/"))
        self.pushButton_obliviate.setText(_translate("TubeN", "Obliviate"))
        self.pushButton_3d.setText(_translate("TubeN", "3D File"))
        self.example_i.setText(_translate("TubeN", "/i/"))
        self.example_u.setText(_translate("TubeN", "/u/"))
        self.pushButton_trajectory.setText(_translate("TubeN", "Trajectory"))
        self.pushButton_save.setText(_translate("TubeN", "Save"))
        self.pushButton_explore.setText(_translate("TubeN", "Explore"))
