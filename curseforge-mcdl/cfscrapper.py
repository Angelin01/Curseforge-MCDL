from urllib.request import urlopen
from bs4 import BeautifulSoup
from threading import Lock

# "list" variables are for threading. If passed, functions will add their results to the list

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
	filter = {
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
	
	webpage = BeautifulSoup(urlopen("https://minecraft.curseforge.com/projects/" + modName + "/files?" + filter + sort), "html.parser")
	
	# Download links are found in "overflow-tip" classes
	if releasesOnly is True:
		# The class "release-phase" is used to mark releases, find the parent's parent and only then search for "overflow-tip"
		fileNumber = webpage.find("div", class_="release-phase").parent.parent.find("a", class_="overflow-tip")["href"].rsplit('/', 1)[-1]
	else:
		fileNumber = webpage.find("a", class_="overflow-tip")["href"].rsplit('/', 1)[-1]
		
	downloadLink = "https://minecraft.curseforge.com/projects/" + modName + "/files/" + fileNumber + "/download"
	if list is not None:
		downloadLock.acquire()
		list.append(downloadLink)
		downloadLock.release()
	
	return(downloadLink)
	
def modFileMD5(downloadLink):
	webpage = BeautifulSoup(urlopen(downloadLink.rsplit('/', 1)[0]), "html.parser")
	return(webpage.find("span", class_="md5").string)
	







