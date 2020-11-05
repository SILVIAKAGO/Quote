import unittest
from app import db
from app.models import Comments,Users

class TestComments(unittest.TestCase):

    def setUp(self):
        self.user_dean=Users(username='wambui',password='neema',email='pwambui13@gmail.com')
        self.new_comment=Comments(email="paulyne@gmail.com",username="user",comment="dope",blog_id=20)

    def tearDown(self):
        Comments.query.delete()
        Users.query.delete()

    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.email,"paulyne@gmail.com")
        self.assertEquals(self.new_comment.username,"user")
        self.assertEquals(self.new_comment.comment,"dope")
        self.assertEquals(self.new_comment.blog_id,20)
        

    def test_save_comment(self):
        self.new_comment.save_comments()
        self.assertTrue(len(Comments.query.all())>0)

    def test_get_comment_by_id(self):
        self.new_comment.save_comments()
        got_comments=Comments.get_comments(20)
        self.assertTrue(len(got_comments)==1)
