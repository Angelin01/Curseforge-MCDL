# CurseForge-MC-ModDownloader
A python script for automatically downloading and updating mods from CurseForge for Minecraft.
Heavily inspired by [this other project](https://gitlab.com/C0rn3j/MCModUpdater/tree/master), which sadly wasn't working for me, so I wrote one from scratch.

# **Instructions**
You'll need, aside from Python 3, the following libraries: "bs4", "requests" and "clint".

Simply take a mod from curseforge and add it's name to a new line in modList.txt
For example: Actually Additions has the following link in CurseForge: https://minecraft.curseforge.com/projects/actually-additions.
Therefore, the mod name is "actually-additions" without quotes.
Lines starting with # are ignored.

Edit the version variable in the .py according to the game version you want the mod to be downloaded in. These can be found at the end of CurseForge files links when filtering.
For example, if you want only 1.11 mods, set it to "?filter-game-version=1738749986%3A599". Default is 1.10.
If you just want the latest version, leave it as "".

Run CurseForge-MC-ModDownloader.py and let it do it's thing :)

# **License**
This project is licensed under the terms of the GNU GPLv3 license.
Feel free to download, use, share, modify and do whatever you want with it.
