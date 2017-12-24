from PyQt5 import QtCore
from urllib.request import urlopen
from bs4 import BeautifulSoup
from threading import Lock

# "list" variables are for threading. If passed, functions will add their results to the list

class ModItem(object):
	def __init__(self, name, optional, dependencyList):
		self.thread = DependecyThread(name, optional, dependencyList)
		self.name = name
		
	def startCheck(self):
		print(self.name + ": dependency check starting")
		self.thread.start()
		
class DependecyThread(QtCore.QThread):
	def __init__(self, name, optional, dependencyList):
		self.name = name
		self.optional = optional
		self.dependencyList = dependencyList
		super().__init__()
		
	def run(self):
		checkDependencies(self.name, self.optional, self.dependencyList)
		print(self.name + ": dependency check complete")

depLock = Lock()
def checkDependencies(modName, optional, list=None):
	try:
	# Webpage consists of https://minecraft.curseforge.com/projects/modName/relations/dependencies[?filter-related-dependencies=3] (the last part will only grab required libraries)
		parsed = BeautifulSoup(urlopen("https://minecraft.curseforge.com/projects/" + modName + "/relations/dependencies" + ("?filter-related-dependencies=3" if not optional else "")), 'html.parser')
	except:
		print("Mod URL for " + modName + "doesn't exist")
		return([])
	
	dependencyList = []
	
	# Download links for dependencies are found in divs with classes 'name-wrapper'
	dependencies = parsed.find_all("div", class_="name-wrapper")
	for item in dependencies:
		dependencyList.append(item.find("a")["href"].rsplit('/', 1)[-1]) # Element href inside the a, take the contents after the last slash
			
	if list is not None:
		depLock.acquire()
		list.extend(dependencyList)
		depLock.release()
	
	return(dependencyList)

# mostRecent = True for most recent, False will prioritize stable releases first
# releasesOnly = True for only releases, False will allow it to download alphas and betas

downloadLock = Lock()
def downloadLink(modName, mcVersion, releasesOnly=True, mostRecent=False, list=None):
	versionFilter = {
		"1.12.2": "filter-game-version=1738749986%3A628",
		"1.11.2": "filter-game-version=1738749986%3A599",
		"1.10.2": "filter-game-version=1738749986%3A572",
		"1.9.4": "filter-game-version=1738749986%3A552",
		"1.8.9": "filter-game-version=1738749986%3A4",
		"1.7.10": "filter-game-version=1738749986%3A5"
	}.get(mcVersion, "1.12.2")
	if mostRecent is True:
		sort = "&sort=-datecreated"
	else:
		sort = "&sort=releasetype"

	try:
		webpage = BeautifulSoup(urlopen("https://minecraft.curseforge.com/projects/" + modName + "/files?" + versionFilter + sort), "html.parser")
	except:
		print("Could not find download link for " + modName)
		return(None)

	# Download links are found in "overflow-tip" classes
	if releasesOnly is True:
		# The class "release-phase" is used to mark releases, find the parent's parent and only then search for "overflow-tip"
		file = webpage.find("div", class_="release-phase")
		if file is None:
			print("Mod " + modName + " has no release-phase version available for " + mcVersion)
			return(None)
		file = file.parent.parent.find("a", class_="overflow-tip")	
	else:
		file = webpage.find("a", class_="overflow-tip")
		if file is None:
			print("Mod " + modName + " has no downloads available for " + mcVersion)
			return(None)
		
	downloadLink = "https://minecraft.curseforge.com/projects/" + modName + "/files/" + file["href"].rsplit('/', 1)[-1] + "/download"
	fileName = file.getText().replace(".jar", "") + ".jar" # Fixes files with no .jar, could break if file has .jar in the middle but...
	if list is not None:
		downloadLock.acquire()
		list.append(downloadLink)
		downloadLock.release()

	return(downloadLink, fileName)
	
def modFileMD5(downloadLink):
	webpage = BeautifulSoup(urlopen(downloadLink.rsplit('/', 1)[0]), "html.parser")
	return(webpage.find("span", class_="md5").string)
	
def modExists(modName):
	try:
		urllib.request.urlopen("https://minecraft.curseforge.com/projects/" + modName)
	except urllib.error.HTTPError: 
		return(False)
	return(True)