import unittest
import os
os.environ['TESTING'] = 'true'
from app import app

# Please run the command `python -m unittest -v tests.test_app` in the terminal to run the tests
class AppTestCase(unittest.TestCase):
  def setUp(self):
      self.client = app.test_client()
  def test_index(self):
      """
      Tests the index route ('/').
      Checks if the status code is 200 and if the response contains "my personal website".
      """
      rv = self.client.get('/')
      assert rv.status_code == 200
      assert b"my personal website" in rv.data

  def test_about(self):
      """
      Tests the about route ('/#about').
      Checks if the status code is 200 and if the response contains "About".
      """
      rv = self.client.get('/#about')
      assert rv.status_code == 200
      assert b"About" in rv.data

  def test_work(self):
      """
      Tests the about route ('/#experience').
      Checks if the status code is 200 and if the response contains "Experience".
      """
      rv = self.client.get('/#experience')
      assert rv.status_code == 200
      assert b"Experience" in rv.data

  def test_hobby(self):
      """
      Tests the about route ('/hobbies').
      Checks if the status code is 200 and if the response contains "Hobbies".
      """
      rv = self.client.get('/hobbies')
      assert rv.status_code == 200
      assert b"Hobbies" in rv.data

  def test_education(self):
      """
      Tests the about route ('/#projects').
      Checks if the status code is 200 and if the response contains "Projects".
      """
      rv = self.client.get('/#projects')
      assert rv.status_code == 200
      assert b"Projects" in rv.data

  def test_place(self):
      """
      Tests the about route ('/#contact').
      Checks if the status code is 200 and if the response contains "Contact".
      """
      rv = self.client.get('/#contact')
      assert rv.status_code == 200
      assert b"Contact" in rv.data