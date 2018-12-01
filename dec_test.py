#!/usr/bin/pyton

import unittest
import dec

class DecTestCase(unittest.TestCase):

	def testHexStringToIntArray(self):
		self.assertEqual(dec.hexstr_to_intarr("ff1020"), [255, 16, 32])

if __name__ == "__main__":
	unittest.main()
