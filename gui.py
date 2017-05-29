from Tkinter import *
import Tkinter as tk

from tmdb3 import *

#Key zum benutzen der Datenbank von https://www.themoviedb.org/
set_key('46e474bac23e4add4ae3e4630bd0d7cf')

class GUI(object):

	def __init__(self, master):
		self.master = master
		self.frame = tk.Frame(self.master)
		#self.button1 = tk.Button(self.frame, text = 'New Window', width = 25, command = self.new_window)
		#self.button1.grid()
		self.frame.grid()
		self.createWidgets()

	def createWidgets(self):
		directorEntry = StringVar()
		writerEntry = StringVar()
		actorEntry = StringVar()
		
		self.label_1 = tk.Label(self.frame, text="Director")
		self.label_2 = tk.Label(self.frame, text="Writer")
		self.label_3 = tk.Label(self.frame, text="Actor")
		self.label_4 = tk.Label(self.frame, text="Genre")
		self.label_5 = tk.Label(self.frame, text="Budget")
		
		self.entry_1 = tk.Entry(self.frame, bd =5, textvariable = directorEntry)
		self.entry_2 = tk.Entry(self.frame, bd =5, textvariable = writerEntry)
		self.entry_3 = tk.Entry(self.frame, bd =5, textvariable = actorEntry)
		
		self.button_1 = tk.Button(self.frame, text = "send", width = 25, command = self.sendCommand)
		
		self.spinbox_1 = tk.Spinbox(self.frame, from_=0, to=10)
		
		self.listbox_1 = tk.Listbox(self.frame, selectmode=MULTIPLE)
		for line in range(100):
			self.listbox_1.insert(END, "This is Genre number " + str(line))
		
		self.label_1.grid(row=0)
		self.label_2.grid(row=1)
		self.label_3.grid(row=2)
		self.label_4.grid(row=3)
		self.label_5.grid(row=4)
		
		self.entry_1.grid(row=0, column=1)
		self.entry_2.grid(row=1, column=1)
		self.entry_3.grid(row=2, column=1)
		
		self.button_1.grid(row=10)
		
		self.spinbox_1.grid(row=4, column=1)
		
		self.listbox_1.grid(row=3, column=1)

	#Durchschnittsbewertung von Filmen mit Schauspieler X
	def averageActorRating(self):
		res = searchPerson(self.entry_3.get())
		counter = 0
		rating = 0
		for role in res[0].roles:
			if role.userrating > 0:
				rating = rating + role.userrating
				counter = counter + 1
			
		print rating / counter
		
	def new_window(self):
		self.newWindow = tk.Toplevel(self.master)
		self.app = NextWindow(self.newWindow)
	
	def sendCommand(self):
		self.averageActorRating()

class NextWindow(object):

	def __init__(self, master):
		self.master = master
		self.frame = tk.Frame(self.master)
		self.quitButton = tk.Button(self.frame, text = 'Quit', width = 25, command = self.close_windows)
		self.quitButton.grid()
		self.frame.grid()

	def close_windows(self):
		self.master.destroy()

def main(): 
	root = tk.Tk()
	root.title("Movie Success Prediction")
	app = GUI(root)
	root.mainloop()

if __name__ == '__main__':
	main()
		
		