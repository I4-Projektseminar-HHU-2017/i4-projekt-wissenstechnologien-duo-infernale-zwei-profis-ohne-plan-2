from Tkinter import *
import Tkinter as tk

from tmdb3 import *

from nltk import *

import numpy as np

#Key zum benutzen der Datenbank von https://www.themoviedb.org/
set_key('46e474bac23e4add4ae3e4630bd0d7cf')

genre_dic = {"Action":6.1, "Adventure":6.5, "Animation":6.6, "Comedy":6.5, "Crime":6.8, "Documentary":0,
"Drama":0, "Family":0, "Fantasy":0, "History":0, "Horror":0, "Music":0, "Mystery":0,
"Romance":0, "Science Fiction":0, "TV Movie":0, "Thriller":0, "War":0, "Western":0}

genre_list = ["Action","Adventure","Animation","Comedy","Crime","Documentary",
"Drama","Family","Fantasy","History","Horror","Music","Mystery",
"Romance","Science Fiction","TV Movie","Thriller","War","Western"]


class GUI(object):

	
	def __init__(self, master):
		self.master = master
		self.frame = tk.Frame(self.master)
		self.frame.grid()
		self.createWidgets()
		self.actor1 = 0
		self.actor2 = 0
		self.writer = 0
		self.director = 0
		self.producer = 0
		self.genres = []
		self.highscore = ""
		self.buttonState = 0
		#self.genreRating("Documentary")
		
		

	def createWidgets(self):
		directorEntry = StringVar()
		writerEntry = StringVar()
		producerEntry = StringVar()
		actorEntry = StringVar()
		actorEntry2 = StringVar()
		
		

		
		self.label_1 = tk.Label(self.frame, text="Director", fg='white', bg="black")
		self.label_1.config(font=("Courier", 20))
		self.label_2 = tk.Label(self.frame, text="Writer", fg='white', bg="black")
		self.label_2.config(font=("Courier", 20))
		self.label_3 = tk.Label(self.frame, text="Producer", fg='white', bg="black")
		self.label_3.config(font=("Courier", 20))
		self.label_4 = tk.Label(self.frame, text="Actor I", fg='white', bg="black")
		self.label_4.config(font=("Courier", 20))
		self.label_5 = tk.Label(self.frame, text="Actor II", fg='white', bg="black")
		self.label_5.config(font=("Courier", 20))
		self.label_6 = tk.Label(self.frame, text="Genre", fg="white", bg="black")
		self.label_6.config(font=("Courier", 20))
		
		self.text1 = tk.Text(self.frame, height=10, width=25, fg='white', bg="black")
		self.text1.config(font=("Courier", 20))
		self.text1.configure(state="normal")
		self.text1.tag_configure("center", justify="center")
		self.text1.insert(END,"Welcome\nto\nMovie\nRating\nPrediction")
		self.text1.tag_add("center", "1.0", "end")
		self.text1.configure(state="disable")
		
		self.entry_1 = tk.Entry(self.frame, bd =0, textvariable = directorEntry, fg='white', bg="black", width=30)
		self.entry_1.config(font=("Courier", 16))
		self.entry_2 = tk.Entry(self.frame, bd =0, textvariable = writerEntry, fg='white', bg="black", width=30)
		self.entry_2.config(font=("Courier", 16))
		self.entry_3 = tk.Entry(self.frame, bd =0, textvariable = producerEntry, fg='white', bg="black", width=30)
		self.entry_3.config(font=("Courier", 16))
		self.entry_4 = tk.Entry(self.frame, bd =0, textvariable = actorEntry, fg='white', bg="black", width=30)
		self.entry_4.config(font=("Courier", 16))
		self.entry_5 = tk.Entry(self.frame, bd =0, textvariable = actorEntry2, fg='white', bg="black", width=30)
		self.entry_5.config(font=("Courier", 16))
			
		self.listbox_1 = tk.Listbox(self.frame, selectmode=MULTIPLE, fg='white', bg="black", width=30)
		self.listbox_1.config(font=("Courier", 16))
		
		self.button_1 = tk.Button(self.frame, text = "Play", width = 12, command = self.sendCommand)
		self.button_1.config(font=("Courier", 16))
		
		
		self.button_2 = tk.Button(self.frame, text = "Top3", width = 12, command = self.xmlAuslesen)
		self.button_2.config(font=("Courier", 16))
		
		
		for key in sorted(genre_dic):
			self.listbox_1.insert(END,key)
			
		
		self.label_1.grid(row=0, pady=10)
		self.label_2.grid(row=1, pady=10)
		self.label_3.grid(row=2, pady=10)
		self.label_4.grid(row=3, pady=10)
		self.label_5.grid(row=4, pady=10)
		self.label_6.grid(row=5, pady=10)
		
		self.text1.grid(row=6, pady=20)
		self.text1.configure(state="disabled")
		
		self.entry_1.grid(row=0, column=1)
		self.entry_2.grid(row=1, column=1)
		self.entry_3.grid(row=2, column=1)
		self.entry_4.grid(row=3, column=1)
		self.entry_5.grid(row=4, column=1)
		
		
		self.button_1.grid(row=7, pady=10, padx=10)
		self.button_2.grid(row=8, pady=10, padx=10)
		
		
		self.listbox_1.grid(row=5, column=1, pady=10)

	#Durchschnittsbewertung von Filmen mit Schauspieler X
	def averageActor1Rating(self, actor_name):
		counter = 0
		actor_rating = 0
		treffer_name = searchPerson(actor_name)
		for role in treffer_name[0].roles:
			try:
				if role.userrating > 0:
					actor_rating = actor_rating + role.userrating
					counter = counter + 1
			except:
				continue
		print "average userrating from Movies with " + treffer_name[0].name + " as " + "Actor: " + str(actor_rating / counter)
		self.actor1 = (actor_rating / counter) * 1.2
		
	def averageActor2Rating(self, actor_name):
		counter = 0
		actor_rating = 0
		treffer_name = searchPerson(actor_name)
		for role in treffer_name[0].roles:
			try:
				if role.userrating > 0:
					actor_rating = actor_rating + role.userrating
					counter = counter + 1
			except:
				continue
		print "average userrating from Movies with " + treffer_name[0].name + " as " + "Actor: " + str(actor_rating / counter)
		self.actor2 = (actor_rating / counter) * 1.2

			
	
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
			try:
				for i in range(1, len(job)):
					title = title + " " + str(job[i])
				job[1] = title
				title = ""
				#print job[0:2]
			except:
				continue
			
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
		self.director = (director_rating / counter) * 1.2
			
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
			try:
				for i in range(1, len(job)):
					title = title + " " + str(job[i])
				job[1] = title
				title = ""
				#print job[0:2]
			except:
				continue
			
			
		for job in job_list:
			try:
				treffer_film = searchMovie(job[1])
				if treffer_film[0].userrating > 0:
					writer_rating = writer_rating + treffer_film[0].userrating
					counter = counter + 1
			except:
				continue
		print "average userrating from Movies with " + treffer_name[0].name + " as " + "Writer: " + str(writer_rating / counter)
		self.writer = (writer_rating / counter) * 1.2
		
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
			try:
				for i in range(1, len(job)):
				
					title = title + " " + str(job[i])
				job[1] = title
				title = ""
				#print job[0:2]
			except:
				continue
			
			
		for job in job_list:
			try:
				treffer_film = searchMovie(job[1])
				if treffer_film[0].userrating > 0:
					producer_rating = producer_rating + treffer_film[0].userrating
					counter = counter + 1	
			except:
				continue
		print "average userrating from Movies with " + treffer_name[0].name + " as " + "Producer: " + str(producer_rating / counter)
		self.producer = producer_rating / counter

	
	def genreSelect(self):
		genres = self.listbox_1.curselection()
		for item in genres:
			self.genres.append(genre_dic[genre_list[item]])
			print genre_list[item]
	
	def result(self):
		result = self.actor1+self.actor2+self.writer+self.director+self.producer
		for genre in self.genres:
			result = result + genre
		return format(result / (5+len(self.genres)),".2f")
		
	
	#Funktion um das durchschnittliche Rating eines Genres zu berechnen
	def genreRating(self, genreWahl):
		tokenizer = RegexpTokenizer(r'\w+')
		genre_list = []
		genre_rating = 0
		counter = 0
		
		for i in range(1,3000):
			try:
				for g in Movie(i).genres:
					genre = tokenizer.tokenize(str(g))
					if genre[-1] == genreWahl and Movie(i).userrating > 0:
						counter += 1
						genre_rating = genre_rating + Movie(i).userrating
						print Movie(i).userrating
			except:
				pass
			
		print genreWahl + ": " + str(genre_rating / counter)
		print counter
		
	def xmlAuslesen(self):
		
		if self.buttonState == 0:
			
			self.highscore = "Highscore\n\n"
			
			d = np.load("highscore.npy").item()
			
   			#d = {1:{"rat": 0, "dir": "X", "wri": "X", "pro": "X", "actI": "X", "actII": "X", "gen": "X, X, X"},
   			#	  2:{"rat": 0, "dir": "X", "wri": "X", "pro": "X", "actI": "X", "actII": "X", "gen": "X, X, X"},
   			#	  3:{"rat": 0, "dir": "X", "wri": "X", "pro": "X", "actI": "X", "actII": "X", "gen": "X, X, X"}}
   			
   			for i in range(1,4):
   				self.highscore = self.highscore + str(i) + "." + "(" + str(d[i]["rat"]) + ")\n"
   				self.highscore = self.highscore + "- Dir: " + d[i]["dir"] + "\n"
   				self.highscore = self.highscore + "- Wri: " + d[i]["wri"] + "\n"
   				self.highscore = self.highscore + "- Pro: " + d[i]["pro"] + "\n"
   				self.highscore = self.highscore + "- ActI: " + d[i]["actI"] + "\n"
   				self.highscore = self.highscore + "- ActII: " + d[i]["actII"] + "\n"
   				self.highscore = self.highscore + "- Gen: " + d[i]["gen"] + "\n\n"

   			self.text1.configure(state="normal")
   			self.text1.delete(1.0,END)
   			self.text1.insert(END,self.highscore)
   			self.text1.configure(state="disable")
			self.buttonState = 1
   		else:
   			self.text1.configure(state="normal")
			self.text1.delete(1.0,END)
			self.text1.configure(state="disable")
   			self.buttonState = 0
   			

   		
   	def xmlCheck(self):
   		
		d = np.load("highscore.npy").item()
		
		for i in range(1,4):
			if float(self.result()) >= d[1]["rat"]:
				d[3]["rat"] = d[2]["rat"]
				d[2]["rat"] = d[1]["rat"]
				d[1]["rat"] = float(self.result())
				
				d[3]["dir"] = d[2]["dir"]
				d[2]["dir"] = d[1]["dir"]
				d[1]["dir"] = self.entry_1.get()
				
				d[3]["wri"] = d[2]["wri"]
				d[2]["wri"] = d[1]["wri"]
				d[1]["wri"] = self.entry_2.get()
				
				d[3]["pro"] = d[2]["pro"]
				d[2]["pro"] = d[1]["pro"]
				d[1]["pro"] = self.entry_3.get()
				
				d[3]["actI"] = d[2]["actI"]
				d[2]["actI"] = d[1]["actI"]
				d[1]["actI"] = self.entry_4.get()
				
				d[3]["actII"] = d[2]["actII"]
				d[2]["actII"] = d[1]["actII"]
				d[1]["actII"] = self.entry_5.get()
				
				d[3]["gen"] = d[2]["gen"]
				d[2]["gen"] = d[1]["gen"]			
				genres = self.listbox_1.curselection()
				g = ""
				for item in genres:
					g = g + genre_list[item] + " "
				d[1]["gen"] = g
				break
			
			if float(self.result()) >= d[2]["rat"]:	
				d[3]["rat"] = d[2]["rat"]
				d[2]["rat"] = float(self.result())
				
				d[3]["dir"] = d[2]["dir"]
				d[2]["dir"] = self.entry_1.get()

				d[3]["wri"] = d[2]["wri"]
				d[2]["wri"] = self.entry_2.get()

				d[3]["pro"] = d[2]["pro"]
				d[2]["pro"] = self.entry_3.get()
				
				d[3]["actI"] = d[2]["actI"]
				d[2]["actI"] = self.entry_4.get()
				
				d[3]["actII"] = d[2]["actII"]
				d[2]["actII"] = self.entry_5.get()
				
				d[3]["gen"] = d[2]["gen"]			
				genres = self.listbox_1.curselection()
				g = ""
				for item in genres:
					g = g + genre_list[item] + " "
				d[2]["gen"] = g
				break				
			
			if float(self.result()) >= d[3]["rat"]:
				d[3]["rat"] = float(self.result())
				
				d[3]["dir"] = self.entry_1.get()
				
				d[3]["wri"] = self.entry_2.get()
				
				d[3]["pro"] = self.entry_3.get()
				
				d[3]["actI"] = self.entry_4.get()
				
				d[3]["actII"] = self.entry_5.get()
				
				genres = self.listbox_1.curselection()
				g = ""
				for item in genres:
					g = g + genre_list[item] + " "
				d[3]["gen"] = g
			
		np.save("highscore.npy", d)
   			
	
	def sendCommand(self):
	
		self.text1.configure(state="normal")
		self.text1.delete(1.0,END)
		
		try:
			self.averageActor1Rating(self.entry_4.get())
		except:
			print "Not found Actor1, Average Actor1 Rating 5.0"
			self.actor1 = 5.0
		try:
			self.averageActor2Rating(self.entry_5.get())
		except:
			print "Not found Actor2, Average Actor2 Rating 5.0"
			self.actor2 = 5.0
		try:
			self.averageDirectorRating()
		except:
			print "Not found Director, Average Director Rating 5.0"
			self.director = 5.0
		try:
			self.averageWriterRating()
		except:
			print "Not found Writer, Average Writer Rating 5.0"
			self.writer = 5.0
		try:
			self.averageProducerRating()	
		except:
			print "Not found Producer, Average Producer Rating 5.0"
			self.producer = 5.0
		try:
			self.genreSelect()
		except:
			print "Not found Genre"

		
		
		self.text1.tag_configure("center", justify="center")
		self.text1.insert(END,self.result())
		self.text1.tag_add("center", "1.0", "end")
		self.text1.configure(state="disable")
		self.xmlCheck()
		#self.newWindow = tk.Toplevel(self.master)
		#self.app = ResultWindow(self.newWindow, self.result())
		
	
def main(): 
	root = tk.Tk()
	root.title("Movie Rating Prediction")
	w = 600 
	h = 850

	# get screen width and height
	ws = root.winfo_screenwidth() # width of the screen
	hs = root.winfo_screenheight() # height of the screen

	# calculate x and y coordinates for the Tk root window
	x = (ws/2) - (w/2)
	y = (hs/2) - (h/2)

	# set the dimensions of the screen 
	# and where it is placed
	root.geometry('%dx%d+%d+%d' % (w, h, x, y))
	app = GUI(root)
	root.mainloop()

if __name__ == '__main__':
	main()
		
		