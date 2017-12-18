# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'teste.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from requests import get
from threading import Thread

# -------------
# Main window
# -------------

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(680, 460)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.treeDownload = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeDownload.setGeometry(QtCore.QRect(220, 40, 240, 270))
        self.treeDownload.setObjectName("treeDownload")
        
        self.listDownload = QtWidgets.QListWidget(self.centralwidget)
        self.listDownload.setGeometry(QtCore.QRect(10, 70, 190, 380))
        self.listDownload.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.listDownload.setObjectName("listDownload")
        
        self.lblMods = QtWidgets.QLabel(self.centralwidget)
        self.lblMods.setGeometry(QtCore.QRect(10, 10, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblMods.setFont(font)
        self.lblMods.setObjectName("lblMods")
        
        self.edtFilter = QtWidgets.QLineEdit(self.centralwidget)
        self.edtFilter.setGeometry(QtCore.QRect(10, 40, 125, 20))
        self.edtFilter.setObjectName("edtFilter")
        
        self.btnFilter = QtWidgets.QPushButton(self.centralwidget)
        self.btnFilter.setGeometry(QtCore.QRect(140, 40, 60, 23))
        self.btnFilter.setObjectName("btnFilter")
        
        self.lblDownloads = QtWidgets.QLabel(self.centralwidget)
        self.lblDownloads.setGeometry(QtCore.QRect(220, 10, 200, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblDownloads.setFont(font)
        self.lblDownloads.setObjectName("lblDownloads")
        
        self.grpImpExp = QtWidgets.QGroupBox(self.centralwidget)
        self.grpImpExp.setGeometry(QtCore.QRect(220, 320, 180, 50))
        self.grpImpExp.setObjectName("grpImpExp")
        
        self.btnImport = QtWidgets.QPushButton(self.grpImpExp)
        self.btnImport.setGeometry(QtCore.QRect(10, 20, 75, 23))
        self.btnImport.setObjectName("btnImport")
        self.btnExport = QtWidgets.QPushButton(self.grpImpExp)
        self.btnExport.setGeometry(QtCore.QRect(100, 20, 75, 23))
        self.btnExport.setObjectName("btnExport")
        
        self.grpNewMod = QtWidgets.QGroupBox(self.centralwidget)
        self.grpNewMod.setGeometry(QtCore.QRect(220, 370, 180, 81))
        self.grpNewMod.setObjectName("grpNewMod")
        
        self.edtAddMod = QtWidgets.QLineEdit(self.grpNewMod)
        self.edtAddMod.setGeometry(QtCore.QRect(10, 20, 161, 20))
        self.edtAddMod.setObjectName("edtAddMod")
        
        self.btnAddMod = QtWidgets.QPushButton(self.grpNewMod)
        self.btnAddMod.setGeometry(QtCore.QRect(10, 50, 75, 23))
        self.btnAddMod.setObjectName("btnAddMod")
        
        self.lblOptions = QtWidgets.QLabel(self.centralwidget)
        self.lblOptions.setGeometry(QtCore.QRect(480, 10, 200, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblOptions.setFont(font)
        self.lblOptions.setObjectName("lblOptions")
        
        self.grpVersions = QtWidgets.QGroupBox(self.centralwidget)
        self.grpVersions.setGeometry(QtCore.QRect(480, 40, 120, 90))
        self.grpVersions.setObjectName("grpVersions")
        
        self.chkAlpha = QtWidgets.QCheckBox(self.grpVersions)
        self.chkAlpha.setGeometry(QtCore.QRect(10, 20, 70, 17))
        self.chkAlpha.setObjectName("chkAlpha")
        
        self.chkBeta = QtWidgets.QCheckBox(self.grpVersions)
        self.chkBeta.setGeometry(QtCore.QRect(10, 40, 70, 17))
        self.chkBeta.setObjectName("chkBeta")
        
        self.chkRelease = QtWidgets.QCheckBox(self.grpVersions)
        self.chkRelease.setGeometry(QtCore.QRect(10, 60, 70, 17))
        self.chkRelease.setObjectName("chkRelease")
        
        self.grpPriority = QtWidgets.QGroupBox(self.centralwidget)
        self.grpPriority.setGeometry(QtCore.QRect(480, 140, 120, 70))
        self.grpPriority.setObjectName("grpPriority")
        
        self.radRecent = QtWidgets.QRadioButton(self.grpPriority)
        self.radRecent.setGeometry(QtCore.QRect(10, 20, 82, 17))
        self.radRecent.setObjectName("radRecent")
        
        self.radStable = QtWidgets.QRadioButton(self.grpPriority)
        self.radStable.setGeometry(QtCore.QRect(10, 40, 82, 17))
        self.radStable.setObjectName("radStable")
        
        self.grpDir = QtWidgets.QGroupBox(self.centralwidget)
        self.grpDir.setGeometry(QtCore.QRect(480, 220, 190, 70))
        self.grpDir.setObjectName("grpDir")
        
        self.lblDir = QtWidgets.QLabel(self.grpDir)
        self.lblDir.setGeometry(QtCore.QRect(10, 20, 170, 13))
        self.lblDir.setObjectName("lblDir")
        
        self.btnDir = QtWidgets.QPushButton(self.grpDir)
        self.btnDir.setGeometry(QtCore.QRect(10, 40, 100, 23))
        self.btnDir.setObjectName("btnDir")
        
        self.chkOptDeps = QtWidgets.QCheckBox(self.centralwidget)
        self.chkOptDeps.setGeometry(QtCore.QRect(490, 300, 170, 17))
        self.chkOptDeps.setObjectName("chkOptDeps")
        
        self.btnUpdate = QtWidgets.QPushButton(self.centralwidget)
        self.btnUpdate.setGeometry(QtCore.QRect(490, 330, 170, 23))
        self.btnUpdate.setObjectName("btnUpdate")
        
        self.btnDownload = QtWidgets.QPushButton(self.centralwidget)
        self.btnDownload.setGeometry(QtCore.QRect(490, 360, 170, 23))
        self.btnDownload.setObjectName("btnDownload")
        
        self.btnUpdateDownload = QtWidgets.QPushButton(self.centralwidget)
        self.btnUpdateDownload.setGeometry(QtCore.QRect(490, 390, 170, 43))
        self.btnUpdateDownload.setObjectName("btnUpdateDownload")
        
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.treeDownload.headerItem().setText(0, _translate("MainWindow", "Progress bar"))
        self.treeDownload.headerItem().setText(1, _translate("MainWindow", "Mod name"))
        self.lblMods.setText(_translate("MainWindow", "Mod list"))
        self.btnFilter.setText(_translate("MainWindow", "Filter"))
        self.lblDownloads.setText(_translate("MainWindow", "Download progress"))
        self.grpImpExp.setTitle(_translate("MainWindow", "Mod list file import or export"))
        self.btnImport.setText(_translate("MainWindow", "Import"))
        self.btnExport.setText(_translate("MainWindow", "Export"))
        self.grpNewMod.setTitle(_translate("MainWindow", "Add new mod to the list"))
        self.btnAddMod.setText(_translate("MainWindow", "Add mod"))
        self.lblOptions.setText(_translate("MainWindow", "Options"))
        self.grpVersions.setTitle(_translate("MainWindow", "Versions"))
        self.chkAlpha.setText(_translate("MainWindow", "Alpha"))
        self.chkBeta.setText(_translate("MainWindow", "Beta"))
        self.chkRelease.setText(_translate("MainWindow", "Release"))
        self.grpPriority.setTitle(_translate("MainWindow", "Priority"))
        self.radRecent.setText(_translate("MainWindow", "Most recent"))
        self.radStable.setText(_translate("MainWindow", "Stable"))
        self.grpDir.setTitle(_translate("MainWindow", "Download directory"))
        self.lblDir.setText(_translate("MainWindow", "D:\\Download\\mods"))
        self.btnDir.setText(_translate("MainWindow", "Select directory..."))
        self.chkOptDeps.setText(_translate("MainWindow", "Include optional dependencies"))
        self.btnUpdate.setText(_translate("MainWindow", "Update dependencies"))
        self.btnDownload.setText(_translate("MainWindow", "Download mods"))
        self.btnUpdateDownload.setText(_translate("MainWindow", "Update dependencies\n"
"and download mods"))

class ModItem(object):
    def __init__(self, name):
        self.name = name
        self.progress = QtWidgets.QProgressBar()
        self.progress.setRange(0, 100)
        self.progress.setValue(0)
        self.progress.setFixedHeight(15)

    def addToTree(self, tree):
        self.item = QtWidgets.QTreeWidgetItem(tree)
        tree.setItemWidget(self.item, 0, self.progress)
        self.item.setText(1, self.name)

    def updateProgress(self, current, total):
        if current > 0:
            percent = current/total * 100
        else:
            percent = 0
        self.progress.setValue(percent)

def startDownload(mod):
    print("start download\n")
    request = get("https://minecraft.curseforge.com/projects/applied-energistics-2/files/2503759/download", stream=True)
    with open("teste.jar", "wb") as modFile:
        size = int(request.headers.get("content-length"))
        print(size, end='\n')
        mod.updateProgress(0, size)
        i = 0
        for chunk in request.iter_content(chunk_size=1024):
            i = i + 1
            modFile.write(chunk)
            modFile.flush()
            mod.updateProgress(i, size/1024)
        modFile.close()
    print("end download\n")

# -----------
# Main code
# -----------

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    
    mod = ModItem("applied-energistics-2")
    mod.addToTree(ui.treeDownload)

    downloadThread = Thread(target = startDownload, args = (mod, ))
    downloadThread.start()
    
    sys.exit(app.exec_())

