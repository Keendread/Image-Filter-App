# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.11.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGraphicsView, QHBoxLayout,
    QLabel, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QSlider, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.setWindowIcon(QIcon("path/to/icon.png"))   # TODO
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.imageInput = QHBoxLayout()
        self.imageInput.setObjectName(u"imageInput")
        self.selectImageButton = QPushButton(self.centralwidget)
        self.selectImageButton.setObjectName(u"selectImageButton")

        self.imageInput.addWidget(self.selectImageButton)

        self.takeImageButton = QPushButton(self.centralwidget)
        self.takeImageButton.setObjectName(u"takeImageButton")

        self.imageInput.addWidget(self.takeImageButton)


        self.verticalLayout.addLayout(self.imageInput)

        self.filterSelection = QHBoxLayout()
        self.filterSelection.setObjectName(u"filterSelection")
        self.filterText = QLabel(self.centralwidget)
        self.filterText.setObjectName(u"filterText")
        self.filterText.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.filterSelection.addWidget(self.filterText)

        self.filterSelector = QComboBox(self.centralwidget)
        self.filterSelector.addItem("")
        self.filterSelector.addItem("")
        self.filterSelector.addItem("")
        self.filterSelector.setObjectName(u"filterSelector")

        self.filterSelection.addWidget(self.filterSelector)


        self.verticalLayout.addLayout(self.filterSelection)

        self.kernelSize = QVBoxLayout()
        self.kernelSize.setObjectName(u"kernelSize")
        self.kernelText = QLabel(self.centralwidget)
        self.kernelText.setObjectName(u"kernelText")
        font = QFont()
        font.setHintingPreference(QFont.PreferDefaultHinting)
        self.kernelText.setFont(font)
        self.kernelText.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.kernelText.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.kernelSize.addWidget(self.kernelText)

        self.kernelSizeSlider = QSlider(self.centralwidget)
        self.kernelSizeSlider.setObjectName(u"kernelSizeSlider")
        self.kernelSizeSlider.setMinimum(1)
        self.kernelSizeSlider.setMaximum(15)
        self.kernelSizeSlider.setSingleStep(2)
        self.kernelSizeSlider.setOrientation(Qt.Orientation.Horizontal)
        self.kernelSizeSlider.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.kernelSizeSlider.setTickInterval(2)

        self.kernelSize.addWidget(self.kernelSizeSlider)


        self.verticalLayout.addLayout(self.kernelSize)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.graphicsViewOriginal = QGraphicsView(self.centralwidget)
        self.graphicsViewOriginal.setObjectName(u"graphicsViewOriginal")

        self.horizontalLayout_2.addWidget(self.graphicsViewOriginal)

        self.graphicsViewFilter = QGraphicsView(self.centralwidget)
        self.graphicsViewFilter.setObjectName(u"graphicsViewFilter")

        self.horizontalLayout_2.addWidget(self.graphicsViewFilter)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Image Filter App", None))
        self.selectImageButton.setText(QCoreApplication.translate("MainWindow", u"Select Image", None))
        self.takeImageButton.setText(QCoreApplication.translate("MainWindow", u"Take a Picture", None))
        self.filterText.setText(QCoreApplication.translate("MainWindow", u"Filter", None))
        self.filterSelector.setItemText(0, QCoreApplication.translate("MainWindow", u"Grayscale", None))
        self.filterSelector.setItemText(1, QCoreApplication.translate("MainWindow", u"Gaussian Blur", None))
        self.filterSelector.setItemText(2, QCoreApplication.translate("MainWindow", u"Canny Edge", None))

        self.kernelText.setText(QCoreApplication.translate("MainWindow", u"Kernel", None))
    # retranslateUi

