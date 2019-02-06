import unittest
from omdb_api_client import OmdbApiClient


class Test3(unittest.TestCase):

    def test3_run(self):
    	print "\nTest 3"

    	# Test 3 data
    	Test3Title="The STEM Journals"
    	Test3ExpectedInPlot="Science, Technology, Engineering and Math"
    	Test3xpectedRuntime="22 min"

    	omdb_api_client = OmdbApiClient()
    	title_dict = omdb_api_client.get_by_title(Test3Title)
    	#self.assertTrue("Plot not contain", )
    	self.assertEqual("Movie runtime", title_dict["runtime"], Test3xpectedRuntime)
        #self.assertEqual('30', '30')


if __name__ == '__main__':
    unittest.main()






