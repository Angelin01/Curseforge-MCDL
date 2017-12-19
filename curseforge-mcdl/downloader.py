from PyQt5 import QtWidgets, QtCore
from requests import get
from os import path, mkdir

import cfscrapper

# ----------
# Mod Item
# ----------

class ModItem(object):
	def __init__(self, name, mcVersion, releasesOnly=True, mostRecent=False, list=None):
		self.name = name
		self.mcVersion = mcVersion
		self.releasesOnly = releasesOnly
		self.mostRecent = mostRecent
		self.list = list
		self.downloadLink = ""

	def addToTree(self, tree):
		self.item = QtWidgets.QTreeWidgetItem(tree)
		self.item.setText(0, self.name)
		self.item.setText(1, "Starting")
	
	def startDownload(self):
		self.thread = DownloadThread(self.name, self.mcVersion, self.releasesOnly, self.mostRecent, self.list)
		self.thread.kept.connect(self.statusKept)
		self.thread.failed.connect(self.statusFailed)
		self.thread.downloading.connect(self.statusDownloading)
		self.thread.complete.connect(self.statusComplete)
		self.thread.start()
	
	def statusKept(self):
		self.item.setText(1, "Kept")
	def statusFailed(self):
		self.item.setText(1, "Failed")
	def statusDownloading(self):
		self.item.setText(1, "Downloading")
	def statusComplete(self):
		self.item.setText(1, "Complete")

class DownloadThread(QtCore.QThread):
	kept = QtCore.pyqtSignal()
	failed = QtCore.pyqtSignal()
	downloading = QtCore.pyqtSignal()
	complete = QtCore.pyqtSignal()

	def __init__(self, name, mcVersion, releasesOnly, mostRecent, list):
		self.name = name
		self.mcVersion = mcVersion
		self.releasesOnly = releasesOnly
		self.mostRecent = mostRecent
		self.list = list
		QtCore.QThread.__init__(self)
	
	def run(self):
		dllink = cfscrapper.downloadLink(self.name, self.mcVersion, self.releasesOnly, self.mostRecent, self.list)
		if dllink is not None:
			self.downloading.emit()
			downloadJob(dllink[0], dllink[1])
			self.complete.emit()
		else:
			self.failed.emit()
		
def downloadJob(url, outFile):
	if path.exists("./mods") == False:
		mkdir("mods")
	
	print(outFile + ": starting download")
	request = get(url, stream=True)
	with open("./mods/" + outFile, "wb") as modFile:
		size = int(request.headers.get("content-length"))
		for chunk in request.iter_content(chunk_size=1024):
			modFile.write(chunk)
			modFile.flush()
		modFile.close()
	print(outFile + ": download finished")

