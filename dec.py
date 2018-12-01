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
