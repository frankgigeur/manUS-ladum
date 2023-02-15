# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'InterfaceJeux.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ManUS_ludum_Interface(object):
    def setupUi(self, ManUS_ludum_Interface):
        ManUS_ludum_Interface.setObjectName("ManUS_ludum_Interface")
        ManUS_ludum_Interface.resize(1619, 958)
        self.centralwidget = QtWidgets.QWidget(ManUS_ludum_Interface)
        self.centralwidget.setObjectName("centralwidget")
        self.header = QtWidgets.QGroupBox(self.centralwidget)
        self.header.setGeometry(QtCore.QRect(10, 10, 1600, 70))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.header.sizePolicy().hasHeightForWidth())
        self.header.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Corbel Light")
        font.setPointSize(26)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.header.setFont(font)
        self.header.setTitle("")
        self.header.setFlat(False)
        self.header.setObjectName("header")
        self.boutonLancementJeux = QtWidgets.QPushButton(self.header)
        self.boutonLancementJeux.setGeometry(QtCore.QRect(10, 10, 700, 50))
        self.boutonLancementJeux.setObjectName("boutonLancementJeux")
        self.titre = QtWidgets.QLabel(self.header)
        self.titre.setGeometry(QtCore.QRect(720, 10, 810, 50))
        font = QtGui.QFont()
        font.setPointSize(37)
        self.titre.setFont(font)
        self.titre.setAutoFillBackground(False)
        self.titre.setAlignment(QtCore.Qt.AlignCenter)
        self.titre.setObjectName("titre")
        self.boutonInfo = QtWidgets.QPushButton(self.header)
        self.boutonInfo.setGeometry(QtCore.QRect(1540, 10, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.boutonInfo.setFont(font)
        self.boutonInfo.setObjectName("boutonInfo")
        self.robot = QtWidgets.QGroupBox(self.centralwidget)
        self.robot.setGeometry(QtCore.QRect(10, 85, 350, 570))
        font = QtGui.QFont()
        font.setFamily("Corbel Light")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.robot.setFont(font)
        self.robot.setTitle("")
        self.robot.setObjectName("robot")
        self.titreContMain = QtWidgets.QLabel(self.robot)
        self.titreContMain.setGeometry(QtCore.QRect(10, 10, 330, 90))
        self.titreContMain.setAutoFillBackground(True)
        self.titreContMain.setFrameShape(QtWidgets.QFrame.Box)
        self.titreContMain.setFrameShadow(QtWidgets.QFrame.Raised)
        self.titreContMain.setLineWidth(2)
        self.titreContMain.setAlignment(QtCore.Qt.AlignCenter)
        self.titreContMain.setObjectName("titreContMain")
        self.boutonRobotRoche = QtWidgets.QPushButton(self.robot)
        self.boutonRobotRoche.setGeometry(QtCore.QRect(35, 160, 280, 90))
        self.boutonRobotRoche.setObjectName("boutonRobotRoche")
        self.boutonRobotPapier = QtWidgets.QPushButton(self.robot)
        self.boutonRobotPapier.setGeometry(QtCore.QRect(35, 260, 280, 90))
        self.boutonRobotPapier.setObjectName("boutonRobotPapier")
        self.boutonRobotCiseaux = QtWidgets.QPushButton(self.robot)
        self.boutonRobotCiseaux.setGeometry(QtCore.QRect(35, 360, 280, 90))
        self.boutonRobotCiseaux.setObjectName("boutonRobotCiseaux")
        self.humain = QtWidgets.QGroupBox(self.centralwidget)
        self.humain.setGeometry(QtCore.QRect(370, 85, 350, 570))
        font = QtGui.QFont()
        font.setFamily("Corbel Light")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.humain.setFont(font)
        self.humain.setTitle("")
        self.humain.setObjectName("humain")
        self.boutonHumainRoche = QtWidgets.QPushButton(self.humain)
        self.boutonHumainRoche.setGeometry(QtCore.QRect(35, 160, 280, 90))
        self.boutonHumainRoche.setObjectName("boutonHumainRoche")
        self.titreContHum = QtWidgets.QLabel(self.humain)
        self.titreContHum.setGeometry(QtCore.QRect(10, 10, 330, 90))
        self.titreContHum.setAutoFillBackground(True)
        self.titreContHum.setFrameShape(QtWidgets.QFrame.Box)
        self.titreContHum.setFrameShadow(QtWidgets.QFrame.Raised)
        self.titreContHum.setLineWidth(2)
        self.titreContHum.setAlignment(QtCore.Qt.AlignCenter)
        self.titreContHum.setObjectName("titreContHum")
        self.boutonHumainCiseaux = QtWidgets.QPushButton(self.humain)
        self.boutonHumainCiseaux.setGeometry(QtCore.QRect(35, 360, 280, 90))
        self.boutonHumainCiseaux.setObjectName("boutonHumainCiseaux")
        self.boutonHumainPapier = QtWidgets.QPushButton(self.humain)
        self.boutonHumainPapier.setGeometry(QtCore.QRect(35, 260, 280, 90))
        self.boutonHumainPapier.setObjectName("boutonHumainPapier")
        self.statistiques = QtWidgets.QGroupBox(self.centralwidget)
        self.statistiques.setGeometry(QtCore.QRect(10, 659, 710, 271))
        font = QtGui.QFont()
        font.setFamily("Corbel Light")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.statistiques.setFont(font)
        self.statistiques.setTitle("")
        self.statistiques.setObjectName("statistiques")
        self.boutonStatsReset = QtWidgets.QPushButton(self.statistiques)
        self.boutonStatsReset.setGeometry(QtCore.QRect(10, 10, 150, 40))
        self.boutonStatsReset.setObjectName("boutonStatsReset")
        self.titreStats = QtWidgets.QLabel(self.statistiques)
        self.titreStats.setGeometry(QtCore.QRect(170, 10, 531, 40))
        self.titreStats.setAutoFillBackground(True)
        self.titreStats.setFrameShape(QtWidgets.QFrame.Box)
        self.titreStats.setFrameShadow(QtWidgets.QFrame.Raised)
        self.titreStats.setLineWidth(2)
        self.titreStats.setAlignment(QtCore.Qt.AlignCenter)
        self.titreStats.setObjectName("titreStats")
        self.statsAIwin = QtWidgets.QLabel(self.statistiques)
        self.statsAIwin.setGeometry(QtCore.QRect(10, 90, 510, 25))
        self.statsAIwin.setObjectName("statsAIwin")
        self.nbAiWin = QtWidgets.QLCDNumber(self.statistiques)
        self.nbAiWin.setGeometry(QtCore.QRect(530, 90, 170, 25))
        self.nbAiWin.setObjectName("nbAiWin")
        self.nbHumWin = QtWidgets.QLCDNumber(self.statistiques)
        self.nbHumWin.setGeometry(QtCore.QRect(530, 140, 170, 25))
        self.nbHumWin.setObjectName("nbHumWin")
        self.statsHumWin = QtWidgets.QLabel(self.statistiques)
        self.statsHumWin.setGeometry(QtCore.QRect(10, 140, 510, 25))
        self.statsHumWin.setObjectName("statsHumWin")
        self.pourcentRoche = QtWidgets.QLCDNumber(self.statistiques)
        self.pourcentRoche.setGeometry(QtCore.QRect(10, 200, 75, 50))
        self.pourcentRoche.setSmallDecimalPoint(False)
        self.pourcentRoche.setObjectName("pourcentRoche")
        self.statsRoche = QtWidgets.QLabel(self.statistiques)
        self.statsRoche.setGeometry(QtCore.QRect(95, 200, 125, 50))
        self.statsRoche.setObjectName("statsRoche")
        self.statsPapier = QtWidgets.QLabel(self.statistiques)
        self.statsPapier.setGeometry(QtCore.QRect(335, 200, 125, 50))
        self.statsPapier.setObjectName("statsPapier")
        self.pourcentPapier = QtWidgets.QLCDNumber(self.statistiques)
        self.pourcentPapier.setGeometry(QtCore.QRect(250, 200, 75, 50))
        self.pourcentPapier.setSmallDecimalPoint(False)
        self.pourcentPapier.setObjectName("pourcentPapier")
        self.statsCiseaux = QtWidgets.QLabel(self.statistiques)
        self.statsCiseaux.setGeometry(QtCore.QRect(575, 200, 125, 50))
        self.statsCiseaux.setObjectName("statsCiseaux")
        self.pourcentCiseaux = QtWidgets.QLCDNumber(self.statistiques)
        self.pourcentCiseaux.setGeometry(QtCore.QRect(490, 200, 75, 50))
        self.pourcentCiseaux.setSmallDecimalPoint(False)
        self.pourcentCiseaux.setObjectName("pourcentCiseaux")
        self.camera = QtWidgets.QGroupBox(self.centralwidget)
        self.camera.setGeometry(QtCore.QRect(729, 80, 881, 621))
        self.camera.setObjectName("camera")


        self.camHolder = QtWidgets.QTabWidget(self.camera)
        self.camHolder.setGeometry(QtCore.QRect(10, 20, 860, 590))
        self.camHolder.setTabPosition(QtWidgets.QTabWidget.South)
        self.camHolder.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.camHolder.setUsesScrollButtons(False)
        self.camHolder.setObjectName("camHolder")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.camHolder.addTab(self.tab, "")


        self.decompte = QtWidgets.QGroupBox(self.centralwidget)
        self.decompte.setGeometry(QtCore.QRect(729, 699, 881, 231))
        self.decompte.setObjectName("decompte")
        ManUS_ludum_Interface.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(ManUS_ludum_Interface)
        self.statusbar.setObjectName("statusbar")
        ManUS_ludum_Interface.setStatusBar(self.statusbar)

        self.retranslateUi(ManUS_ludum_Interface)
        self.camHolder.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(ManUS_ludum_Interface)

    def retranslateUi(self, ManUS_ludum_Interface):
        _translate = QtCore.QCoreApplication.translate
        ManUS_ludum_Interface.setWindowTitle(_translate("ManUS_ludum_Interface", "MainWindow"))
        self.boutonLancementJeux.setText(_translate("ManUS_ludum_Interface", "Commencer la partie"))
        self.titre.setText(_translate("ManUS_ludum_Interface", "ManUS ludum"))
        self.boutonInfo.setText(_translate("ManUS_ludum_Interface", "i"))
        self.titreContMain.setText(_translate("ManUS_ludum_Interface", "Contrôle de la main"))
        self.boutonRobotRoche.setText(_translate("ManUS_ludum_Interface", "Roche"))
        self.boutonRobotPapier.setText(_translate("ManUS_ludum_Interface", "Papier"))
        self.boutonRobotCiseaux.setText(_translate("ManUS_ludum_Interface", "Ciseaux"))
        self.boutonHumainRoche.setText(_translate("ManUS_ludum_Interface", "Roche"))
        self.titreContHum.setText(_translate("ManUS_ludum_Interface", "Correction de votre coup"))
        self.boutonHumainCiseaux.setText(_translate("ManUS_ludum_Interface", "Ciseaux"))
        self.boutonHumainPapier.setText(_translate("ManUS_ludum_Interface", "Papier"))
        self.boutonStatsReset.setText(_translate("ManUS_ludum_Interface", "Réinitialisation"))
        self.titreStats.setText(_translate("ManUS_ludum_Interface", "Statistiques de jeux"))
        self.statsAIwin.setText(_translate("ManUS_ludum_Interface", "Nombre de partie gagnée par ManUS :"))
        self.statsHumWin.setText(_translate("ManUS_ludum_Interface", "Nombre de partie que vous avez gagnée :"))
        self.statsRoche.setText(_translate("ManUS_ludum_Interface", "% Roche"))
        self.statsPapier.setText(_translate("ManUS_ludum_Interface", "% Papier"))
        self.statsCiseaux.setText(_translate("ManUS_ludum_Interface", "% Ciseaux"))
        self.camera.setTitle(_translate("ManUS_ludum_Interface", "camera"))
        self.camHolder.setTabText(self.camHolder.indexOf(self.tab), _translate("ManUS_ludum_Interface", "web cam"))
        self.decompte.setTitle(_translate("ManUS_ludum_Interface", "decompte"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ManUS_ludum_Interface = QtWidgets.QMainWindow()
    ui = Ui_ManUS_ludum_Interface()
    ui.setupUi(ManUS_ludum_Interface)
    ManUS_ludum_Interface.show()
    sys.exit(app.exec_())
