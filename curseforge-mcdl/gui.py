from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
	
		# --------------------
		# Auto generated stuff
		# --------------------
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(612, 538)
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.treeDownload = QtWidgets.QTreeWidget(self.centralwidget)
		self.treeDownload.setGeometry(QtCore.QRect(220, 40, 240, 270))
		self.treeDownload.setHeaderHidden(True)
		self.treeDownload.setObjectName("treeDownload")
		self.treeDownload.header().setVisible(False)
		self.listDownload = QtWidgets.QListWidget(self.centralwidget)
		self.listDownload.setGeometry(QtCore.QRect(10, 70, 191, 391))
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
		self.grpImpExp.setGeometry(QtCore.QRect(10, 470, 191, 50))
		self.grpImpExp.setObjectName("grpImpExp")
		self.btnImport = QtWidgets.QPushButton(self.grpImpExp)
		self.btnImport.setGeometry(QtCore.QRect(10, 20, 75, 23))
		self.btnImport.setObjectName("btnImport")
		self.btnExport = QtWidgets.QPushButton(self.grpImpExp)
		self.btnExport.setGeometry(QtCore.QRect(100, 20, 75, 23))
		self.btnExport.setObjectName("btnExport")
		self.grpNewMod = QtWidgets.QGroupBox(self.centralwidget)
		self.grpNewMod.setGeometry(QtCore.QRect(220, 320, 241, 51))
		self.grpNewMod.setObjectName("grpNewMod")
		self.edtAddMod = QtWidgets.QLineEdit(self.grpNewMod)
		self.edtAddMod.setGeometry(QtCore.QRect(10, 20, 151, 20))
		self.edtAddMod.setObjectName("edtAddMod")
		self.btnAddMod = QtWidgets.QPushButton(self.grpNewMod)
		self.btnAddMod.setGeometry(QtCore.QRect(170, 20, 61, 23))
		self.btnAddMod.setObjectName("btnAddMod")
		self.lblOptions = QtWidgets.QLabel(self.centralwidget)
		self.lblOptions.setGeometry(QtCore.QRect(490, 10, 200, 20))
		font = QtGui.QFont()
		font.setPointSize(12)
		self.lblOptions.setFont(font)
		self.lblOptions.setObjectName("lblOptions")
		self.grpModVersions = QtWidgets.QGroupBox(self.centralwidget)
		self.grpModVersions.setGeometry(QtCore.QRect(480, 100, 121, 71))
		self.grpModVersions.setObjectName("grpModVersions")
		self.radAll = QtWidgets.QRadioButton(self.grpModVersions)
		self.radAll.setGeometry(QtCore.QRect(10, 20, 82, 17))
		self.radAll.setObjectName("radAll")
		self.radioReleases = QtWidgets.QRadioButton(self.grpModVersions)
		self.radioReleases.setGeometry(QtCore.QRect(10, 40, 101, 17))
		self.radioReleases.setObjectName("radioReleases")
		self.grpDir = QtWidgets.QGroupBox(self.centralwidget)
		self.grpDir.setGeometry(QtCore.QRect(480, 260, 121, 70))
		self.grpDir.setObjectName("grpDir")
		self.lblDir = QtWidgets.QLabel(self.grpDir)
		self.lblDir.setGeometry(QtCore.QRect(10, 20, 170, 13))
		self.lblDir.setObjectName("lblDir")
		self.btnDir = QtWidgets.QPushButton(self.grpDir)
		self.btnDir.setGeometry(QtCore.QRect(10, 40, 100, 23))
		self.btnDir.setObjectName("btnDir")
		self.btnDownload = QtWidgets.QPushButton(self.centralwidget)
		self.btnDownload.setGeometry(QtCore.QRect(350, 470, 111, 51))
		self.btnDownload.setObjectName("btnDownload")
		self.grpMcVersion = QtWidgets.QGroupBox(self.centralwidget)
		self.grpMcVersion.setGeometry(QtCore.QRect(480, 40, 121, 51))
		self.grpMcVersion.setObjectName("grpMcVersion")
		self.cmbMcVersion = QtWidgets.QComboBox(self.grpMcVersion)
		self.cmbMcVersion.setGeometry(QtCore.QRect(10, 20, 69, 22))
		self.cmbMcVersion.setObjectName("cmbMcVersion")
		self.cmbMcVersion.addItem("")
		self.cmbMcVersion.addItem("")
		self.cmbMcVersion.addItem("")
		self.cmbMcVersion.addItem("")
		self.cmbMcVersion.addItem("")
		self.cmbMcVersion.addItem("")
		self.grpRemMod = QtWidgets.QGroupBox(self.centralwidget)
		self.grpRemMod.setGeometry(QtCore.QRect(220, 470, 121, 51))
		self.grpRemMod.setObjectName("grpRemMod")
		self.btnRemMod = QtWidgets.QPushButton(self.grpRemMod)
		self.btnRemMod.setGeometry(QtCore.QRect(10, 20, 75, 23))
		self.btnRemMod.setObjectName("btnRemMod")
		self.grpUpdate = QtWidgets.QGroupBox(self.centralwidget)
		self.grpUpdate.setGeometry(QtCore.QRect(220, 380, 241, 80))
		self.grpUpdate.setObjectName("grpUpdate")
		self.chkOptDeps = QtWidgets.QCheckBox(self.grpUpdate)
		self.chkOptDeps.setGeometry(QtCore.QRect(10, 20, 170, 17))
		self.chkOptDeps.setObjectName("chkOptDeps")
		self.btnUpdate = QtWidgets.QPushButton(self.grpUpdate)
		self.btnUpdate.setGeometry(QtCore.QRect(10, 40, 170, 23))
		self.btnUpdate.setObjectName("btnUpdate")
		self.txtConsole = QtWidgets.QTextBrowser(self.centralwidget)
		self.txtConsole.setGeometry(QtCore.QRect(480, 340, 121, 181))
		self.txtConsole.setObjectName("txtConsole")
		self.grpPriority = QtWidgets.QGroupBox(self.centralwidget)
		self.grpPriority.setGeometry(QtCore.QRect(480, 180, 121, 71))
		self.grpPriority.setObjectName("grpPriority")
		self.radRecent = QtWidgets.QRadioButton(self.grpPriority)
		self.radRecent.setGeometry(QtCore.QRect(10, 20, 82, 17))
		self.radRecent.setObjectName("radRecent")
		self.radStable = QtWidgets.QRadioButton(self.grpPriority)
		self.radStable.setGeometry(QtCore.QRect(10, 40, 82, 17))
		self.radStable.setObjectName("radStable")
		MainWindow.setCentralWidget(self.centralwidget)

		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)
		MainWindow.setTabOrder(self.edtFilter, self.btnFilter)
		MainWindow.setTabOrder(self.btnFilter, self.listDownload)
		MainWindow.setTabOrder(self.listDownload, self.btnImport)
		MainWindow.setTabOrder(self.btnImport, self.btnExport)
		MainWindow.setTabOrder(self.btnExport, self.treeDownload)
		MainWindow.setTabOrder(self.treeDownload, self.edtAddMod)
		MainWindow.setTabOrder(self.edtAddMod, self.btnAddMod)
		MainWindow.setTabOrder(self.btnAddMod, self.chkOptDeps)
		MainWindow.setTabOrder(self.chkOptDeps, self.btnUpdate)
		MainWindow.setTabOrder(self.btnUpdate, self.btnRemMod)
		MainWindow.setTabOrder(self.btnRemMod, self.cmbMcVersion)
		MainWindow.setTabOrder(self.cmbMcVersion, self.btnDir)
		MainWindow.setTabOrder(self.btnDir, self.btnDownload)
		
		# --------------------
		# Manually added stuff
		# --------------------
		self.modList = [] # Temp, should auto import from file in the future
		self.btnAddMod.clicked.connect(self.addMod)
		self.edtAddMod.returnPressed.connect(self.addMod)
		self.btnRemMod.clicked.connect(self.remMod)
		self.btnImport.clicked.connect(self.importFile)

	def retranslateUi(self, MainWindow):
		# --------------------
		# Auto generated stuff
		# --------------------
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "Mod Downloader"))
		self.treeDownload.setSortingEnabled(False)
		self.treeDownload.headerItem().setText(0, _translate("MainWindow", "Progress bar"))
		self.treeDownload.headerItem().setText(1, _translate("MainWindow", "Mod name"))
		self.lblMods.setText(_translate("MainWindow", "Mod list"))
		self.btnFilter.setText(_translate("MainWindow", "Filter"))
		self.lblDownloads.setText(_translate("MainWindow", "Download progress"))
		self.grpImpExp.setTitle(_translate("MainWindow", "Mod list file import or export"))
		self.btnImport.setText(_translate("MainWindow", "Import"))
		self.btnExport.setText(_translate("MainWindow", "Export"))
		self.grpNewMod.setTitle(_translate("MainWindow", "Add new mod"))
		self.btnAddMod.setText(_translate("MainWindow", "Add mod"))
		self.lblOptions.setText(_translate("MainWindow", "Options"))
		self.grpModVersions.setTitle(_translate("MainWindow", "Mod Versions"))
		self.radAll.setText(_translate("MainWindow", "All types"))
		self.radioReleases.setText(_translate("MainWindow", "Releases only"))
		self.grpDir.setTitle(_translate("MainWindow", "Download directory"))
		self.lblDir.setText(_translate("MainWindow", "D:\\Download\\mods"))
		self.btnDir.setText(_translate("MainWindow", "Select directory..."))
		self.btnDownload.setText(_translate("MainWindow", "Start\nDownload / Update"))
		self.grpMcVersion.setTitle(_translate("MainWindow", "Minecraft Version"))
		self.cmbMcVersion.setItemText(0, _translate("MainWindow", "1.12.2"))
		self.cmbMcVersion.setItemText(1, _translate("MainWindow", "1.11.2"))
		self.cmbMcVersion.setItemText(2, _translate("MainWindow", "1.10.2"))
		self.cmbMcVersion.setItemText(3, _translate("MainWindow", "1.9.4"))
		self.cmbMcVersion.setItemText(4, _translate("MainWindow", "1.8.9"))
		self.cmbMcVersion.setItemText(5, _translate("MainWindow", "1.7.10"))
		self.grpRemMod.setTitle(_translate("MainWindow", "Remove selected mods"))
		self.btnRemMod.setText(_translate("MainWindow", "Remove Mods"))
		self.grpUpdate.setTitle(_translate("MainWindow", "Update depencies for selected mods"))
		self.chkOptDeps.setText(_translate("MainWindow", "Include optional dependencies"))
		self.btnUpdate.setText(_translate("MainWindow", "Update dependencies"))
		self.grpPriority.setTitle(_translate("MainWindow", "Priority"))
		self.radRecent.setText(_translate("MainWindow", "Most recent"))
		self.radStable.setText(_translate("MainWindow", "Most stable"))

	
	# Add and remove mods
	def addMod(self):
		modToAdd = self.edtAddMod.text()
		if modToAdd == "":
			return
		
		if modToAdd in self.modList:
			# Pop an error? 
			return
		
		self.modList.append(modToAdd)
		self.listDownload.addItem(modToAdd)
		self.edtAddMod.clear()
		
	def remMod(self):
		itemsToRem = self.listDownload.selectedItems()
		if len(itemsToRem) == 0:
			return
			
		for item in itemsToRem:
			self.modList.remove(item.text())
			self.listDownload.takeItem(self.listDownload.indexFromItem(item).row()) # Takes the row from the item's index after searching for the item again... This is so bad, why is there no remove
			
	def importFile(self):
		file = QtWidgets.QFileDialog.getOpenFileName()[0]
		if file == "":
			return
		
		fileMods = open(file, 'r').readlines()
		for mod in fileMods:
			mod = mod.strip()
			if not mod.startswith('#') and mod.strip() not in self.modList:
				self.modList.append(mod)
				self.listDownload.addItem(mod)		
		
		
if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())