from unittest import TestCase

from my_stuff.mojeFunkcje import mojaSuma

class TestSuma(TestCase):
    def test_suma(self):

        x = mojaSuma(2,3)
        self.assertEquals(x,5)
