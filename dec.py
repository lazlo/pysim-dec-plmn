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
	ia = hexstr_to_intarr(twohexbytes)
	u16t = (ia[0] << 8)|ia[1]
	sel = []
	if u16t & (1 << 15):
		sel.append("UTRAN")
	if u16t & (1 << 14):
		sel.append("E-UTRAN")
	if u16t & (1 << 7):
		sel.append("GSM")
	if u16t & (1 << 6):
		sel.append("GSM COMPACT")
	if u16t & (1 << 5):
		sel.append("cdma2000 HRPD")
	if u16t & (1 << 4):
		sel.append("cdma2000 1xRTT")
	return sel
