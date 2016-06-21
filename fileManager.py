"""
Contains functions that manage low-level information saving and retrieval.

Also manages manifest files.
(I should really work on figuring out what manifests should do, considering how much time I spent writing those functions.)
"""
#Imports
import json
import os
import constants


#Initialize variables


def GetDataFromFile(filename):
	"""
Retrives JSON formatted data from a file and loads as a Python object.

Returns False if the requested file is unreadable.
	"""

	try:
		fileObj = open(filename, 'r')
	except IOError:
		return False
	data = json.load(fileObj)
	fileObj.close()
	return data



def SaveDataToFile(data, filename):
	"""
Saves a Python object in JSON format in the specified file.

Renames the current file as a backup, writes JSON encoded data to the specified file, and removes the backup.
Returns True if no errors are raised in the process, False if otherwise.
	"""

	filenameBackup = constants.BACKUP + filename

	try:
		os.rename(filename, filenameBackup)
		fileObj = open(filename)
		json.dump(data, fileObj)
		fileObj.close()
		os.remove(filenameBackup)
	except:
		return False
	return True


def appendDataToFile(data, filename):
	filenameBackup = constants.BACKUP + filename

	try:
		fileObj = open(filename, 'r')
	except IOError:
		return False

	try:
		oldData = json.load(fileObj)
	except:
		return False

	fileObj.close()

	oldData.update(data)
	newData = oldData

	try:
		fileObj = open(filename, 'w')
	except IOError:
		return False

	json.dump(newData)
	return True


def isManifest(overrideFile = None):
	"""
Checks whether a manifest file exists.
	"""
	if overrideFile:
		manifestLoc = overrideFile
	else:
		manifestLoc = constants.DEFAULTMANIFEST

	if not os.path.isfile(manifestLoc):
		return False
	
	try:
		fileObj = open(manifestLoc)
	except IOError:
		return False

	try:
		json.load(fileObj)
	except:
		fileObj.close()
		return False

	fileObj.close()
	return True



def getFileManifest(overrideFile = None):
	"""
Returns a list of files as a Python dictionary from a JSON encoded manifest file.

If file is unreadable or blank, it will return False.
	"""
	if overrideFile:
		manifestLoc = overrideFile
	else:
		manifestLoc = constants.DEFAULTMANIFEST

	if not isManifest(manifestLoc):
		return False

	data = json.load(fileObj)
	fileObj.close()
	return data


def createManifest(initialData = dict(), overrideFile = None):
	if overrideFile:
		manifestLoc = overrideFile
	else:
		manifestLoc = constants.DEFAULTMANIFEST

	if isManifest(manifestLoc):
		return False

	try:
		fileObj = open(manifestLoc)
	except:
		return False

	try:
		json.dump(initialData, fileObj)
	except:
		fileObj.close()
		return False

	return True


def writeManifest(data = dict(), overrideFile = None, ignoreMissing = False):
	"""
	Overwrites an existing manifest with new data.

	If called without the "data" argument set, will set the manifest to blank.
	Will return false if a manifest does not already exist and "ignoreMissing" is not true.
	"""
	if overrideFile:
		manifestLoc = overrideFile
	else:
		manifestLoc = constants.DEFAULTMANIFEST

	if not isManifest(manifestLoc):
		if ignoreMissing:
			createManifest(manifestLoc)
		else:
			return False

	try:
		fileObj = open(manifestLoc, 'w')
	except:
		return False

	json.dump(data, fileObj)

	fileObj.close()
	return True


def appendManifest(additionalData, overrideFile = None):
	"""
Appends additional data to an existing manifest.

Uses Python's dict().update() method,
meaning that duplicate keys in the old data and the new will be set to the new value.
	"""
	if overrideFile:
		manifestLoc = overrideFile
	else:
		manifestLoc = constants.DEFAULTMANIFEST

	if not isManifest(manifestLoc):
		return False

	currentManifestData = getFileManifest(manifestLoc)
	newManifestData = currentManifestData.copy()
	newManifestData.update(additionalData)

	return True

