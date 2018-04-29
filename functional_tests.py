from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self):
		# Wallace checks the homepage.
		self.browser.get('http://localhost:8000')

		# Wallace sees that the page title and header mention to-do lists
		self.assertIn('To-Do', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do', header_text)

		# Wallace is invited to enter a to-do item immediately.
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(
			inputbox.get_attribute('placeholder'),
			'Enter a to-do item'
		)

		# Wallace types "Buy cheese" into a text box.
		inputbox.send_keys('Buy cheese')

		# When Wallace hits enter, the page updates to show
		# "1. Buy cheese" as a to-do list item
		inputbox.send_keys(Keys.ENTER)
		time.sleep(1)

		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertTrue(
			any(row.text == '1: Buy cheese' for row in rows)
		)

		# There is stil la text box inviting Wallace to enter another item.
		# Wallace enters "Buy crackers"
		self.fail('Finish the test!')

		# The page updates and now shows two items in the list.


if __name__ == '__main__':
	unittest.main()
