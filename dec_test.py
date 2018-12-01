#!/usr/bin/pyton

import unittest
import dec

class DecTestCase(unittest.TestCase):

	def testHexStringToIntArray(self):
		self.assertEqual(dec.hexstr_to_intarr("ff1020"), [255, 16, 32])

	def testDecMCCfromPLMN(self):
		self.assertEqual(dec.mcc_from_plmn("92f501"), 295)

	def testDecMNCfromPLMN_twiDigitMNC(self):
		self.assertEqual(dec.mnc_from_plmn("92f501"), 10)

	def testDecMNCfromPLMN_threeDigitMNC(self):
		self.assertEqual(dec.mnc_from_plmn("031263"), 361)

	def testDecAct_noneSet(self):
		self.assertEqual(dec.act("0000"), [])

	def testDecAct_allSet(self):
		self.assertEqual(dec.act("ffff"), ["UTRAN", "E-UTRAN", "GSM", "GSM COMPACT", "cdma2000 HRPD", "cdma2000 1xRTT"])

if __name__ == "__main__":
	unittest.main()
