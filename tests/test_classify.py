import unittest
import pygeoda

__author__ = "Xun Li <lixun910@gmail.com>, "

class TestClassify(unittest.TestCase):
    def setUp(self):
        self.guerry = pygeoda.open("./data/Guerry.shp")
        self.crm_prp = self.guerry.GetIntegerCol("Crm_prp")

    def test_stddev_breaks(self):
        pass