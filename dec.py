def hexstr_to_intarr(s):
	a = []
	for i in range(0, len(s) / 2):
		msb_nib = s[2 * i]
		lsb_nib = s[(2 * i) + 1]
		tmp = msb_nib + lsb_nib
		v = int(tmp, 16)
		a.append(v)
	return a
