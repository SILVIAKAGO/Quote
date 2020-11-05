from app import db
from app.models import Blogs

import unittest

class TestBlogs(unittest.TestCase):
    def setUp(self):
        self.new_blog=Blogs(title="money",body="money money")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_blog,Blogs))

    def tearDown(self):
        Blogs.query.delete()


    def test_blog_instance_saved(self):
        self.assertEquals(self.new_blog.title,"money")
        self.assertEquals(self.new_blog.body,"money money")

    def test_saved_blog(self):
        db.session.add(self.new_blog)
        self.assertTrue(len(Blogs.query.all())>0)
