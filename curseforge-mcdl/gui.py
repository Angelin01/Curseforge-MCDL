from PyQt5 import QtCore, QtGui, QtWidgets
from os import path, mkdir

import downloader
import cfscrapper
import sys

class Ui_MainWindow(object):
	def __init__(self, config=None):
		if config is None:
			self.modList = []
			self.downloadDir = path.dirname(path.abspath(__file__)).replace(path.sep, "/") + "/mods"
			self.importDir = path.dirname(path.abspath(__file__)).replace(path.sep, "/")
			self.exportDir = path.dirname(path.abspath(__file__)).replace(path.sep, "/")
			self.cmbMcIndex = 0
			self.mostRecent = False
			self.releasesOnly = True
			self.optionalDeps = False
		else:
			self.modList = config['General']['modlist'].split(',')
			self.downloadDir = config['General']['downloadDir']
			self.importDir = config['General']['importDir']
			self.exportDir = config['General']['exportDir']
			self.cmbMcIndex = int(config['General']['cmbMcIndex'])
			self.mostRecent = True if config['General']['mostRecent'] == 'True' else False
			self.releasesOnly = True if config['General']['releasesOnly'] == 'True' else False
			self.optionalDeps = True if config['General']['optionalDeps'] == 'True' else False
		
		self.modDownloadList = []
		self.modDependencyList = []
		self.toUpdateDependencyList = []
		self.waitThread = None

	def setupUi(self, MainWindow):
	
		# --------------------
		# Auto generated stuff
		# --------------------
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(720, 550)
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.treeDownload = QtWidgets.QTreeWidget(self.centralwidget)
		self.treeDownload.setGeometry(QtCore.QRect(470, 39, 240, 291))
		self.treeDownload.setIndentation(0)
		self.treeDownload.setHeaderHidden(True)
		self.treeDownload.setObjectName("treeDownload")
		item_0 = QtWidgets.QTreeWidgetItem(self.treeDownload)
		self.treeDownload.header().setVisible(False)
		self.listDownload = QtWidgets.QListWidget(self.centralwidget)
		self.listDownload.setGeometry(QtCore.QRect(10, 130, 191, 411))
		self.listDownload.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
		self.listDownload.setObjectName("listDownload")
		self.lblMods = QtWidgets.QLabel(self.centralwidget)
		self.lblMods.setGeometry(QtCore.QRect(10, 10, 91, 20))
		font = QtGui.QFont()
		font.setPointSize(12)
		self.lblMods.setFont(font)
		self.lblMods.setObjectName("lblMods")
		self.edtFilter = QtWidgets.QLineEdit(self.centralwidget)
		self.edtFilter.setGeometry(QtCore.QRect(10, 100, 125, 20))
		self.edtFilter.setObjectName("edtFilter")
		self.btnFilter = QtWidgets.QPushButton(self.centralwidget)
		self.btnFilter.setGeometry(QtCore.QRect(140, 100, 60, 23))
		self.btnFilter.setObjectName("btnFilter")
		self.lblDownloads = QtWidgets.QLabel(self.centralwidget)
		self.lblDownloads.setGeometry(QtCore.QRect(470, 10, 200, 20))
		font = QtGui.QFont()
		font.setPointSize(12)
		self.lblDownloads.setFont(font)
		self.lblDownloads.setObjectName("lblDownloads")
		self.grpImpExp = QtWidgets.QGroupBox(self.centralwidget)
		self.grpImpExp.setGeometry(QtCore.QRect(10, 40, 191, 50))
		self.grpImpExp.setObjectName("grpImpExp")
		self.btnImport = QtWidgets.QPushButton(self.grpImpExp)
		self.btnImport.setGeometry(QtCore.QRect(10, 20, 75, 23))
		self.btnImport.setObjectName("btnImport")
		self.btnExport = QtWidgets.QPushButton(self.grpImpExp)
		self.btnExport.setGeometry(QtCore.QRect(100, 20, 75, 23))
		self.btnExport.setObjectName("btnExport")
		self.grpNewMod = QtWidgets.QGroupBox(self.centralwidget)
		self.grpNewMod.setGeometry(QtCore.QRect(210, 40, 251, 51))
		self.grpNewMod.setObjectName("grpNewMod")
		self.edtAddMod = QtWidgets.QLineEdit(self.grpNewMod)
		self.edtAddMod.setGeometry(QtCore.QRect(10, 20, 161, 20))
		self.edtAddMod.setObjectName("edtAddMod")
		self.btnAddMod = QtWidgets.QPushButton(self.grpNewMod)
		self.btnAddMod.setGeometry(QtCore.QRect(180, 20, 61, 23))
		self.btnAddMod.setObjectName("btnAddMod")
		self.lblOptions = QtWidgets.QLabel(self.centralwidget)
		self.lblOptions.setGeometry(QtCore.QRect(220, 160, 61, 20))
		font = QtGui.QFont()
		font.setPointSize(12)
		self.lblOptions.setFont(font)
		self.lblOptions.setObjectName("lblOptions")
		self.grpModVersions = QtWidgets.QGroupBox(self.centralwidget)
		self.grpModVersions.setGeometry(QtCore.QRect(210, 250, 121, 71))
		self.grpModVersions.setObjectName("grpModVersions")
		self.radAll = QtWidgets.QRadioButton(self.grpModVersions)
		self.radAll.setGeometry(QtCore.QRect(10, 20, 82, 17))
		self.radAll.setObjectName("radAll")
		self.radReleases = QtWidgets.QRadioButton(self.grpModVersions)
		self.radReleases.setGeometry(QtCore.QRect(10, 40, 101, 17))
		self.radReleases.setObjectName("radReleases")
		self.grpDir = QtWidgets.QGroupBox(self.centralwidget)
		self.grpDir.setGeometry(QtCore.QRect(210, 330, 251, 70))
		self.grpDir.setObjectName("grpDir")
		self.lblDir = QtWidgets.QLabel(self.grpDir)
		self.lblDir.setGeometry(QtCore.QRect(10, 20, 231, 16))
		self.lblDir.setObjectName("lblDir")
		self.btnDir = QtWidgets.QPushButton(self.grpDir)
		self.btnDir.setGeometry(QtCore.QRect(10, 40, 100, 23))
		self.btnDir.setObjectName("btnDir")
		self.btnDownload = QtWidgets.QPushButton(self.centralwidget)
		self.btnDownload.setGeometry(QtCore.QRect(210, 490, 251, 51))
		self.btnDownload.setObjectName("btnDownload")
		self.grpMcVersion = QtWidgets.QGroupBox(self.centralwidget)
		self.grpMcVersion.setGeometry(QtCore.QRect(210, 190, 121, 51))
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
		self.grpRemMod.setGeometry(QtCore.QRect(210, 100, 251, 51))
		self.grpRemMod.setObjectName("grpRemMod")
		self.btnRemMod = QtWidgets.QPushButton(self.grpRemMod)
		self.btnRemMod.setGeometry(QtCore.QRect(10, 20, 101, 23))
		self.btnRemMod.setObjectName("btnRemMod")
		self.grpUpdate = QtWidgets.QGroupBox(self.centralwidget)
		self.grpUpdate.setGeometry(QtCore.QRect(210, 410, 251, 71))
		self.grpUpdate.setObjectName("grpUpdate")
		self.chkOptDeps = QtWidgets.QCheckBox(self.grpUpdate)
		self.chkOptDeps.setGeometry(QtCore.QRect(10, 20, 170, 17))
		self.chkOptDeps.setObjectName("chkOptDeps")
		self.btnUpdate = QtWidgets.QPushButton(self.grpUpdate)
		self.btnUpdate.setGeometry(QtCore.QRect(10, 40, 170, 23))
		self.btnUpdate.setObjectName("btnUpdate")
		self.txtConsole = QtWidgets.QTextBrowser(self.centralwidget)
		self.txtConsole.setGeometry(QtCore.QRect(470, 340, 241, 201))
		self.txtConsole.setObjectName("txtConsole")
		self.grpPriority = QtWidgets.QGroupBox(self.centralwidget)
		self.grpPriority.setGeometry(QtCore.QRect(340, 250, 121, 71))
		self.grpPriority.setObjectName("grpPriority")
		self.radRecent = QtWidgets.QRadioButton(self.grpPriority)
		self.radRecent.setGeometry(QtCore.QRect(10, 20, 82, 17))
		self.radRecent.setObjectName("radRecent")
		self.radStable = QtWidgets.QRadioButton(self.grpPriority)
		self.radStable.setGeometry(QtCore.QRect(10, 40, 82, 17))
		self.radStable.setObjectName("radStable")
		MainWindow.setCentralWidget(self.centralwidget)
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
		# Set starting selections
		self.modList = list(set(self.modList))
		for mod in self.modList:
			self.listDownload.addItem(mod)
			
		if self.cmbMcIndex >= 0 and self.cmbMcIndex <= 5:
			self.cmbMcVersion.setCurrentIndex(self.cmbMcIndex)
		else:
			self.cmbMcVersion.setCurrentIndex(0)
		
		if self.mostRecent == True:
			self.radRecent.setChecked(True)
		else:
			self.radStable.setChecked(True)
		
		if self.releasesOnly == True:
			self.radReleases.setChecked(True)
		else:
			self.radAll.setChecked(True)
			
		if self.optionalDeps == True:
			self.chkOptDeps.setChecked(True)
		
		# Download directory
		self.btnDir.clicked.connect(self.updateDir)
		
		# Add and remove mods
		self.btnAddMod.clicked.connect(self.addMod)
		self.edtAddMod.returnPressed.connect(self.addMod)
		self.btnRemMod.clicked.connect(self.remMod)
		
		# Import and export
		self.btnImport.clicked.connect(self.importFile)
		self.btnExport.clicked.connect(self.exportFile)
		
		# Update dependencies
		self.btnUpdate.clicked.connect(self.updateDependencies)

		# Download
		self.btnDownload.clicked.connect(self.startDownload)
		
		# Filter
		self.btnFilter.clicked.connect(self.filterMods)
		self.edtFilter.returnPressed.connect(self.filterMods)
		
		self.retranslateUi(MainWindow)

	def retranslateUi(self, MainWindow):
		# --------------------
		# Auto generated stuff
		# --------------------
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "Mod Downloader"))
		self.treeDownload.setSortingEnabled(False)
		self.treeDownload.headerItem().setText(0, _translate("MainWindow", "Progress bar"))
		self.treeDownload.headerItem().setText(1, _translate("MainWindow", "Mod name"))
		self.treeDownload.setIndentation(0)
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
		self.radReleases.setText(_translate("MainWindow", "Releases only"))
		self.grpDir.setTitle(_translate("MainWindow", "Download directory"))
		self.lblDir.setText(_translate("MainWindow", self.downloadDir)) # Starting downloader folder
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
		self.grpUpdate.setTitle(_translate("MainWindow", "Update dependencies for all mods"))
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
			print("ERROR: Mod already in mod list")
			return
		
		self.modList.append(modToAdd)
		self.listDownload.addItem(modToAdd)
		self.edtAddMod.clear()
		print("Successfully added mod " + modToAdd)
		
	def remMod(self):
		itemsToRem = self.listDownload.selectedItems()
		if len(itemsToRem) == 0:
			return
			
		for item in itemsToRem:
			self.modList.remove(item.text())
			self.listDownload.takeItem(self.listDownload.indexFromItem(item).row()) # Takes the row from the item's index after searching for the item again... This is so bad, why is there no remove
		print("Removed " + str(len(itemsToRem)) + " mods")
		
	def importFile(self):
		file = QtWidgets.QFileDialog.getOpenFileName(None, "Select mod list file", self.importDir)[0]
		if file == "": # User canceled
			return
			
		self.importDir = path.dirname(file)
		
		fileMods = open(file, 'r').readlines()
		for mod in fileMods:
			mod = mod.strip()
			if not mod.startswith('#') and mod != "" and mod not in self.modList:
				self.modList.append(mod)
				self.listDownload.addItem(mod)		
		
	def exportFile(self):
		file = QtWidgets.QFileDialog.getSaveFileName(None, "Select new mod list file", self.exportDir)[0]
		if file == "": # User canceled
			return
		# Overwrite warning is given by dialog itself, neat!
		
		self.exportDir = path.dirname(file)
			
		with open(file, 'w') as exportFile:
			for mod in self.modList:
				exportFile.write(mod + "\n")
				
	def startDownload(self):
		print("Downloading / Updating mods...")
		# Disable widgets
		self.edtAddMod.setEnabled(False)
		self.btnAddMod.setEnabled(False)
		self.btnRemMod.setEnabled(False)
		self.cmbMcVersion.setEnabled(False)
		self.radAll.setEnabled(False)
		self.radRecent.setEnabled(False)
		self.radReleases.setEnabled(False)
		self.radStable.setEnabled(False)
		self.btnDir.setEnabled(False)
		self.chkOptDeps.setEnabled(False)
		self.btnUpdate.setEnabled(False)
		self.btnDownload.setEnabled(False)
		
		self.modDownloadList = []
		self.treeDownload.clear()
		releasesOnly = self.radReleases.isChecked()
		mostRecent = self.radRecent.isChecked()
		downloadDir = self.downloadDir
		
		if path.exists(downloadDir) == False:
			mkdir(downloadDir)
		
		for item in self.modList:
			mod = downloader.ModItem(item, self.cmbMcVersion.currentText(), releasesOnly, mostRecent, None, downloadDir)
			self.modDownloadList.append(mod)
			mod.addToTree(self.treeDownload)
			mod.startDownload()
		self.waitThread = WaitThread(self.modDownloadList)
		self.waitThread.finished.connect(self.downloadsComplete)
		self.waitThread.start()
			
	def updateDir(self):
		directory = QtWidgets.QFileDialog.getExistingDirectory(None, "Select download directory", self.downloadDir)
		if directory == "":
			return
		
		self.downloadDir = directory
		self.lblDir.setText(directory)
		print("Download directory updated!")
		
	def downloadsComplete(self):
		# Reenable widgets
		self.edtAddMod.setEnabled(True)
		self.btnAddMod.setEnabled(True)
		self.btnRemMod.setEnabled(True)
		self.cmbMcVersion.setEnabled(True)
		self.radAll.setEnabled(True)
		self.radRecent.setEnabled(True)
		self.radReleases.setEnabled(True)
		self.radStable.setEnabled(True)
		self.btnDir.setEnabled(True)
		self.chkOptDeps.setEnabled(True)
		self.btnUpdate.setEnabled(True)
		self.btnDownload.setEnabled(True)
		print("DOWNLOADS COMPLETE!")
		
	def updateDependencies(self):
		print("Updating dependencies...")
		# Disable widgets
		self.edtAddMod.setEnabled(False)
		self.btnAddMod.setEnabled(False)
		self.btnRemMod.setEnabled(False)
		self.chkOptDeps.setEnabled(False)
		self.btnUpdate.setEnabled(False)
		self.btnDownload.setEnabled(False)
	
		self.modDependencyList = []
		self.toUpdateDependencyList = []
		optional = self.chkOptDeps.isChecked()
		for item in self.modList:
			mod = cfscrapper.ModItem(item, optional, self.toUpdateDependencyList)
			self.modDependencyList.append(mod)
			mod.startCheck()
		
		self.waitThread = WaitThread(self.modDependencyList)
		self.waitThread.finished.connect(self.checksComplete)
		self.waitThread.start()
			
	def checksComplete(self):
		# Reenable widgets
		self.edtAddMod.setEnabled(True)
		self.btnAddMod.setEnabled(True)
		self.btnRemMod.setEnabled(True)
		self.chkOptDeps.setEnabled(True)
		self.btnUpdate.setEnabled(True)
		self.btnDownload.setEnabled(True)
		for mod in self.toUpdateDependencyList:
			if mod not in self.modList:
				self.modList.append(mod)
				self.listDownload.addItem(mod)	
		print("DEPENDENCIES CHECK COMPLETE!")
		
	def filterMods(self):
		filterWord = self.edtFilter.text()
		filteredMods = []
		self.filteredMods = []
		self.listDownload.clear()
		
		for mod in self.modList:
			if filterWord in mod:
				filteredMods.append(mod)
		
		for mod in filteredMods:
			self.listDownload.addItem(mod)
		
class WaitThread(QtCore.QThread):
	def __init__(self, threadList):
		self.threadList = threadList
		super().__init__()
		
	def run(self):
		for item in self.threadList:
			item.thread.wait()
