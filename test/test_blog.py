
import unittest
from app.models import Blog, User,
from app import db


class BlogModelTest(unittest.TestCase):
    def setUp(self):
        self.user_charles = User(username='kimani', password='st.bandict', email='test@bandict.com')
        self.new_blog = Blog(id=1, title='Test', content='This testing blog', user_id=self.user_kimani.id)

    def tearDown(self):
        Blog.query.delete()
        User.query.delete()

    def test_check_instance_variables(self):
        self.assertEquals(self.new_blog.title, 'Test')
        self.assertEquals(self.new_blog.content, 'This testing blog')
        self.assertEquals(self.new_blog.user_id, self.user_dennis.id)

    def test_save_blog(self):
        self.new_blog.save()
        self.assertTrue(len(Blog.query.all()) > 0)

 