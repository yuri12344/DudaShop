from selenium import webdriver
import unittest

class NewVisitor(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
    
    def tearDown(self) -> None:
        return self.browser.quit()
    
    def test_can_go_to_home_page(self):
        # Go to the home page
        self.browser.get('http://localhost:3000')

        self.assertIn('Duda Store', self.browser.title)



if __name__ == '__main__':
    unittest.main(warnings='ignore')