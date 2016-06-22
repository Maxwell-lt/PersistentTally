"""
Frontend Module, handles all GUI code and user interaction.
"""

#Imports
from tkinter import *
import dataHandler
import constants
import fileManager
import en_us

#Initialize Variables
root = Tk()



class startUpBox(Tk.frame):
	def __init__(self, master):
		self.master = master
		self.frame = Tk.frame(self.master)
		self.title(en_us.NAME)
		self.label = Label(self, en_us.STARTUPWIN.CHOOSE)
		self.dropdown = Listbox(self, fileManager.loadFiles())
		self.addNewButton = Button(self, en_us.STARTUPWIN.ADDNEW, command = self.newFileDialogOpener)

		self.label.pack()
		self.dropdown.pack()
		self.addNewButton.pack()

		self.frame.pack()

	def newFileDialogOpener(self):
		self.newFileDialog = Toplevel(self.master)
		self.newFileDialogWindow = newFileDialog(self.newFileDialog)


class newFileDialog(Tk.frame):
	def __init__(self, master):
		#Initiate Window
		self.master = master
		self.frame = Tk.frame(self.master)

		#Initiate Components
		self.title(en_us.ADDLISTDIALOG.NAME)
		self.inputPairContainer = LabelFrame(self.frame)
		self.label = Label(self.inputPairContainer, en_us.ADDLISTDIALOG.LABEL)
		self.textBox = Entry(self.inputPairContainer)
		self.submitButton = Button(self.frame, en_us.SUBMIT, command = self.submitPressed)
		
		#Pack Elements
		self.label.pack()
		self.textBox.pack()
		self.inputPairContainer.pack()
		self.submitButton.pack()
		self.frame.pack()

	def submitPressed(self):




		