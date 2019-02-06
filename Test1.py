import unittest
from omdb_api_client import OmdbApiClient


class Test1(unittest.TestCase):

    def test1_run(self):
    	print "\nTest 1"
    	#assert (5 > 0),"Result has less then 30 items"
    	#assert (5 >= 0),"No titles found"
        #self.assertEqual('30', '30')
        # Test 1 data
        Test1Expected="30"
        Test1Movie="stem"		
        Test1SearchedTitle1="The STEM Journals"
        Test1SearchedTitle2="Activision: STEM - in the Videogame Industry"
        omdb_api_client = OmdbApiClient()
        #omdb_api_client.search(Test1SearchedTitle1)
        searchReasult = omdb_api_client.search(Test1Movie)
        #print "searchReesult len: " + str(len(searchReasult))

        contain1 = False; contain2 = False; containStem = False
        for f in searchReasult:
        	f.print_film()
        	if f.title == Test1SearchedTitle1:
        		contain1 = True
        	if f.title == Test1SearchedTitle2:
        		contain2 = True
        containStem = contain1 and contain2

        print "contain1: " + str(contain1) + " contain2: " + str(contain2) + " containStem: " + str(containStem)

        assert(contain1 and contain2), "No searched items"
        assert(len(searchReasult) >= 30), "Less then 30 results"




if __name__ == '__main__':
    unittest.main()






