from PyQt5 import QtWidgets, QtCore
from requests import get
from os import path, mkdir
from threading import Thread

import cfscrapper

# ----------
# Mod Item
# ----------

class ModItem(object):
	def __init__(self, name, mcVersion, releasesOnly=True, mostRecent=False, list=None):
		self.name = name
		self.downloadLink = cfscrapper.downloadLink(name, mcVersion, releasesOnly, mostRecent, list)
		self.fileName = name + ".jar" # falta catar nome do arquivo

	def addToTree(self, tree):
		self.item = QtWidgets.QTreeWidgetItem(tree)
		self.item.setText(0, self.name)
		self.item.setText(1, "Downloading")
	
	def startDownload(self):
		self.thread = DownloadThread(self.downloadLink, self.fileName)
		self.thread.finished.connect(self.onFinish)
		self.thread.start()
	
	def onFinish(self):
		self.item.setText(1, "Complete")

class DownloadThread(QtCore.QThread):
	def __init__(self, url, outFile):
		self.url = url
		self.outFile = outFile
		QtCore.QThread.__init__(self)
	
	def run(self):
		downloadThread(self.url, self.outFile)
		
def downloadThread(url, outFile):
	if path.exists("./mods") == False:
		mkdir("mods")
	
	print(outFile + ": starting download")
	request = get(url, stream=True)
	with open("./mods/" + outFile, "wb") as modFile:
		size = int(request.headers.get("content-length"))
		i = 0
		for chunk in request.iter_content(chunk_size=1024):
			i = i + 1
			modFile.write(chunk)
			modFile.flush()
		modFile.close()
	print(outFile + ": download finished")

