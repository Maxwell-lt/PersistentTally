"""
Interface between GUI and fileManager.py
"""


#Imports
import constants
import fileManager

#Initialize Variables


def loadFileList():
	files = fileManager.getFileManifest()
	if files:
		return files
	else:
		return dict()


def addListFile():
	