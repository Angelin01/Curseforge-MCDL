# CurseForge-MCDL
A python program for automatically downloading and updating mods from CurseForge for Minecraft.

# **Instructions**

Simply take a mod from CurseForge and add it's name to the list.
For example: Actually Additions has the following link in CurseForge: https://minecraft.curseforge.com/projects/actually-additions.
Therefore, the mod name is "actually-additions" without quotes.

Selecting a mod (or multiple mods) from the list and clicking update dependencies will check Curseforge for the required mod dependencies and automatically add them to the mod list. If you select the "optional dependencies" checkbox, those will also be downloaded.

You can remove a mod (or multiple mods) from the list by selecting them and clicking remove mods.

You can also use many filters, like Minecraft Versions, which release types to download and to prioritize most recent file or the most recent stable version only.

You can also put the file names in a file and import (or export) the mod list.
The file format is simple: one mod name per line, nothing else. Lines starting with # are ignored.


