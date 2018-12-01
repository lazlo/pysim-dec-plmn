def hexstr_to_intarr(s):
	a = []
	for i in range(0, len(s) / 2):
		offset = 2 * i
		msb_nib = s[offset]
		lsb_nib = s[offset + 1]
		tmp = msb_nib + lsb_nib
		v = int(tmp, 16)
		a.append(v)
	return a

# Accepts hex string representing three bytes
def mcc_from_plmn(plmn):
	ia = hexstr_to_intarr(plmn)
	digit1 = ia[0] & 0x0F		# 1st byte, LSB
	digit2 = (ia[0] & 0xF0) >> 4	# 1st byte, MSB
	digit3 = ia[1] & 0x0F		# 2nd byte, LSB
	mcc = digit1 * 100
	mcc += digit2 * 10
	mcc += digit3
	return mcc

def mnc_from_plmn(plmn):
	ia = hexstr_to_intarr(plmn)
	digit1 = ia[2] & 0x0F		# 3rd byte, LSB
	digit2 = (ia[2] & 0xF0) >> 4	# 3rd byte, MSB
	digit3 = (ia[1] & 0xF0) >> 4	# 2nd byte, MSB
	mnc = 0
	# signifies two digit MNC
	if digit3 == 0xF:
		mnc += digit1 * 10
		mnc += digit2
	else:
		mnc += digit1 * 100
		mnc += digit2 * 10
		mnc += digit3
	return mnc

def act(twohexbytes):
	act_list = [
		{'bit': 15, 'name': "UTRAN"},
		{'bit': 14, 'name': "E-UTRAN"},
		{'bit':  7, 'name': "GSM"},
		{'bit':  6, 'name': "GSM COMPACT"},
		{'bit':  5, 'name': "cdma2000 HRPD"},
		{'bit':  4, 'name': "cdma2000 1xRTT"},
	]
	ia = hexstr_to_intarr(twohexbytes)
	u16t = (ia[0] << 8)|ia[1]
	sel = []
	for a in act_list:
		if u16t & (1 << a['bit']):
			sel.append(a['name'])
	return sel
