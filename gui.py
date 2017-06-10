from Tkinter import *
import Tkinter as tk

from tmdb3 import *

from nltk import *

#Key zum benutzen der Datenbank von https://www.themoviedb.org/
set_key('46e474bac23e4add4ae3e4630bd0d7cf')

genre_list = Genre.getAll()
#print genre_list


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
		producerEntry = StringVar()
		actorEntry = StringVar()
		
		self.label_1 = tk.Label(self.frame, text="Director")
		self.label_2 = tk.Label(self.frame, text="Writer")
		self.label_3 = tk.Label(self.frame, text="Producer")
		self.label_4 = tk.Label(self.frame, text="Actor")
		self.label_5 = tk.Label(self.frame, text="Genre")
		self.label_6 = tk.Label(self.frame, text="Budget")
		
		self.entry_1 = tk.Entry(self.frame, bd =5, textvariable = directorEntry)
		self.entry_2 = tk.Entry(self.frame, bd =5, textvariable = writerEntry)
		self.entry_3 = tk.Entry(self.frame, bd =5, textvariable = producerEntry)
		self.entry_4 = tk.Entry(self.frame, bd =5, textvariable = actorEntry)
		
		self.button_1 = tk.Button(self.frame, text = "send", width = 25, command = self.sendCommand)
		
		self.spinbox_1 = tk.Spinbox(self.frame, from_=0, to=10)
		
		self.listbox_1 = tk.Listbox(self.frame, selectmode=MULTIPLE)
		for genre in genre_list:
			#self.listbox_1.insert(END, "This is Genre number " + str(line))
			self.listbox_1.insert(END,genre)
		
		self.label_1.grid(row=0)
		self.label_2.grid(row=1)
		self.label_3.grid(row=2)
		self.label_4.grid(row=3)
		self.label_5.grid(row=4)
		self.label_6.grid(row=5)
		
		self.entry_1.grid(row=0, column=1)
		self.entry_2.grid(row=1, column=1)
		self.entry_3.grid(row=2, column=1)
		self.entry_4.grid(row=3, column=1)
		
		self.button_1.grid(row=10)
		
		self.spinbox_1.grid(row=5, column=1)
		
		self.listbox_1.grid(row=4, column=1)

	#Durchschnittsbewertung von Filmen mit Schauspieler X
	def averageActorRating(self):
		counter = 0
		actor_rating = 0
		try:
			treffer_name = searchPerson(self.entry_4.get())
			for role in treffer_name[0].roles:
				if role.userrating > 0:
					actor_rating = actor_rating + role.userrating
					counter = counter + 1
			print "average userrating from Movies with " + treffer_name[0].name + " as " + "Actor: " + str(actor_rating / counter)
		except:
			print "Not found Actor"
			
	
	#Durchschnittsbewertung von Filmen mit Director X
	def averageDirectorRating(self):
		counter = 0
		director_rating = 0
		job_list = []
		title = ""
		
		#Suche in der DB nach Personen mit dem Namen X
		treffer_name = searchPerson(self.entry_1.get())
		
		#Tokenizer der nur Woerter akzeptiert
		tokenizer = RegexpTokenizer(r'\w+')
		
		#Filtert die Filme bei denen X Director war
		for element in treffer_name[0].crew:
			job = tokenizer.tokenize(str(element))
			job.pop(-1)
			job.pop(0)
			job.pop(1)
			
			if job[0] == "Director":
				job_list.append(job)
		
		for job in job_list:
			for i in range(1, len(job)):
				title = title + " " + str(job[i])
			job[1] = title
			title = ""
			#print job[0:2]
			
		#Berechnet das Durchschnittsrating von allen Filmen, wo X Director war	
		for job in job_list:
			try:
				treffer_film = searchMovie(job[1])
				if treffer_film[0].userrating > 0:
					director_rating = director_rating + treffer_film[0].userrating
					counter = counter + 1
			except:
				continue
		print "average userrating from Movies with " + treffer_name[0].name + " as " + "Director: " + str(director_rating / counter)
	
	#Durchschnittsbewertung von Filmen mit Writer X
	def averageWriterRating(self):
		treffer_name = searchPerson(self.entry_2.get())
		counter = 0
		writer_rating = 0
		job_list = []
		tokenizer = RegexpTokenizer(r'\w+')
		title = ""
		
		for element in treffer_name[0].crew:
			job = tokenizer.tokenize(str(element))
			job.pop(-1)
			job.pop(0)
			job.pop(1)
			
			if job[0] == "Writer":
				job_list.append(job)
		
		for job in job_list:
			for i in range(1, len(job)):
				title = title + " " + str(job[i])
			job[1] = title
			title = ""
			#print job[0:2]
			
			
		for job in job_list:
			try:
				treffer_film = searchMovie(job[1])
				if treffer_film[0].userrating > 0:
					writer_rating = writer_rating + treffer_film[0].userrating
					counter = counter + 1
			except:
				continue
		print "average userrating from Movies with " + treffer_name[0].name + " as " + "Writer: " + str(writer_rating / counter)
		
	#Durchschnittsbewertung von Filmen mit Producer X
	def averageProducerRating(self):
		treffer_name = searchPerson(self.entry_3.get())
		counter = 0
		producer_rating = 0
		job_list = []
		tokenizer = RegexpTokenizer(r'\w+')
		title = ""
		
		for element in treffer_name[0].crew:
			job = tokenizer.tokenize(str(element))
			job.pop(-1)
			job.pop(0)
			job.pop(1)
			
			if job[0] == "Producer":
				job_list.append(job)
		
		for job in job_list:
			for i in range(1, len(job)):
				title = title + " " + str(job[i])
			job[1] = title
			title = ""
			#print job[0:2]
			
			
		for job in job_list:
			try:
				treffer_film = searchMovie(job[1])
				if treffer_film[0].userrating > 0:
					producer_rating = producer_rating + treffer_film[0].userrating
					counter = counter + 1
			except:
				continue
		print "average userrating from Movies with " + treffer_name[0].name + " as " + "Producer: " + str(producer_rating / counter)
	
	def new_window(self):
		self.newWindow = tk.Toplevel(self.master)
		self.app = NextWindow(self.newWindow)
	
	def sendCommand(self):
		try:
			self.averageActorRating()
		except:
			print "Please insert Producer"
		try:
			self.averageDirectorRating()
		except:
			print "Please insert Director"
		try:
			self.averageWriterRating()
		except:
			print "Please insert Writer"
		try:
			self.averageProducerRating()
		except:
			print "Please insert Producer"
		
		
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
		
		