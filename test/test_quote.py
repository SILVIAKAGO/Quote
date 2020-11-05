import unittest
from app.models import Quote

class TestQuote(unittest.TestCase):
    new_blog=[]
    def setUp(self):
        self.new_quote=(Quote(quote="like flower",author="i"))

    def test_quote_saved(self):
        self.assertEquals(self.new_quote.quote,"like flower")
        self.assertEquals(self.new_quote.author,"i")
