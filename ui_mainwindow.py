# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QLayout, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_SudokuGraphia(object):
    def setupUi(self, SudokuGraphia):
        if not SudokuGraphia.objectName():
            SudokuGraphia.setObjectName(u"SudokuGraphia")
        SudokuGraphia.setWindowModality(Qt.WindowModal)
        SudokuGraphia.setEnabled(True)
        SudokuGraphia.resize(955, 600)
        SudokuGraphia.setMinimumSize(QSize(955, 600))
        SudokuGraphia.setMaximumSize(QSize(955, 600))
        icon = QIcon(QIcon.fromTheme(u"battery"))
        SudokuGraphia.setWindowIcon(icon)
        SudokuGraphia.setStyleSheet(u"* {\n"
"	font: 14pt \"Sans Serif\";\n"
"}\n"
"QLineEdit {\n"
"	padding: 0px;\n"
"	border: none;\n"
"	font: 19pt \"Sans Serif\";\n"
"	background-color: rgb(237, 250, 255);\n"
"}\n"
"QLineEdit[echoMode=\"2\"] {\n"
"    lineedit-password-character: 9679;\n"
"}\n"
"QMainWindow {\n"
"	background-color: rgb(43, 67, 83);\n"
"}\n"
"QPushButton {\n"
"	padding: 7px;\n"
"	border-radius:9px;\n"
"	font: 14pt \"Sans Serif\";\n"
"	font-weight:600;\n"
"}\n"
"QGroupBox {\n"
"	border: 1px solid #76797C;\n"
"    border-radius: 2px;\n"
"    margin-top: 20px;\n"
"	padding: 5px;\n"
"}\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    padding-top: 10px;\n"
"}\n"
"QFrame > QPushButton {\n"
"	color: rgb(192, 236, 234);\n"
"}\n"
"QGroupBox > QPushButton {\n"
"	background-color: rgb(43, 67, 83);\n"
"	color: rgb(192, 236, 234);\n"
"}\n"
"QGroupBox{\n"
"	border-color: rgb(232, 99, 10);\n"
"}\n"
"QGroupBox:title {\n"
"	color: r"
                        "gb(232, 99, 10);\n"
"}\n"
"#frame_carre_1, #frame_carre_3, #frame_carre_5, #frame_carre_7, #frame_carre_9 {\n"
"	background-color: #e7f5fe;\n"
"}\n"
"#frame_carre_2 , #frame_carre_4, #frame_carre_6, #frame_carre_8{\n"
"background-color: rgb(93, 140, 176);\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"#frame_carre_2 > QLineEdit , #frame_carre_4  > QLineEdit, #frame_carre_6  > QLineEdit, #frame_carre_8  > QLineEdit{\n"
"	background-color: rgba(0, 0, 255, 0.06);\n"
"}\n"
"#trad_part {\n"
"	border: 1px solid #76797C;\n"
"	border-color: rgb(232, 99, 10);\n"
"    border-radius: 2px;\n"
"}\n"
"#lineEdit {\n"
"	background: transparent;\n"
"	color:  rgb(232, 99, 10);\n"
"}")
        SudokuGraphia.setProperty("setContentsMargins", 0)
        SudokuGraphia.setProperty("horizontalSpacing", 0)
        self.centralwidget = QWidget(SudokuGraphia)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(-10, 0, 481, 600))
        self.frame.setMinimumSize(QSize(0, 600))
        self.frame.setLayoutDirection(Qt.LeftToRight)
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet(u"QFrame {\n"
"	border-top-right-radius: 25px;\n"
"	border-bottom-right-radius: 15px;\n"
"	background-color: rgb(192, 236, 234);\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.verticalLayout.setContentsMargins(22, -1, 13, -1)
        self.groupBox_algo = QGroupBox(self.frame)
        self.groupBox_algo.setObjectName(u"groupBox_algo")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_algo.sizePolicy().hasHeightForWidth())
        self.groupBox_algo.setSizePolicy(sizePolicy)
        self.groupBox_algo.setLayoutDirection(Qt.LeftToRight)
        self.groupBox_algo.setStyleSheet(u"")
        self.groupBox_algo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.groupBox_algo.setFlat(False)
        self.groupBox_algo.setCheckable(False)
        self.horizontalLayout = QHBoxLayout(self.groupBox_algo)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.powel = QPushButton(self.groupBox_algo)
        self.powel.setObjectName(u"powel")
        self.powel.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.powel)

        self.bck = QPushButton(self.groupBox_algo)
        self.bck.setObjectName(u"bck")
        self.bck.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.bck)

        self.gl = QPushButton(self.groupBox_algo)
        self.gl.setObjectName(u"gl")
        self.gl.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.gl)

        self.encourt = QPushButton(self.groupBox_algo)
        self.encourt.setObjectName(u"encourt")
        self.encourt.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.encourt)


        self.verticalLayout.addWidget(self.groupBox_algo, 0, Qt.AlignHCenter)

        self.groupBox_2 = QGroupBox(self.frame)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMaximumSize(QSize(413, 16777215))
        self.groupBox_2.setAutoFillBackground(False)
        self.groupBox_2.setStyleSheet(u"")
        self.groupBox_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.groupBox_2.setFlat(False)
        self.groupBox_2.setCheckable(False)
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.desc = QTextEdit(self.groupBox_2)
        self.desc.setObjectName(u"desc")
        self.desc.setMinimumSize(QSize(312, 0))
        self.desc.setStyleSheet(u"QScrollBar:vertical {\n"
"    background: lightgray;\n"
"    width: 10px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background:  rgb(232, 99, 10);\n"
"    min-height: 20px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    background: lightgray;\n"
"    height: 10px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    background: lightgray;\n"
"    height: 10px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}")
        self.desc.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.desc)


        self.verticalLayout.addWidget(self.groupBox_2, 0, Qt.AlignHCenter)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QSize(420, 0))
        self.frame_2.setStyleSheet(u"QPushButton {\n"
"	width: 100px;	\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.reset = QPushButton(self.frame_2)
        self.reset.setObjectName(u"reset")
        self.reset.setCursor(QCursor(Qt.PointingHandCursor))
        self.reset.setStyleSheet(u"background-color: rgb(43, 67, 83);")

        self.gridLayout.addWidget(self.reset, 1, 1, 1, 1)

        self.generate = QPushButton(self.frame_2)
        self.generate.setObjectName(u"generate")
        self.generate.setCursor(QCursor(Qt.PointingHandCursor))
        self.generate.setStyleSheet(u"background-color: rgb(43, 67, 83);\n"
"")

        self.gridLayout.addWidget(self.generate, 1, 0, 1, 1)

        self.resolveButton = QPushButton(self.frame_2)
        self.resolveButton.setObjectName(u"resolveButton")
        self.resolveButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.resolveButton.setStyleSheet(u"background-color: rgb(43, 67, 83);")

        self.gridLayout.addWidget(self.resolveButton, 1, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 0, 1, 1, 1)


        self.verticalLayout.addWidget(self.frame_2, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(500, 60, 430, 418))
        self.groupBox_3.setStyleSheet(u"")
        self.groupBox_3.setAlignment(Qt.AlignCenter)
        self.groupBox_3.setFlat(False)
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_sudo = QFrame(self.groupBox_3)
        self.frame_sudo.setObjectName(u"frame_sudo")
        self.frame_sudo.setMaximumSize(QSize(400, 16777215))
        font = QFont()
        font.setFamilies([u"Sans Serif"])
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setHintingPreference(QFont.PreferDefaultHinting)
        self.frame_sudo.setFont(font)
        self.frame_sudo.setContextMenuPolicy(Qt.NoContextMenu)
        self.frame_sudo.setLayoutDirection(Qt.LeftToRight)
        self.frame_sudo.setStyleSheet(u"")
        self.gridLayout_2 = QGridLayout(self.frame_sudo)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_carre_8 = QFrame(self.frame_sudo)
        self.frame_carre_8.setObjectName(u"frame_carre_8")
        self.frame_carre_8.setStyleSheet(u"")
        self.frame_carre_8.setFrameShape(QFrame.StyledPanel)
        self.frame_carre_8.setFrameShadow(QFrame.Raised)
        self.gridLayout_28 = QGridLayout(self.frame_carre_8)
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.l59 = QLineEdit(self.frame_carre_8)
        self.l59.setObjectName(u"l59")
        self.l59.setMaxLength(1)
        self.l59.setAlignment(Qt.AlignCenter)

        self.gridLayout_28.addWidget(self.l59, 0, 1, 1, 1)

        self.l77 = QLineEdit(self.frame_carre_8)
        self.l77.setObjectName(u"l77")
        self.l77.setEnabled(True)
        self.l77.setMaxLength(1)
        self.l77.setAlignment(Qt.AlignCenter)

        self.gridLayout_28.addWidget(self.l77, 2, 1, 1, 1)

        self.l58 = QLineEdit(self.frame_carre_8)
        self.l58.setObjectName(u"l58")
        self.l58.setMaxLength(1)
        self.l58.setAlignment(Qt.AlignCenter)

        self.gridLayout_28.addWidget(self.l58, 0, 0, 1, 1)

        self.l69 = QLineEdit(self.frame_carre_8)
        self.l69.setObjectName(u"l69")
        self.l69.setMaxLength(1)
        self.l69.setAlignment(Qt.AlignCenter)

        self.gridLayout_28.addWidget(self.l69, 1, 2, 1, 1)

        self.l78 = QLineEdit(self.frame_carre_8)
        self.l78.setObjectName(u"l78")
        self.l78.setMaxLength(1)
        self.l78.setAlignment(Qt.AlignCenter)

        self.gridLayout_28.addWidget(self.l78, 2, 2, 1, 1)

        self.l67 = QLineEdit(self.frame_carre_8)
        self.l67.setObjectName(u"l67")
        self.l67.setMaxLength(1)
        self.l67.setAlignment(Qt.AlignCenter)

        self.gridLayout_28.addWidget(self.l67, 1, 0, 1, 1)

        self.l60 = QLineEdit(self.frame_carre_8)
        self.l60.setObjectName(u"l60")
        self.l60.setMaxLength(1)
        self.l60.setAlignment(Qt.AlignCenter)

        self.gridLayout_28.addWidget(self.l60, 0, 2, 1, 1)

        self.l68 = QLineEdit(self.frame_carre_8)
        self.l68.setObjectName(u"l68")
        self.l68.setMaxLength(1)
        self.l68.setAlignment(Qt.AlignCenter)

        self.gridLayout_28.addWidget(self.l68, 1, 1, 1, 1)

        self.l76 = QLineEdit(self.frame_carre_8)
        self.l76.setObjectName(u"l76")
        self.l76.setMaxLength(1)
        self.l76.setAlignment(Qt.AlignCenter)

        self.gridLayout_28.addWidget(self.l76, 2, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame_carre_8, 2, 1, 1, 1)

        self.frame_carre_6 = QFrame(self.frame_sudo)
        self.frame_carre_6.setObjectName(u"frame_carre_6")
        self.frame_carre_6.setStyleSheet(u"")
        self.frame_carre_6.setFrameShape(QFrame.StyledPanel)
        self.frame_carre_6.setFrameShadow(QFrame.Raised)
        self.gridLayout_26 = QGridLayout(self.frame_carre_6)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.l35 = QLineEdit(self.frame_carre_6)
        self.l35.setObjectName(u"l35")
        self.l35.setMaxLength(1)
        self.l35.setAlignment(Qt.AlignCenter)

        self.gridLayout_26.addWidget(self.l35, 0, 1, 1, 1)

        self.l53 = QLineEdit(self.frame_carre_6)
        self.l53.setObjectName(u"l53")
        self.l53.setEnabled(True)
        self.l53.setMaxLength(1)
        self.l53.setAlignment(Qt.AlignCenter)

        self.gridLayout_26.addWidget(self.l53, 2, 1, 1, 1)

        self.l34 = QLineEdit(self.frame_carre_6)
        self.l34.setObjectName(u"l34")
        self.l34.setMaxLength(1)
        self.l34.setAlignment(Qt.AlignCenter)

        self.gridLayout_26.addWidget(self.l34, 0, 0, 1, 1)

        self.l45 = QLineEdit(self.frame_carre_6)
        self.l45.setObjectName(u"l45")
        self.l45.setMaxLength(1)
        self.l45.setAlignment(Qt.AlignCenter)

        self.gridLayout_26.addWidget(self.l45, 1, 2, 1, 1)

        self.l54 = QLineEdit(self.frame_carre_6)
        self.l54.setObjectName(u"l54")
        self.l54.setMaxLength(1)
        self.l54.setAlignment(Qt.AlignCenter)

        self.gridLayout_26.addWidget(self.l54, 2, 2, 1, 1)

        self.l43 = QLineEdit(self.frame_carre_6)
        self.l43.setObjectName(u"l43")
        self.l43.setMaxLength(1)
        self.l43.setAlignment(Qt.AlignCenter)

        self.gridLayout_26.addWidget(self.l43, 1, 0, 1, 1)

        self.l36 = QLineEdit(self.frame_carre_6)
        self.l36.setObjectName(u"l36")
        self.l36.setMaxLength(1)
        self.l36.setAlignment(Qt.AlignCenter)

        self.gridLayout_26.addWidget(self.l36, 0, 2, 1, 1)

        self.l44 = QLineEdit(self.frame_carre_6)
        self.l44.setObjectName(u"l44")
        self.l44.setMaxLength(1)
        self.l44.setAlignment(Qt.AlignCenter)

        self.gridLayout_26.addWidget(self.l44, 1, 1, 1, 1)

        self.l52 = QLineEdit(self.frame_carre_6)
        self.l52.setObjectName(u"l52")
        self.l52.setMaxLength(1)
        self.l52.setAlignment(Qt.AlignCenter)

        self.gridLayout_26.addWidget(self.l52, 2, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame_carre_6, 1, 2, 1, 1)

        self.frame_carre_5 = QFrame(self.frame_sudo)
        self.frame_carre_5.setObjectName(u"frame_carre_5")
        self.frame_carre_5.setStyleSheet(u"")
        self.frame_carre_5.setFrameShape(QFrame.StyledPanel)
        self.frame_carre_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_25 = QGridLayout(self.frame_carre_5)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.l32 = QLineEdit(self.frame_carre_5)
        self.l32.setObjectName(u"l32")
        self.l32.setMaxLength(1)
        self.l32.setAlignment(Qt.AlignCenter)

        self.gridLayout_25.addWidget(self.l32, 0, 1, 1, 1)

        self.l50 = QLineEdit(self.frame_carre_5)
        self.l50.setObjectName(u"l50")
        self.l50.setEnabled(True)
        self.l50.setMaxLength(1)
        self.l50.setAlignment(Qt.AlignCenter)

        self.gridLayout_25.addWidget(self.l50, 2, 1, 1, 1)

        self.l31 = QLineEdit(self.frame_carre_5)
        self.l31.setObjectName(u"l31")
        self.l31.setMaxLength(1)
        self.l31.setAlignment(Qt.AlignCenter)

        self.gridLayout_25.addWidget(self.l31, 0, 0, 1, 1)

        self.l42 = QLineEdit(self.frame_carre_5)
        self.l42.setObjectName(u"l42")
        self.l42.setMaxLength(1)
        self.l42.setAlignment(Qt.AlignCenter)

        self.gridLayout_25.addWidget(self.l42, 1, 2, 1, 1)

        self.l51 = QLineEdit(self.frame_carre_5)
        self.l51.setObjectName(u"l51")
        self.l51.setMaxLength(1)
        self.l51.setAlignment(Qt.AlignCenter)

        self.gridLayout_25.addWidget(self.l51, 2, 2, 1, 1)

        self.l40 = QLineEdit(self.frame_carre_5)
        self.l40.setObjectName(u"l40")
        self.l40.setMaxLength(1)
        self.l40.setAlignment(Qt.AlignCenter)

        self.gridLayout_25.addWidget(self.l40, 1, 0, 1, 1)

        self.l33 = QLineEdit(self.frame_carre_5)
        self.l33.setObjectName(u"l33")
        self.l33.setMaxLength(1)
        self.l33.setAlignment(Qt.AlignCenter)

        self.gridLayout_25.addWidget(self.l33, 0, 2, 1, 1)

        self.l41 = QLineEdit(self.frame_carre_5)
        self.l41.setObjectName(u"l41")
        self.l41.setMaxLength(1)
        self.l41.setAlignment(Qt.AlignCenter)

        self.gridLayout_25.addWidget(self.l41, 1, 1, 1, 1)

        self.l49 = QLineEdit(self.frame_carre_5)
        self.l49.setObjectName(u"l49")
        self.l49.setMaxLength(1)
        self.l49.setAlignment(Qt.AlignCenter)

        self.gridLayout_25.addWidget(self.l49, 2, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame_carre_5, 1, 1, 1, 1)

        self.frame_carre_9 = QFrame(self.frame_sudo)
        self.frame_carre_9.setObjectName(u"frame_carre_9")
        self.frame_carre_9.setStyleSheet(u"")
        self.frame_carre_9.setFrameShape(QFrame.StyledPanel)
        self.frame_carre_9.setFrameShadow(QFrame.Raised)
        self.gridLayout_29 = QGridLayout(self.frame_carre_9)
        self.gridLayout_29.setObjectName(u"gridLayout_29")
        self.l62 = QLineEdit(self.frame_carre_9)
        self.l62.setObjectName(u"l62")
        self.l62.setMaxLength(1)
        self.l62.setAlignment(Qt.AlignCenter)

        self.gridLayout_29.addWidget(self.l62, 0, 1, 1, 1)

        self.l80 = QLineEdit(self.frame_carre_9)
        self.l80.setObjectName(u"l80")
        self.l80.setEnabled(True)
        self.l80.setMaxLength(1)
        self.l80.setAlignment(Qt.AlignCenter)

        self.gridLayout_29.addWidget(self.l80, 2, 1, 1, 1)

        self.l61 = QLineEdit(self.frame_carre_9)
        self.l61.setObjectName(u"l61")
        self.l61.setMaxLength(1)
        self.l61.setAlignment(Qt.AlignCenter)

        self.gridLayout_29.addWidget(self.l61, 0, 0, 1, 1)

        self.l72 = QLineEdit(self.frame_carre_9)
        self.l72.setObjectName(u"l72")
        self.l72.setMaxLength(1)
        self.l72.setAlignment(Qt.AlignCenter)

        self.gridLayout_29.addWidget(self.l72, 1, 2, 1, 1)

        self.l81 = QLineEdit(self.frame_carre_9)
        self.l81.setObjectName(u"l81")
        self.l81.setMaxLength(1)
        self.l81.setAlignment(Qt.AlignCenter)

        self.gridLayout_29.addWidget(self.l81, 2, 2, 1, 1)

        self.l70 = QLineEdit(self.frame_carre_9)
        self.l70.setObjectName(u"l70")
        self.l70.setMaxLength(1)
        self.l70.setAlignment(Qt.AlignCenter)

        self.gridLayout_29.addWidget(self.l70, 1, 0, 1, 1)

        self.l63 = QLineEdit(self.frame_carre_9)
        self.l63.setObjectName(u"l63")
        self.l63.setMaxLength(1)
        self.l63.setAlignment(Qt.AlignCenter)

        self.gridLayout_29.addWidget(self.l63, 0, 2, 1, 1)

        self.l71 = QLineEdit(self.frame_carre_9)
        self.l71.setObjectName(u"l71")
        self.l71.setMaxLength(1)
        self.l71.setAlignment(Qt.AlignCenter)

        self.gridLayout_29.addWidget(self.l71, 1, 1, 1, 1)

        self.l79 = QLineEdit(self.frame_carre_9)
        self.l79.setObjectName(u"l79")
        self.l79.setMaxLength(1)
        self.l79.setAlignment(Qt.AlignCenter)

        self.gridLayout_29.addWidget(self.l79, 2, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame_carre_9, 2, 2, 1, 1)

        self.frame_carre_1 = QFrame(self.frame_sudo)
        self.frame_carre_1.setObjectName(u"frame_carre_1")
        self.frame_carre_1.setStyleSheet(u"")
        self.frame_carre_1.setFrameShape(QFrame.StyledPanel)
        self.frame_carre_1.setFrameShadow(QFrame.Raised)
        self.gridLayout_18 = QGridLayout(self.frame_carre_1)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.l3 = QLineEdit(self.frame_carre_1)
        self.l3.setObjectName(u"l3")
        self.l3.setMaxLength(1)
        self.l3.setAlignment(Qt.AlignCenter)

        self.gridLayout_18.addWidget(self.l3, 0, 2, 1, 1)

        self.l19 = QLineEdit(self.frame_carre_1)
        self.l19.setObjectName(u"l19")
        self.l19.setMaxLength(1)
        self.l19.setAlignment(Qt.AlignCenter)

        self.gridLayout_18.addWidget(self.l19, 2, 0, 1, 1)

        self.l1 = QLineEdit(self.frame_carre_1)
        self.l1.setObjectName(u"l1")
        self.l1.setStyleSheet(u"")
        self.l1.setMaxLength(1)
        self.l1.setAlignment(Qt.AlignCenter)

        self.gridLayout_18.addWidget(self.l1, 0, 0, 1, 1)

        self.l2 = QLineEdit(self.frame_carre_1)
        self.l2.setObjectName(u"l2")
        self.l2.setMaxLength(1)
        self.l2.setAlignment(Qt.AlignCenter)

        self.gridLayout_18.addWidget(self.l2, 0, 1, 1, 1)

        self.l11 = QLineEdit(self.frame_carre_1)
        self.l11.setObjectName(u"l11")
        self.l11.setMaxLength(1)
        self.l11.setAlignment(Qt.AlignCenter)

        self.gridLayout_18.addWidget(self.l11, 1, 1, 1, 1)

        self.l12 = QLineEdit(self.frame_carre_1)
        self.l12.setObjectName(u"l12")
        self.l12.setMaxLength(1)
        self.l12.setAlignment(Qt.AlignCenter)

        self.gridLayout_18.addWidget(self.l12, 1, 2, 1, 1)

        self.l10 = QLineEdit(self.frame_carre_1)
        self.l10.setObjectName(u"l10")
        self.l10.setMaxLength(1)
        self.l10.setAlignment(Qt.AlignCenter)

        self.gridLayout_18.addWidget(self.l10, 1, 0, 1, 1)

        self.l20 = QLineEdit(self.frame_carre_1)
        self.l20.setObjectName(u"l20")
        self.l20.setEnabled(True)
        self.l20.setMaxLength(1)
        self.l20.setAlignment(Qt.AlignCenter)

        self.gridLayout_18.addWidget(self.l20, 2, 1, 1, 1)

        self.l21 = QLineEdit(self.frame_carre_1)
        self.l21.setObjectName(u"l21")
        self.l21.setMaxLength(1)
        self.l21.setAlignment(Qt.AlignCenter)

        self.gridLayout_18.addWidget(self.l21, 2, 2, 1, 1)


        self.gridLayout_2.addWidget(self.frame_carre_1, 0, 0, 1, 1)

        self.frame_carre_4 = QFrame(self.frame_sudo)
        self.frame_carre_4.setObjectName(u"frame_carre_4")
        self.frame_carre_4.setStyleSheet(u"")
        self.frame_carre_4.setFrameShape(QFrame.StyledPanel)
        self.frame_carre_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_24 = QGridLayout(self.frame_carre_4)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.l29 = QLineEdit(self.frame_carre_4)
        self.l29.setObjectName(u"l29")
        self.l29.setMaxLength(1)
        self.l29.setAlignment(Qt.AlignCenter)

        self.gridLayout_24.addWidget(self.l29, 0, 1, 1, 1)

        self.l47 = QLineEdit(self.frame_carre_4)
        self.l47.setObjectName(u"l47")
        self.l47.setEnabled(True)
        self.l47.setMaxLength(1)
        self.l47.setAlignment(Qt.AlignCenter)

        self.gridLayout_24.addWidget(self.l47, 2, 1, 1, 1)

        self.l28 = QLineEdit(self.frame_carre_4)
        self.l28.setObjectName(u"l28")
        self.l28.setMaxLength(1)
        self.l28.setAlignment(Qt.AlignCenter)

        self.gridLayout_24.addWidget(self.l28, 0, 0, 1, 1)

        self.l39 = QLineEdit(self.frame_carre_4)
        self.l39.setObjectName(u"l39")
        self.l39.setMaxLength(1)
        self.l39.setAlignment(Qt.AlignCenter)

        self.gridLayout_24.addWidget(self.l39, 1, 2, 1, 1)

        self.l48 = QLineEdit(self.frame_carre_4)
        self.l48.setObjectName(u"l48")
        self.l48.setMaxLength(1)
        self.l48.setAlignment(Qt.AlignCenter)

        self.gridLayout_24.addWidget(self.l48, 2, 2, 1, 1)

        self.l37 = QLineEdit(self.frame_carre_4)
        self.l37.setObjectName(u"l37")
        self.l37.setMaxLength(1)
        self.l37.setAlignment(Qt.AlignCenter)

        self.gridLayout_24.addWidget(self.l37, 1, 0, 1, 1)

        self.l30 = QLineEdit(self.frame_carre_4)
        self.l30.setObjectName(u"l30")
        self.l30.setMaxLength(1)
        self.l30.setAlignment(Qt.AlignCenter)

        self.gridLayout_24.addWidget(self.l30, 0, 2, 1, 1)

        self.l38 = QLineEdit(self.frame_carre_4)
        self.l38.setObjectName(u"l38")
        self.l38.setMaxLength(1)
        self.l38.setAlignment(Qt.AlignCenter)

        self.gridLayout_24.addWidget(self.l38, 1, 1, 1, 1)

        self.l46 = QLineEdit(self.frame_carre_4)
        self.l46.setObjectName(u"l46")
        self.l46.setMaxLength(1)
        self.l46.setAlignment(Qt.AlignCenter)

        self.gridLayout_24.addWidget(self.l46, 2, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame_carre_4, 1, 0, 1, 1)

        self.frame_carre_2 = QFrame(self.frame_sudo)
        self.frame_carre_2.setObjectName(u"frame_carre_2")
        self.frame_carre_2.setStyleSheet(u"")
        self.frame_carre_2.setFrameShape(QFrame.StyledPanel)
        self.frame_carre_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_22 = QGridLayout(self.frame_carre_2)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.l4 = QLineEdit(self.frame_carre_2)
        self.l4.setObjectName(u"l4")
        self.l4.setMaxLength(1)
        self.l4.setAlignment(Qt.AlignCenter)

        self.gridLayout_22.addWidget(self.l4, 0, 0, 1, 1)

        self.l14 = QLineEdit(self.frame_carre_2)
        self.l14.setObjectName(u"l14")
        self.l14.setMaxLength(1)
        self.l14.setAlignment(Qt.AlignCenter)

        self.gridLayout_22.addWidget(self.l14, 1, 1, 1, 1)

        self.l13 = QLineEdit(self.frame_carre_2)
        self.l13.setObjectName(u"l13")
        self.l13.setMaxLength(1)
        self.l13.setAlignment(Qt.AlignCenter)

        self.gridLayout_22.addWidget(self.l13, 1, 0, 1, 1)

        self.l15 = QLineEdit(self.frame_carre_2)
        self.l15.setObjectName(u"l15")
        self.l15.setMaxLength(1)
        self.l15.setAlignment(Qt.AlignCenter)

        self.gridLayout_22.addWidget(self.l15, 1, 2, 1, 1)

        self.l6 = QLineEdit(self.frame_carre_2)
        self.l6.setObjectName(u"l6")
        self.l6.setMaxLength(1)
        self.l6.setAlignment(Qt.AlignCenter)

        self.gridLayout_22.addWidget(self.l6, 0, 2, 1, 1)

        self.l5 = QLineEdit(self.frame_carre_2)
        self.l5.setObjectName(u"l5")
        self.l5.setMaxLength(1)
        self.l5.setAlignment(Qt.AlignCenter)

        self.gridLayout_22.addWidget(self.l5, 0, 1, 1, 1)

        self.l22 = QLineEdit(self.frame_carre_2)
        self.l22.setObjectName(u"l22")
        self.l22.setMaxLength(1)
        self.l22.setAlignment(Qt.AlignCenter)

        self.gridLayout_22.addWidget(self.l22, 2, 0, 1, 1)

        self.l23 = QLineEdit(self.frame_carre_2)
        self.l23.setObjectName(u"l23")
        self.l23.setEnabled(True)
        self.l23.setMaxLength(1)
        self.l23.setAlignment(Qt.AlignCenter)

        self.gridLayout_22.addWidget(self.l23, 2, 1, 1, 1)

        self.l24 = QLineEdit(self.frame_carre_2)
        self.l24.setObjectName(u"l24")
        self.l24.setMaxLength(1)
        self.l24.setAlignment(Qt.AlignCenter)

        self.gridLayout_22.addWidget(self.l24, 2, 2, 1, 1)


        self.gridLayout_2.addWidget(self.frame_carre_2, 0, 1, 1, 1)

        self.frame_carre_7 = QFrame(self.frame_sudo)
        self.frame_carre_7.setObjectName(u"frame_carre_7")
        self.frame_carre_7.setStyleSheet(u"")
        self.frame_carre_7.setFrameShape(QFrame.StyledPanel)
        self.frame_carre_7.setFrameShadow(QFrame.Raised)
        self.gridLayout_27 = QGridLayout(self.frame_carre_7)
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.l73 = QLineEdit(self.frame_carre_7)
        self.l73.setObjectName(u"l73")
        self.l73.setMaxLength(1)
        self.l73.setAlignment(Qt.AlignCenter)

        self.gridLayout_27.addWidget(self.l73, 2, 0, 1, 1)

        self.l66 = QLineEdit(self.frame_carre_7)
        self.l66.setObjectName(u"l66")
        self.l66.setMaxLength(1)
        self.l66.setAlignment(Qt.AlignCenter)

        self.gridLayout_27.addWidget(self.l66, 1, 2, 1, 1)

        self.l75 = QLineEdit(self.frame_carre_7)
        self.l75.setObjectName(u"l75")
        self.l75.setMaxLength(1)
        self.l75.setAlignment(Qt.AlignCenter)

        self.gridLayout_27.addWidget(self.l75, 2, 2, 1, 1)

        self.l65 = QLineEdit(self.frame_carre_7)
        self.l65.setObjectName(u"l65")
        self.l65.setMaxLength(1)
        self.l65.setAlignment(Qt.AlignCenter)

        self.gridLayout_27.addWidget(self.l65, 1, 1, 1, 1)

        self.l74 = QLineEdit(self.frame_carre_7)
        self.l74.setObjectName(u"l74")
        self.l74.setEnabled(True)
        self.l74.setMaxLength(1)
        self.l74.setAlignment(Qt.AlignCenter)

        self.gridLayout_27.addWidget(self.l74, 2, 1, 1, 1)

        self.l55 = QLineEdit(self.frame_carre_7)
        self.l55.setObjectName(u"l55")
        self.l55.setMaxLength(1)
        self.l55.setAlignment(Qt.AlignCenter)

        self.gridLayout_27.addWidget(self.l55, 0, 0, 1, 1)

        self.l64 = QLineEdit(self.frame_carre_7)
        self.l64.setObjectName(u"l64")
        self.l64.setMaxLength(1)
        self.l64.setAlignment(Qt.AlignCenter)

        self.gridLayout_27.addWidget(self.l64, 1, 0, 1, 1)

        self.l56 = QLineEdit(self.frame_carre_7)
        self.l56.setObjectName(u"l56")
        self.l56.setMaxLength(1)
        self.l56.setAlignment(Qt.AlignCenter)

        self.gridLayout_27.addWidget(self.l56, 0, 1, 1, 1)

        self.l57 = QLineEdit(self.frame_carre_7)
        self.l57.setObjectName(u"l57")
        self.l57.setMaxLength(1)
        self.l57.setAlignment(Qt.AlignCenter)

        self.gridLayout_27.addWidget(self.l57, 0, 2, 1, 1)


        self.gridLayout_2.addWidget(self.frame_carre_7, 2, 0, 1, 1)

        self.frame_carre_3 = QFrame(self.frame_sudo)
        self.frame_carre_3.setObjectName(u"frame_carre_3")
        self.frame_carre_3.setStyleSheet(u"")
        self.frame_carre_3.setFrameShape(QFrame.StyledPanel)
        self.frame_carre_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_23 = QGridLayout(self.frame_carre_3)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.l8 = QLineEdit(self.frame_carre_3)
        self.l8.setObjectName(u"l8")
        self.l8.setMaxLength(1)
        self.l8.setAlignment(Qt.AlignCenter)

        self.gridLayout_23.addWidget(self.l8, 0, 1, 1, 1)

        self.l26 = QLineEdit(self.frame_carre_3)
        self.l26.setObjectName(u"l26")
        self.l26.setEnabled(True)
        self.l26.setMaxLength(1)
        self.l26.setAlignment(Qt.AlignCenter)

        self.gridLayout_23.addWidget(self.l26, 2, 1, 1, 1)

        self.l7 = QLineEdit(self.frame_carre_3)
        self.l7.setObjectName(u"l7")
        self.l7.setMaxLength(1)
        self.l7.setAlignment(Qt.AlignCenter)

        self.gridLayout_23.addWidget(self.l7, 0, 0, 1, 1)

        self.l18 = QLineEdit(self.frame_carre_3)
        self.l18.setObjectName(u"l18")
        self.l18.setMaxLength(1)
        self.l18.setAlignment(Qt.AlignCenter)

        self.gridLayout_23.addWidget(self.l18, 1, 2, 1, 1)

        self.l27 = QLineEdit(self.frame_carre_3)
        self.l27.setObjectName(u"l27")
        self.l27.setMaxLength(1)
        self.l27.setAlignment(Qt.AlignCenter)

        self.gridLayout_23.addWidget(self.l27, 2, 2, 1, 1)

        self.l16 = QLineEdit(self.frame_carre_3)
        self.l16.setObjectName(u"l16")
        self.l16.setMaxLength(1)
        self.l16.setAlignment(Qt.AlignCenter)

        self.gridLayout_23.addWidget(self.l16, 1, 0, 1, 1)

        self.l9 = QLineEdit(self.frame_carre_3)
        self.l9.setObjectName(u"l9")
        self.l9.setMaxLength(1)
        self.l9.setAlignment(Qt.AlignCenter)

        self.gridLayout_23.addWidget(self.l9, 0, 2, 1, 1)

        self.l17 = QLineEdit(self.frame_carre_3)
        self.l17.setObjectName(u"l17")
        self.l17.setMaxLength(1)
        self.l17.setAlignment(Qt.AlignCenter)

        self.gridLayout_23.addWidget(self.l17, 1, 1, 1, 1)

        self.l25 = QLineEdit(self.frame_carre_3)
        self.l25.setObjectName(u"l25")
        self.l25.setMaxLength(1)
        self.l25.setAlignment(Qt.AlignCenter)

        self.gridLayout_23.addWidget(self.l25, 2, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame_carre_3, 0, 2, 1, 1)


        self.horizontalLayout_2.addWidget(self.frame_sudo)

        SudokuGraphia.setCentralWidget(self.centralwidget)

        self.retranslateUi(SudokuGraphia)

        QMetaObject.connectSlotsByName(SudokuGraphia)
    # setupUi

    def retranslateUi(self, SudokuGraphia):
        SudokuGraphia.setWindowTitle(QCoreApplication.translate("SudokuGraphia", u"MainWindow", None))
        self.groupBox_algo.setTitle(QCoreApplication.translate("SudokuGraphia", u"Algorithme de r\u00e9solution", None))
        self.powel.setText(QCoreApplication.translate("SudokuGraphia", u"Powel", None))
        self.bck.setText(QCoreApplication.translate("SudokuGraphia", u"Backtracking", None))
        self.gl.setText(QCoreApplication.translate("SudokuGraphia", u"Glouton", None))
        self.encourt.setText(QCoreApplication.translate("SudokuGraphia", u"Manuel", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("SudokuGraphia", u"Description", None))
        self.desc.setHtml(QCoreApplication.translate("SudokuGraphia", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<ol style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li style=\" font-size:9pt;\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">Initialisation :</span><span style=\" font-size:12pt;\"> Commencez par trier les sommets du graphe de mani\u00e8re \u00e0 ce que les sommets de degr\u00e9 \u00e9lev\u00e9 soient trait\u00e9s en premier. Le deg"
                        "r\u00e9 d'un sommet est le nombre d'ar\u00eates incidentes \u00e0 ce sommet.</span></li>\n"
"<li style=\" font-size:12pt;\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">Attribution de couleurs :</span> Parcourez chaque sommet du graphe dans l'ordre tri\u00e9. Pour chaque sommet, attribuez-lui la plus petite couleur possible qui n'est pas d\u00e9j\u00e0 utilis\u00e9e par ses voisins. Si tous les voisins ont d\u00e9j\u00e0 une couleur attribu\u00e9e, ajoutez une nouvelle couleur.</li>\n"
"<li style=\" font-size:12pt;\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">Terminaison :</span> R\u00e9p\u00e9tez l'\u00e9tape 2 pour tous les sommets du graphe jusqu'\u00e0 ce que tous les sommets soient colori\u00e9s.</li></ol>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0"
                        "px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">L'algorithme de coloriage de graphes glouton donne une solution acceptable, mais pas toujours optimale. Il peut utiliser plus de couleurs que n\u00e9cessaire, mais il est rapide et simple. L'efficacit\u00e9 de l'algorithme d\u00e9pend souvent de l'ordre dans lequel les sommets sont trait\u00e9s.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">En pratique, cet algorithme est utilis\u00e9 pour r\u00e9soudre des probl\u00e8mes de coloration de graphes dans des domaines tels que l'assignation de fr\u00e9quences aux canaux de communication sans fil, l'assignation de registres dans la compilation de programmes, etc.</span></p></body></html>", None))
        self.reset.setText(QCoreApplication.translate("SudokuGraphia", u"R\u00e9initialiser", None))
        self.generate.setText(QCoreApplication.translate("SudokuGraphia", u"G\u00e9n\u00e9rer", None))
        self.resolveButton.setText(QCoreApplication.translate("SudokuGraphia", u"R\u00e9soudre", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("SudokuGraphia", u"Sudoku", None))
        self.l59.setText(QCoreApplication.translate("SudokuGraphia", u"2", None))
        self.l77.setText(QCoreApplication.translate("SudokuGraphia", u"8", None))
        self.l58.setText(QCoreApplication.translate("SudokuGraphia", u"1", None))
        self.l69.setText(QCoreApplication.translate("SudokuGraphia", u"6", None))
        self.l78.setText(QCoreApplication.translate("SudokuGraphia", u"9", None))
        self.l67.setText(QCoreApplication.translate("SudokuGraphia", u"4", None))
        self.l60.setText(QCoreApplication.translate("SudokuGraphia", u"3", None))
        self.l68.setText(QCoreApplication.translate("SudokuGraphia", u"5", None))
        self.l76.setText(QCoreApplication.translate("SudokuGraphia", u"7", None))
        self.l35.setText(QCoreApplication.translate("SudokuGraphia", u"2", None))
        self.l53.setText(QCoreApplication.translate("SudokuGraphia", u"8", None))
        self.l34.setText(QCoreApplication.translate("SudokuGraphia", u"1", None))
        self.l45.setText(QCoreApplication.translate("SudokuGraphia", u"6", None))
        self.l54.setText(QCoreApplication.translate("SudokuGraphia", u"9", None))
        self.l43.setText(QCoreApplication.translate("SudokuGraphia", u"4", None))
        self.l36.setText(QCoreApplication.translate("SudokuGraphia", u"3", None))
        self.l44.setText(QCoreApplication.translate("SudokuGraphia", u"5", None))
        self.l52.setText(QCoreApplication.translate("SudokuGraphia", u"7", None))
        self.l32.setText(QCoreApplication.translate("SudokuGraphia", u"2", None))
        self.l50.setText(QCoreApplication.translate("SudokuGraphia", u"8", None))
        self.l31.setText(QCoreApplication.translate("SudokuGraphia", u"1", None))
        self.l42.setText(QCoreApplication.translate("SudokuGraphia", u"6", None))
        self.l51.setText(QCoreApplication.translate("SudokuGraphia", u"9", None))
        self.l40.setText(QCoreApplication.translate("SudokuGraphia", u"4", None))
        self.l33.setText(QCoreApplication.translate("SudokuGraphia", u"3", None))
        self.l41.setText(QCoreApplication.translate("SudokuGraphia", u"5", None))
        self.l49.setText(QCoreApplication.translate("SudokuGraphia", u"7", None))
        self.l62.setText(QCoreApplication.translate("SudokuGraphia", u"2", None))
        self.l80.setText(QCoreApplication.translate("SudokuGraphia", u"8", None))
        self.l61.setText(QCoreApplication.translate("SudokuGraphia", u"1", None))
        self.l72.setText(QCoreApplication.translate("SudokuGraphia", u"6", None))
        self.l81.setText(QCoreApplication.translate("SudokuGraphia", u"9", None))
        self.l70.setText(QCoreApplication.translate("SudokuGraphia", u"4", None))
        self.l63.setText(QCoreApplication.translate("SudokuGraphia", u"3", None))
        self.l71.setText(QCoreApplication.translate("SudokuGraphia", u"5", None))
        self.l79.setText(QCoreApplication.translate("SudokuGraphia", u"7", None))
        self.l3.setText(QCoreApplication.translate("SudokuGraphia", u"3", None))
        self.l19.setText(QCoreApplication.translate("SudokuGraphia", u"7", None))
        self.l1.setText(QCoreApplication.translate("SudokuGraphia", u"1", None))
        self.l2.setText(QCoreApplication.translate("SudokuGraphia", u"2", None))
        self.l11.setText(QCoreApplication.translate("SudokuGraphia", u"5", None))
        self.l12.setText(QCoreApplication.translate("SudokuGraphia", u"6", None))
        self.l10.setText(QCoreApplication.translate("SudokuGraphia", u"4", None))
        self.l20.setText(QCoreApplication.translate("SudokuGraphia", u"8", None))
        self.l21.setText(QCoreApplication.translate("SudokuGraphia", u"9", None))
        self.l29.setText(QCoreApplication.translate("SudokuGraphia", u"2", None))
        self.l47.setText(QCoreApplication.translate("SudokuGraphia", u"8", None))
        self.l28.setText(QCoreApplication.translate("SudokuGraphia", u"1", None))
        self.l39.setText(QCoreApplication.translate("SudokuGraphia", u"6", None))
        self.l48.setText(QCoreApplication.translate("SudokuGraphia", u"9", None))
        self.l37.setText(QCoreApplication.translate("SudokuGraphia", u"4", None))
        self.l30.setText(QCoreApplication.translate("SudokuGraphia", u"3", None))
        self.l38.setText(QCoreApplication.translate("SudokuGraphia", u"5", None))
        self.l46.setText(QCoreApplication.translate("SudokuGraphia", u"7", None))
        self.l4.setText(QCoreApplication.translate("SudokuGraphia", u"1", None))
        self.l14.setText(QCoreApplication.translate("SudokuGraphia", u"5", None))
        self.l13.setText(QCoreApplication.translate("SudokuGraphia", u"4", None))
        self.l15.setText(QCoreApplication.translate("SudokuGraphia", u"6", None))
        self.l6.setText(QCoreApplication.translate("SudokuGraphia", u"3", None))
        self.l5.setText(QCoreApplication.translate("SudokuGraphia", u"2", None))
        self.l22.setText(QCoreApplication.translate("SudokuGraphia", u"7", None))
        self.l23.setText(QCoreApplication.translate("SudokuGraphia", u"8", None))
        self.l24.setText(QCoreApplication.translate("SudokuGraphia", u"9", None))
        self.l73.setText(QCoreApplication.translate("SudokuGraphia", u"7", None))
        self.l66.setText(QCoreApplication.translate("SudokuGraphia", u"6", None))
        self.l75.setText(QCoreApplication.translate("SudokuGraphia", u"9", None))
        self.l65.setText(QCoreApplication.translate("SudokuGraphia", u"5", None))
        self.l74.setText(QCoreApplication.translate("SudokuGraphia", u"8", None))
        self.l55.setText(QCoreApplication.translate("SudokuGraphia", u"1", None))
        self.l64.setText(QCoreApplication.translate("SudokuGraphia", u"4", None))
        self.l56.setText(QCoreApplication.translate("SudokuGraphia", u"2", None))
        self.l57.setText(QCoreApplication.translate("SudokuGraphia", u"3", None))
        self.l8.setText(QCoreApplication.translate("SudokuGraphia", u"2", None))
        self.l26.setText(QCoreApplication.translate("SudokuGraphia", u"8", None))
        self.l7.setText(QCoreApplication.translate("SudokuGraphia", u"1", None))
        self.l18.setText(QCoreApplication.translate("SudokuGraphia", u"6", None))
        self.l27.setText(QCoreApplication.translate("SudokuGraphia", u"9", None))
        self.l16.setText(QCoreApplication.translate("SudokuGraphia", u"4", None))
        self.l9.setText(QCoreApplication.translate("SudokuGraphia", u"3", None))
        self.l17.setText(QCoreApplication.translate("SudokuGraphia", u"5", None))
        self.l25.setText(QCoreApplication.translate("SudokuGraphia", u"7", None))
    # retranslateUi

