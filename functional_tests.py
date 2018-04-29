from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self):
		# User checks the homepageself.
		self.browser.get('http://localhost:8000')

		# Page title is 'To-Do'
		self.assertIn('To-Do', self.browser.title)
		self.fail('Finish the test!')

if __name__ == '__main__':
	unittest.main()
