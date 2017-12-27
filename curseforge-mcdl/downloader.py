from PyQt5 import QtWidgets, QtCore, QtGui
from requests import get
from os import path, mkdir
import hashlib

import cfscrapper

# ----------
# Mod Item
# ----------

class ModItem(object):
	def __init__(self, name, mcVersion, releasesOnly=True, mostRecent=False, list=None, downloadDir=None):
		self.name = name
		self.mcVersion = mcVersion
		self.releasesOnly = releasesOnly
		self.mostRecent = mostRecent
		self.list = list
		self.downloadLink = ""
		if downloadDir is not None:
			self.downloadDir = downloadDir
		else:
			self.downloadDir = path.dirname(path.abspath(__file__)).replace(path.sep, "/") + "/mods"

	def addToTree(self, tree):
		self.item = QtWidgets.QTreeWidgetItem(tree)
		self.item.setText(0, self.name)
		self.item.setText(1, "Starting")
	
	def startDownload(self):
		self.thread = DownloadThread(self.name, self.mcVersion, self.releasesOnly, self.mostRecent, self.list, self.downloadDir)
		self.thread.kept.connect(self.statusKept)
		self.thread.failed.connect(self.statusFailed)
		self.thread.downloading.connect(self.statusDownloading)
		self.thread.complete.connect(self.statusComplete)
		print(self.name + ": starting download")
		self.thread.start()
		self.thread.setPriority(QtCore.QThread.LowPriority)
	
	def statusKept(self):
		self.item.setText(1, "Kept")
		self.item.setIcon(1, QtGui.QIcon(path.dirname(path.abspath(__file__)).replace(path.sep, "/") + "/icons/kept.ico"))
	def statusFailed(self):
		self.item.setText(1, "Failed")
		self.item.setIcon(1, QtGui.QIcon(path.dirname(path.abspath(__file__)).replace(path.sep, "/") + "/icons/failed.ico"))
	def statusDownloading(self):
		self.item.setText(1, "Downloading")
	def statusComplete(self):
		self.item.setText(1, "Complete")
		self.item.setIcon(1, QtGui.QIcon(path.dirname(path.abspath(__file__)).replace(path.sep, "/") + "/icons/complete.ico"))

class DownloadThread(QtCore.QThread):
	kept = QtCore.pyqtSignal()
	failed = QtCore.pyqtSignal()
	downloading = QtCore.pyqtSignal()
	complete = QtCore.pyqtSignal()

	def __init__(self, name, mcVersion, releasesOnly, mostRecent, list, downloadDir):
		self.name = name
		self.mcVersion = mcVersion
		self.releasesOnly = releasesOnly
		self.mostRecent = mostRecent
		self.list = list
		self.downloadDir = downloadDir
		super().__init__()
	
	def run(self):
		dllink = cfscrapper.downloadLink(self.name, self.mcVersion, self.releasesOnly, self.mostRecent, self.list)
		if dllink is not None:
			if path.isfile(self.downloadDir + "/" + self.name + ".jar"):
				if cfscrapper.modFileMD5(dllink[0]) == md5Chunks(self.downloadDir + "/" + self.name + ".jar"):
					# File exists and is up to date
					#print(dllink[1] + ": up to date")
					self.kept.emit()
				else:
					# File exists, but is outdated/broken
					#print(dllink[1] + ": MD5 check NOT OK")
					self.downloading.emit()
					downloadJob(dllink[0], self.name + ".jar", self.downloadDir)
					self.complete.emit()
			else:
				# File does not exist
				self.downloading.emit()
				downloadJob(dllink[0], self.name + ".jar", self.downloadDir)
				self.complete.emit()
		else:
			# Couldn't get the download link
			self.failed.emit()
		
def downloadJob(url, outFile, downloadDir):
	request = get(url, stream=True)
	with open(downloadDir + "/" + outFile, "wb") as modFile:
		size = int(request.headers.get("content-length"))
		for chunk in request.iter_content(chunk_size=1024):
			modFile.write(chunk)
			modFile.flush()
		modFile.close()

def md5Chunks(filePath):
	md5 = hashlib.md5()
	with open(filePath, "rb") as file:
		for chunk in iter(lambda: file.read(4096), b""):
			md5.update(chunk)
	return md5.hexdigest()
