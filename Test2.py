import unittest
from omdb_api_client import OmdbApiClient



class Test2(unittest.TestCase):

	def test2_run(self):
		print "\nTest 2"
		# Test 2 data
		Test1Movie="stem"
		Test2ExpectedReleased="23 Nov 2010"
		Test2ExpectedDirector="Mike Feurstein"
		Test2SearchedTitle="Activision: STEM - in the Videogame Industry"
		omdb_api_client = OmdbApiClient()
		searchReasult = omdb_api_client.search(Test1Movie)

		for f in searchReasult:
			f.print_film()
			if f.title == Test2SearchedTitle:
				idf = f.imdbId
				title = f.title

		dict_by_id = omdb_api_client.get_by_id(idf)
	   	self.assertEquals("Movie not released", Test2ExpectedReleased, dict_by_id["released"])
	   	self.assertEquals("Director not ...", Test2ExpectedDirector, dict_by_id["director"])
		#self.assertEquals( "1", "2", "jedan not eq")

if __name__ == '__main__':
	unittest.main()






