from django.test import TestCase, SimpleTestCase
from django.urls import reverse


# Create your tests here.

# testing the urls for loading the pages
class HomepageTests (SimpleTestCase):
	def test_url_exist_at_correct_location(self):
		response = self.client.get("/home/")
		self.assertEqual(response.status_code, 200)

	def test_url_available_by_name(self):
		response = self.client.get(reverse("home"))
		self.assertEqual(response.status_code, 200)

	def test_template_content(self):
		response = self.client.get(reverse("home"))	
		self.assertContains(response,"<h1 style='color:pink'>Homepage</h1>")



class AboutpageTest(SimpleTestCase):
	def test_url_exist_at_correct_location(self):
		response = self.client.get("/about/")
		self.assertEqual(response.status_code, 200)

	def test_url_available_by_name(self):
		response = self.client.get(reverse("about"))	
		self.assertEqual(response.status_code,200)

	def test_template_content(self):
		response = self.client.get(reverse("about"))
		self.assertContains(response,"<h1><i>About page!</i></h1>")		






class HomePageViewFunctionBased(SimpleTestCase):
	def test_url_exist_at_correct_location(self):
		response = self.client.get("/")
		self.assertEqual(response.status_code, 200)

	def test_url_available_by_name(self):
		response = self.client.get(reverse("testpage"))	


