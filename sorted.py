L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
	return t[0]# t means the list L. Here t[0] means name part from every element of L.
L2 = sorted(L, key=by_name)
print(L2)
