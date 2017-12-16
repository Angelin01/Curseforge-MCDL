from urllib.request import urlopen
from bs4 import BeautifulSoup
from threading import Lock

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