import unittest
import os
os.environ['TESTING'] = 'true'
from app import app

# Please run the command `python -m unittest -v tests.test_app` in the terminal to run the tests
class AppTestCase(unittest.TestCase):
  def setUp(self):
      self.client = app.test_client()
  def test_index(self):
      """Test the index route"""
      rv = self.client.get('/')
      assert rv.status_code == 200
      assert b"my personal website" in rv.data

  def test_about(self):
      """Test the about route"""
      rv = self.client.get('/#about')
      assert rv.status_code == 200
      assert b"About" in rv.data

  def test_work(self):
      """Test the work route"""
      rv = self.client.get('/#experience')
      assert rv.status_code == 200
      assert b"Experience" in rv.data

  def test_hobby(self):
      """Test the hobby route"""
      rv = self.client.get('/hobbies')
      assert rv.status_code == 200
      assert b"Hobbies" in rv.data

  def test_education(self):
      """Test the education route"""
      rv = self.client.get('/#projects')
      assert rv.status_code == 200
      assert b"Projects" in rv.data

  def test_place(self):
      """Test the place route"""
      rv = self.client.get('/#contact')
      assert rv.status_code == 200
      assert b"Contact" in rv.data


