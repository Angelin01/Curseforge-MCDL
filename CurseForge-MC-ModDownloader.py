from urllib.request import urlopen
from bs4 import BeautifulSoup # Não é default
from requests import get # Não é default
from clint.textui import progress # Não é default
from os import remove
from os import path
from os import mkdir


# Seta versão filtro, parte final do link, deixar como "" se vazio
version = "?filter-game-version=1738749986%3A572" # 1.10

modList = open('modList.txt','r')

# Criar history.txt e pasta mods se não existem
if path.exists('history.txt') == False:
    open('history.txt','w').close()
	
if path.exists('./mods') == False:
	mkdir('mods')

# Abre e le o histórico
oldHistory = open('history.txt','r')
line2 = oldHistory.readlines()
oldHistory.close() # Fecha o histórico, o velho não é mais utilizado

# Novo histórico criado
newHistory = open('history.txt','w+')

line1 = modList.readlines()

# Andando pela lista
for line1s in line1:
	li = line1s.strip() # Abre em characters
	if not li.startswith("#"): # Checa se não está comentado
		modName = line1s.rstrip().lstrip()#r/lstrip remove por default whitespace characters, como CR e LF
		link = 'https://minecraft.curseforge.com/projects/' + modName + '/files' + version 
		
		try:
			webpage = urlopen(link) #Cata o link
		except:
			print("Error getting URL for " + modName)
			continue
		
		hmmSopa = BeautifulSoup(webpage, 'html.parser') # Parsea o link, pra ele ser parsa e n treta com os trem, moro mano?
		try:
			download = hmmSopa.find("div",class_='project-file-name-container').find("a",class_="overflow-tip") # class eh reservado no Python, dai usa "class_" e como é só o primeiro elemento, find() em vez de find_all()
		except:
			print("Couldn't find a download for " + modName + " for the specified version")
			continue
		
		found = False # Pra saber se tem que escrever entry nova na lista ou não
		for line2s in line2: # Pesquisa no histórico antigo
			if modName in line2s:
				found = True 
				currentFile = line2s.split(",",1)[1].rstrip() # Quebra histórico no meio
				
				if currentFile == download.getText().rstrip(".jar"): # Se mod já ta atualizado, mantém.
					print(modName + " is up-to-date")
					newHistory.write(modName + "," + currentFile+"\n") # Atualiza histórico
					break
					
				else: # Senão, cata novo
					print(modName + " is outdated, downloading...")
					newHistory.write(modName + "," + download.getText().rstrip(".jar")+"\n") # Atualiza histórico
					
					#downloading stuff CURRENTLY SLOWish
					request = get("https://minecraft.curseforge.com"+download["href"]+"/download") # Link + a parte de download + /download pra baixar direto
					with open("./mods/" + download.getText().rstrip(".jar")+".jar",'wb') as downloadedMod: # Esse strip e adiciona é pra garantir que não vai ficar sem .jar ou com .jar extra
						total_length = int(request.headers.get('content-length'))
						for data in progress.bar(request.iter_content(chunk_size=1024), expected_size=(total_length/1024) + 1):
							downloadedMod.write(data)
							downloadedMod.flush()
							
					#delete old stuff
					try:
						remove("./mods/"+currentFile+".jar")
					except:
						print("Error deleting last file. Maybe it has already been deleted? Ignoring and continuing")
					break
					
		if found == False: # Não achou, escreve novo trequinho no histórico
			print(modName + " isn't present on the history, downloading... ")
			newHistory.write(modName+","+download.getText().rstrip(".jar")+"\n") # Atualiza histórico
			#downloading stuff CURRENTLY SLOWish
			request = get("https://minecraft.curseforge.com"+download["href"]+"/download") # Link + a parte de download + /download pra baixar direto
			with open("./mods/" + download.getText().rstrip(".jar")+".jar",'wb') as downloadedMod: # Esse strip e adiciona é pra garantir que não vai ficar sem .jar ou com .jar extra
				total_length = int(request.headers.get('content-length'))
				for data in progress.bar(request.iter_content(chunk_size=1024), expected_size=(total_length/1024) + 1):
					downloadedMod.write(data)
					downloadedMod.flush()
		
newHistory.close() # Fecha pra salvar o arquivo
modList.close()
