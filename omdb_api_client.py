import json, requests
from film import Film


class OmdbApiClient(object):
	""""""
	def __init__(self):
		self.api_key = "6761b6e1"
		self.omdb = "http://www.omdbapi.com/?"

	def search (self, s):
		allFilms = []

		omdb_query = self.omdb + "s=" + s + "&apikey=" + self.api_key
		# http://www.omdbapi.com/?s=godfather&apiKey=6761b6e1
		# http://www.omdbapi.com/?s=stem&apikey=6761b6e1
		# http://www.omdbapi.com/?s=stem&apikey=6761b6e1&page=1
		# 
		print "search for omdb_query: " + omdb_query
		pages = self.pagination(omdb_query);
		print "pages: " + str(pages)
		for i in range (1, pages+1):
			omdb_query_page = omdb_query + "&page=" + str(i)
			response = requests.get(omdb_query_page)
			jsoned_response = json.loads(response.text)
			print "omdb_query_page: " + omdb_query_page
			search_response = jsoned_response.get("Search")
			for j in range (1, len(search_response)):
				film = Film(search_response[j].get("Title"), search_response[j].get("Year"), search_response[j].get("imdbID"), search_response[j].get("Type"))
				film.print_film()
				allFilms.append(film)

		return allFilms


	def get_by_id(self, id):
		omdb_query_id = self.omdb + "i=" + id + "&apikey=" + self.api_key
		print "omdb_query_id: " + omdb_query_id
		response = requests.get(omdb_query_id)
		jsoned_response = json.loads(response.text)
		released = jsoned_response.get("released")
		director = jsoned_response.get("director")
		id_dict = {}
		id_dict["released"] = released
		id_dict["director"] = director
		return id_dict

	def get_by_title(self, title):
		omdb_query_title = self.omdb + "t=" + title + "&apikey=" + self.api_key
		print "omdb_query_title: " + omdb_query_title
		response = requests.get(omdb_query_title)
		jsoned_response = json.loads(response.text)
		plot = jsoned_response.get("Plot")
		runtime = jsoned_response.get("Runtime")
		title_dict = {"plot" : plot, "runtime" : runtime}
		#id_dict["released"] = released
		#id_dict["director"] = director
		return title_dict


	def pagination(self, omdb_query):
		print "pagination for this query: " + omdb_query
		response = self.omdbQuery(omdb_query)
		total_results = response["totalResults"]
		print "total_results: " + total_results
		if (int(total_results) % 10 == 0):
			pages = total_results/10
		else:
			pages = int(total_results)/10 + 1
		return pages


	def omdbQuery(self, omdb_query):
		print "omdb_query: " + omdb_query
		response = requests.get(omdb_query)
		response_dict = json.loads(response.text)
		#total_results = jsoned_response["totalResults"]
		#print "total_results: " + total_results
		return response_dict
		


		






