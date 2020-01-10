import unittest
import pygeoda

__author__ = "Xun Li <lixun910@gmail.com>, "

class TestLISA(unittest.TestCase):
    def setUp(self):
        self.guerry = pygeoda.open("./data/Guerry.shp")
        self.queen_w = pygeoda.weights.queen(self.guerry)
        self.crm_prp = self.guerry.GetIntegerCol("Crm_prp")

    def test_local_moran(self):
        lisa = pygeoda.local_moran(self.queen_w, self.crm_prp)

        lms = lisa.GetLISAValues()
        self.assertEqual(lms[0], 0.015431978309803657)
        self.assertEqual(lms[1], 0.3270633223656033)
        self.assertEqual(lms[2], 0.3270633223656033)

        pvals = lisa.GetPValues()
        self.assertEqual(pvals[0], 0.41399999999999998)
        self.assertEqual(pvals[1], 0.123)
        self.assertEqual(pvals[2], 0.001)

        cvals = lisa.GetClusterIndicators()
        self.assertEqual(cvals[0], 0)
        self.assertEqual(cvals[1], 0)
        self.assertEqual(cvals[2], 1)

    def test_local_geary(self):
        lisa = pygeoda.local_geary(self.queen_w, self.crm_prp)

        lvals = lisa.GetLISAValues()
        self.assertEqual(lvals[0], 0.3980833011783602)
        self.assertEqual(lvals[1], 0.3270633223656033)
        self.assertEqual(lvals[2], 0.3270633223656033)

        pvals = lisa.GetPValues()
        self.assertEqual(pvals[0], 0.41399999999999998)
        self.assertEqual(pvals[1], 0.123)
        self.assertEqual(pvals[2], 0.001)

        cvals = lisa.GetClusterIndicators()
        self.assertEqual(cvals[0], 0)
        self.assertEqual(cvals[1], 0)
        self.assertEqual(cvals[2], 1)