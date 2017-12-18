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
        self.downloadLink = cfscrapper.downloadLink(name, mcVersion, releasesOnly, mostRecent, list)
        self.fileName = name + ".jar" # falta catar nome do arquivo
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

class DownloadThread(QtCore.QThread):
    def __init__(self, mod):
        self.mod = mod
        QtCore.QThread.__init__(self)

    def __del__(self):
        self.wait()

    def run(self):
        if path.exists("./mods") == False:
            mkdir("mods")
        
        request = get(self.mod.downloadLink, stream=True)
        with open("./mods/" + self.mod.fileName, "wb") as modFile:
            size = int(request.headers.get("content-length"))
            self.mod.updateProgress(0, size)
            i = 0
            for chunk in request.iter_content(chunk_size=1024):
                i = i + 1
                modFile.write(chunk)
                modFile.flush()
                self.mod.updateProgress(i, size/1024)
            modFile.close()

