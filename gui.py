from Tkinter import *
import Tkinter as tk

from tmdb3 import *

from nltk import *

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
		self.actor = 0
		self.writer = 0
		self.director = 0
		self.producer = 0
		self.genres = []
		#self.genreRating("Documentary")

	def createWidgets(self):
		directorEntry = StringVar()
		writerEntry = StringVar()
		producerEntry = StringVar()
		actorEntry = StringVar()
		actorEntry2 = StringVar()

		
		self.label_1 = tk.Label(self.frame, text="Director", fg='white', bg="black")
		self.label_2 = tk.Label(self.frame, text="Writer", fg='white', bg="black")
		self.label_3 = tk.Label(self.frame, text="Producer", fg='white', bg="black")
		self.label_4 = tk.Label(self.frame, text="Actor I", fg='white', bg="black")
		self.label_5 = tk.Label(self.frame, text="Actor II", fg='white', bg="black")
		self.label_6 = tk.Label(self.frame, text="Genre", fg="white", bg="black")
		
		self.entry_1 = tk.Entry(self.frame, bd =0, textvariable = directorEntry, fg='white', bg="black")
		self.entry_2 = tk.Entry(self.frame, bd =0, textvariable = writerEntry, fg='white', bg="black")
		self.entry_3 = tk.Entry(self.frame, bd =0, textvariable = producerEntry, fg='white', bg="black")
		self.entry_4 = tk.Entry(self.frame, bd =0, textvariable = actorEntry, fg='white', bg="black")
		self.entry_5 = tk.Entry(self.frame, bd =0, textvariable = actorEntry2, fg='white', bg="black")
			
		self.listbox_1 = tk.Listbox(self.frame, selectmode=MULTIPLE, fg='white', bg="black")
		
		self.button_1 = tk.Button(self.frame, text = "Play", width = 12, command = self.sendCommand)
		
		for key in sorted(genre_dic):
			self.listbox_1.insert(END,key)
			
		
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
		self.entry_5.grid(row=4, column=1)
		
		
		self.button_1.grid(row=10)
		
		self.listbox_1.grid(row=5, column=1)

	#Durchschnittsbewertung von Filmen mit Schauspieler X
	def averageActorRating(self):
		counter = 0
		actor_rating = 0
		treffer_name = searchPerson(self.entry_4.get())
		for role in treffer_name[0].roles:
			try:
				if role.userrating > 0:
					actor_rating = actor_rating + role.userrating
					counter = counter + 1
			except:
				continue
		print "average userrating from Movies with " + treffer_name[0].name + " as " + "Actor: " + str(actor_rating / counter)
		self.actor = actor_rating / counter

			
	
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
		self.director = director_rating / counter
			
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
		self.writer = writer_rating / counter
		
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
	
	def result(self):
		result = self.actor+self.writer+self.director+self.producer
		for genre in self.genres:
			result = result + genre
		return str(result / (4+len(self.genres)))
		
	
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
	
	def sendCommand(self):
	
		try:
			self.averageActorRating()
		except:
			print "Not found Actor, Average Actor Rating 5.0"
			self.actor = 5.0
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

		
		
		self.newWindow = tk.Toplevel(self.master)
		self.app = ResultWindow(self.newWindow, self.result())
			
		
		
class ResultWindow(object):

	def __init__(self, master, blabla):
		self.master = master
		self.frame = tk.Frame(self.master)
		self.label_progress = tk.Label(self.frame, text= blabla)
		self.label_progress.grid()
		self.frame.grid()

	def close_windows(self):
		self.master.destroy()

def main(): 
	root = tk.Tk()
	root.title("Movie Rating Prediction")
	app = GUI(root)
	root.mainloop()

if __name__ == '__main__':
	main()
		
		