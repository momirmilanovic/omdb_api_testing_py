
class Film(object):
	""""""
	def __init__(self, title, year, imdbId, typee):
		self.title = title
		self.year = year
		self.imdbId = imdbId
		self.type = typee

	def print_film(self):
		print "Film - title: " + self.title.encode("utf-8") + ", year: " + self.year.encode("utf-8") + ", imdbId: " + self.imdbId.encode("utf-8") + ", type: " + self.type.encode("utf-8")







		






