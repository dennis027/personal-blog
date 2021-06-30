
import unittest
from app.models import Comment, Blog, User
from app import db

class CommentModelTest(unittest.TestCase):
    def setUp(self):
        
        self.new_comment = Comment(id = 1, comment = 'Test comment', user = self.user_bandict, blog_id = self.new_blog)
        
    def tearDown(self):
        Blog.query.delete()
        User.query.delete()
    
    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.comment,'Test comment')
        self.assertEquals(self.new_comment.user,self.user_bandict)
        self.assertEquals(self.new_comment.blog_id,self.new_blog)
